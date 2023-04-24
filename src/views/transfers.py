"""Transfer Frame"""
from UI.transfer import Ui_TransferFrame
from src.controllers.transfer_controller import TransferController


# pylint: disable=E1121

class TransferFrame(Ui_TransferFrame):
    """Transfer Frame"""
    def __init__(self, parent):
        Ui_TransferFrame.__init__(self)
        self.parent = parent
        self.controller = TransferController()
        self.pb_createtransfer.clicked.connect(lambda: self.controller.create_transfer(self.parent.current_account_id, self.le_username.text(), self.le_value.text(), self.le_currency.text(), self.le_description.text()),
                                               self.le_currency.clear(), self.le_description.clear(), self.le_username.clear(), self.le_value.clear())  # to add message box
