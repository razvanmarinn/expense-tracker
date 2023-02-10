from UI.transfer import Ui_TransferFrame
from general.util import make_api_post_request
from src.headers import headers

class TransferFrame(Ui_TransferFrame):
    def __init__(self, parent):
        Ui_TransferFrame.__init__(self)
        self.parent = parent

        self.pb_createtransfer.clicked.connect(self.create_transfer)

    def create_transfer(self):
        endpoint_url = "http://{}:{}/transfer/create_transfer/{}/{}/{}/{}".format("127.0.0.1", "8000", self.parent.current_account_id, self.le_uuid.text(), int(self.le_value.text()), self.le_description.text())
        make_api_post_request(endpoint_url, headers=headers)
        return 'Transfer created'
        # """Create transfer method"""
        # new_transfer = Transfer(self.parent.current_account_id, self.le_uuid.text(), int(self.le_value.text()), self.le_description.text())
        # self.transfer_model.create_transfer(new_transfer)
        # self.hide()
