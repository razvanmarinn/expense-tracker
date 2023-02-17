"""This module contains the login // controller for login"""
from PyQt6.QtWidgets import QDialog
from UI.Login import Ui_LoginForm
from src.controllers.login_controller import LoginController


class LoginFormWindow(QDialog, Ui_LoginForm):
    """Login form window"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.controller = LoginController(self)
        self.b_login.clicked.connect(self.controller.login)
        self.b_createacc.clicked.connect(self.controller.sign_up)
