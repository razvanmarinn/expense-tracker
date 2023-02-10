from UI.transfer import Ui_TransferFrame


class TransferFrame(Ui_TransferFrame):
    def __init__(self, parent):
        Ui_TransferFrame.__init__(self)
        self.parent = parent

        self.pb_createtransfer.clicked.connect(self.create_transfer)

    def create_transfer(self):
        pass
        # """Create transfer method"""
        # new_transfer = Transfer(self.parent.current_account_id, self.le_uuid.text(), int(self.le_value.text()), self.le_description.text())
        # self.transfer_model.create_transfer(new_transfer)
        # self.hide()
