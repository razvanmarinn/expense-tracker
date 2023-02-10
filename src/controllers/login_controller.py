"""Login controller"""
import psycopg2
from PyQt6 import QtTest
from PyQt6.QtWidgets import QMainWindow
from general.util import make_api_get_request, make_api_post_request, update_env_file
from src.views.main import MainWindow
from src.dtos.user_dto import UserDTO
from src.headers import headers


class LoginController():
    """Login controller"""
    def __init__(self, view):
        self.view = view
        self.view.b_login.clicked.connect(self.login)
        self.view.b_createacc.clicked.connect(self.sign_up)

        self.conn = psycopg2.connect(
        database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432'
        )
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True


    def create_user_dto(self, username, user_id):
        """Create a user dto"""
        user_dto = UserDTO(username, user_id)
        return user_dto

    def login(self):
        endpoint_url = "http://{}:{}/user/login/{}/{}".format("127.0.0.1", "8000", self.view.le_username.text(), self.view.le_password.text())
        user_data = make_api_post_request(endpoint_url, headers=headers)
        if "detail" in user_data:
            if user_data["detail"] == "User not found" :
                self.view.l_loggedin.setText("Username doesn't exist")
            elif user_data["detail"] == "Wrong password":
                self.view.l_loggedin.setText("Password is not matching")
        else:
            self.view.l_loggedin.setText("Logged in")
            QtTest.QTest.qWait(500)
            user_dto = self.create_user_dto(user_data["username"], user_data["id"])
            update_env_file("API_KEY", user_data["access_token"])
            self.switch_to_accounts(user_dto)

    def sign_up(self):
        """Create the user account and encrypt the password using BCRYPT"""
        endpoint_url = "http://{}:{}/user/get_user/{}".format("127.0.0.1", "8000", self.view.le_username.text())
        user_data = make_api_get_request(endpoint_url, headers=headers)
        if user_data is None:
            self.view.l_loggedin.setText("username already exists")

        endpoint_url = "http://{}:{}/user/create_user/{}/{}".format("127.0.0.1", "8000", self.view.le_username.text(), self.view.le_password.text())
        user_data = make_api_post_request(endpoint_url, headers=headers)
        self.view.l_loggedin.setText("Account created")


    def switch_to_accounts(self, user: UserDTO):
        """Switch to accounts tab"""
        self.window= QMainWindow()
        self.ui_accounts = MainWindow(user)
        self.view.hide()