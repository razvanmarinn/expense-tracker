from UI.transfer import Ui_createtransfer
from PyQt6.QtWidgets import QDialog
from templates.Models import TransferModel, Transfer


class TransferPopup(QDialog, Ui_createtransfer):

    def __init__(self, AccWindow):
        super().__init__(AccWindow)
        self.setupUi(self, AccWindow)
        self.AccWindow = AccWindow
        self.transfer_model = TransferModel()
        self.pb_createtransfer.clicked.connect(self.create_transfer)

    def create_transfer(self):

        self.transfer_model.create_transfer(Transfer(self.AccWindow.current_account_id, self.le_iban.text(), int(self.le_value.text()), self.le_description.text()))
        self.AccWindow.create_new()
        self.hide()