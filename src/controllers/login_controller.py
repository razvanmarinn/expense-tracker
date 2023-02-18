"""Login controller"""
from PyQt6 import QtTest
from PyQt6.QtWidgets import QMainWindow
from general.util import make_api_get_request, make_api_post_request, update_env_file
from general.headers import headers, base_url
from src.views.main import MainWindow
from src.dtos.user_dto import UserDTO


class LoginController():
    """Login controller"""
    def __init__(self, view):
        self.view = view

    def create_user_dto(self, username, user_id):
        """Create a user dto"""
        user_dto = UserDTO(username, user_id)
        return user_dto

    def login(self):
        """Login the user"""
        # try:
        endpoint_url = f"{base_url}/user/login/{self.view.le_username.text()}/{self.view.le_password.text()}"
        user_data = make_api_post_request(endpoint_url, headers=headers)
        if "detail" in user_data:
            if user_data["detail"] == "User not found":
                self.view.l_loggedin.setText("Username doesn't exist")
            elif user_data["detail"] == "Wrong password":
                self.view.l_loggedin.setText("Password is not matching")
        else:
            self.view.l_loggedin.setText("Logged in")
            QtTest.QTest.qWait(500)
            user_dto = self.create_user_dto(user_data["username"], user_data["id"])
            update_env_file("API_KEY", user_data["access_token"])
            self.switch_to_accounts(user_dto)
        # except Exception as exception_thrown:
        #     print(exception_thrown)
        #     self.view.l_loggedin.setText("Error")

    def sign_up(self):
        """Create the user account and encrypt the password using BCRYPT"""
        endpoint_url = f"{base_url}/user/get_user/{self.view.le_username.text()}"
        user_data = make_api_get_request(endpoint_url, headers=headers)
        if user_data is None:
            self.view.l_loggedin.setText("username already exists")

        endpoint_url = f"{base_url}/user/create_user/{self.view.le_username.text()}/{self.view.le_password.text()}"
        user_data = make_api_post_request(endpoint_url, headers=headers)
        self.view.l_loggedin.setText("Account created")

    def switch_to_accounts(self, user: UserDTO):
        """Switch to accounts tab"""
        QMainWindow()
        MainWindow(user)
        self.view.hide()
