"""Transfer Frame"""
from UI.transfer import Ui_TransferFrame
from general.util import make_api_post_request
from general.headers import headers, base_url


class TransferFrame(Ui_TransferFrame):
    """Transfer Frame"""
    def __init__(self, parent):
        Ui_TransferFrame.__init__(self)
        self.parent = parent
        self.pb_createtransfer.clicked.connect(self.create_transfer)

    def create_transfer(self):
        """Create a new transfer"""
        endpoint_url = f"{base_url}/transfer/create_transfer/{self.parent.current_account_id}/{self.le_uuid.text()}/{self.le_value.text()}/{self.le_description.text()}"
        make_api_post_request(endpoint_url, headers=headers)
        return 'Transfer created'
