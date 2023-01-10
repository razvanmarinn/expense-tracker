from PyQt6.QtWidgets import QMainWindow, QDialog
from UI.Login import Ui_LoginForm
from templates.Accounts import AccountsFormTab
from templates.User import UserModel, User
from templates.Util import passwordHashing
import time
import bcrypt
import psycopg2

conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432'
)
cursor = conn.cursor()
conn.autocommit = True


salt = bcrypt.gensalt()

class LoginFormWindow(QDialog, Ui_LoginForm):
    """Login form window"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.user_model = UserModel()
        self.b_login.clicked.connect(self.login)
        self.b_createacc.clicked.connect(self.sign_up)

    def login(self):
        """Login button functionality"""
        user = self.user_model.get_user_by_username(self.le_username.text())
        if user is  None:
            self.l_loggedin.setText("Username doesn't exist")
        else:

            if bcrypt.checkpw(self.le_password.text().encode('utf-8') , bytes(user[2] , 'utf-8')):
                self.l_loggedin.setText("Logged in")
                current_user =  User(user[1], user[2])
                current_user.id = user[0]
                time.sleep(2)
                self.switch_to_accounts(current_user)
            else:
                self.l_loggedin.setText("Password is not matching")


    def sign_up(self):
        """Create the user account and encrypt the password using BCRYPT"""
        user = self.user_model.get_user_by_username(self.le_username.text())
        if user is None:
            hashed_pass = passwordHashing(self.le_password.text())
            new_user = User(self.le_username.text(), hashed_pass)
            self.user_model.create_user(new_user)
            new_user.id = cursor.lastrowid
            self.l_loggedin.setText("Account created")
        else:
            self.l_loggedin.setText("username already exists")

    def switch_to_accounts(self, user):
        """Switch to accounts tab"""
        self.window= QMainWindow()
        self.ui_accounts = AccountsFormTab(LoginFormWindow, user)    #creating an object
        self.hide()





