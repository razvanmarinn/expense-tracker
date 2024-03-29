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
        try:
            self.l_iban.setText(self.acc_window.account_dto.account_uuid)
            self.l_accountid.setText(str(self.acc_window.account_dto.account_id))
        except AttributeError:
            self.l_iban.setText("No account selected")
            self.l_accountid.setText("No account selected")
