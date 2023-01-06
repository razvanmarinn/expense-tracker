from PyQt6.QtWidgets import QMainWindow, QDialog 
from UI.Login import Ui_LoginForm
from templates.Accounts import AccountsFormTab
from templates.Buttons import LoginButton, CreateUserAcc



class LoginFormWindow(QDialog, Ui_LoginForm):
    """Login form window"""
    idd = []
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.login_button = LoginButton(self)
        self.create_acc_button = CreateUserAcc(self)
        self.b_login.clicked.connect(self.login_button.functionality)
        self.b_createacc.clicked.connect(self.create_acc_button.functionality)


    def switch_to_accounts(self):
        """Switch to accounts tab"""
        self.window= QMainWindow()
        self.ui_accounts = AccountsFormTab(LoginFormWindow)    #creating an object
        self.hide()