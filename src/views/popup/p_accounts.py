"""This module contains the class for the popup window to add a custom category to the combobox"""
from PyQt6.QtWidgets import QDialog
from UI.popup import Ui_Form
from src.controllers.popup_accounts_controller import PopUpAccountsController


class PopUpWindowAcc(QDialog, Ui_Form):
    """Popup window class"""
    def __init__(self, acc_window):
        super().__init__(acc_window)
        self.setupUi(self)
        self.show()
        self.acc_window = acc_window
        self.controller = PopUpAccountsController(self, self.acc_window)
