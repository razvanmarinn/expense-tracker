"""This module contains the controller for the popup window for creating new accounts"""
from src.dtos.transactions_dto import TransactionDTO
from general.util import make_api_post_request, make_api_get_request
from src.headers import headers

class PopUpAccountsController():
    """This class contains the controller for the popup window for creating new accounts"""
    def __init__(self, view, acc_window):
        self.view = view
        self.acc_window = acc_window
        self.view.pb_add.clicked.connect(self.create_user_account)

    def create_user_account(self):
        """Create account method"""
        endpoint_url = "http://{}:{}/accounts/count_accounts/{}/".format("127.0.0.1", "8000", self.acc_window.user.id)
        user_data = make_api_get_request(endpoint_url, headers=headers)
        if user_data >= self.acc_window.max_accounts_per_user:
            print("max accs")
        else:
            endpoint_url = "http://{}:{}/accounts/create_account/{}/{}/{}".format("127.0.0.1", "8000", self.acc_window.user.id ,self.view.le_accountname.text(), self.view.le_budgetname.text())
            user_data = make_api_post_request(endpoint_url, headers=headers)
            self.acc_window.cb_dropdown.addItem(self.view.le_accountname.text())
            self.acc_window.cb_dropdown.update()
            self.view.hide()
