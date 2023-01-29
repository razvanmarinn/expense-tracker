"""Login controller"""
import time
import bcrypt
import psycopg2
from PyQt6.QtWidgets import QMainWindow
from general.util import password_hashing
#from src.views.accounts import AccountsFormTab
from src.views.main import MainWindow
from src.models import UserModel, User
from src.dtos.user_dto import UserDTO


salt = bcrypt.gensalt()

class LoginController():
    """Login controller"""
    def __init__(self, view):
        self.view = view
        self.user_model = UserModel()
        self.view.b_login.clicked.connect(self.login)
        self.view.b_createacc.clicked.connect(self.sign_up)

        self.conn = psycopg2.connect(
        database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432'
        )
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True


    def create_user_dto(self, user: User):
        """Create a user dto"""
        user_dto = UserDTO(user)
        return user_dto

    def login(self):
        """Login button functionality"""
        user = self.user_model.get_user_by_username(self.view.le_username.text())
        if user is  None:
            self.view.l_loggedin.setText("Username doesn't exist")
        else:

            if bcrypt.checkpw(self.view.le_password.text().encode('utf-8') , bytes(user[2] , 'utf-8')):
                self.view.l_loggedin.setText("Logged in")
                current_user =  User(user[1], user[2])
                current_user.id = user[0]
                user_dto = self.create_user_dto(current_user)
                time.sleep(2)
                self.switch_to_accounts(user_dto)
            else:
                self.view.l_loggedin.setText("Password is not matching")


    def sign_up(self):
        """Create the user account and encrypt the password using BCRYPT"""
        user = self.user_model.get_user_by_username(self.view.le_username.text())
        if user is None:
            hashed_pass = password_hashing(self.view.le_password.text())
            new_user = User(self.view.le_username.text(), hashed_pass)
            user_dto = self.create_user_dto(new_user)
            self.user_model.create_user(user_dto)
            new_user.id = self.cursor.lastrowid
            self.view.l_loggedin.setText("Account created")
        else:
            self.view.l_loggedin.setText("username already exists")

    def switch_to_accounts(self, user: UserDTO):
        """Switch to accounts tab"""
        self.window= QMainWindow()
        self.ui_accounts = MainWindow(user)
        self.view.hide()
