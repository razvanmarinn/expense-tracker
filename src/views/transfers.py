"""Transfer Frame"""
from UI.transfer import Ui_TransferFrame
from src.controllers.transfer_controller import TransferController


class TransferFrame(Ui_TransferFrame):
    """Transfer Frame"""
    def __init__(self, parent):
        Ui_TransferFrame.__init__(self)
        self.parent = parent
        self.controller = TransferController()
        self.pb_createtransfer.clicked.connect(lambda: self.controller.create_transfer(self.parent.current_account_id, self.le_username.text(), self.le_value.text(), self.le_currency.text(), self.le_description.text()))
