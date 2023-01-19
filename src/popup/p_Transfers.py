"""This file contains the popup for creating a new transfer"""
from PyQt6.QtWidgets import QDialog
from UI.transfer import Ui_createtransfer
from src.models import TransferModel, Transfer


class TransferPopup(QDialog, Ui_createtransfer):
    """Transfer popup class"""
    def __init__(self, acc_window):
        super().__init__(acc_window)
        self.setupUi(self, acc_window)
        self.acc_window = acc_window
        self.transfer_model = TransferModel()
        self.pb_createtransfer.clicked.connect(self.create_transfer)

    def create_transfer(self):
        """Create transfer method"""
        new_transfer = Transfer(self.acc_window.current_account_id, self.le_iban.text(), int(self.le_value.text()), self.le_description.text())
        self.transfer_model.create_transfer(new_transfer)
        self.acc_window.create_new()
        self.hide()
