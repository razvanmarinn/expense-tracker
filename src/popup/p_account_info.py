"""This module contains account info popup class"""
from PyQt6.QtWidgets import QDialog
from UI.info import Ui_Form

class AccountInfoPopup(QDialog, Ui_Form):
    """Account info popup class"""
    def __init__(self, acc_window):
        super().__init__(acc_window)
        self.setupUi(self, acc_window)
        self.acc_window = acc_window
        self.show()

        self.l_iban.setText(self.acc_window.current_accout_iban)
        self.l_accountid.setText(str(self.acc_window.current_account_id))
