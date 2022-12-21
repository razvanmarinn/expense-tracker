from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog
import sys
from UI.Login import Ui_LoginForm
from templates.Acc import AccountsFormTab
from templates.Buttons import LoginButton, CreateUserAcc




class LoginFormWindow(QDialog, Ui_LoginForm):
    idd = []
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.LoginButton = LoginButton(self)
        self.CreateAccButton = CreateUserAcc(self)
        self.b_login.clicked.connect(self.LoginButton.functionality)
        self.b_createacc.clicked.connect(self.CreateAccButton.functionality)

    
    def switch_to_accounts(self):
        self.window= QMainWindow()
        self.ui= AccountsFormTab(LoginFormWindow)    #creating an object 
        self.hide()






app = QApplication(sys.argv)
Login = LoginFormWindow()
sys.exit(app.exec())


