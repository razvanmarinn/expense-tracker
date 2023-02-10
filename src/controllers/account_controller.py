"""Account Controller"""
from src.views.popup.p_accounts import PopUpWindowAcc
from src.views.popup.p_account_info import AccountInfoPopup
from src.dtos.accounts_dto import AccountDTO
from general.util import make_api_get_request, make_api_delete_request
from src.controllers.transactions_controller import TransactionController
from src.headers import headers


class AccountsController():
    """Account controller class"""
    def __init__(self, view):
        self.view = view

    def get_account_data(self, account_id):
        """Get account data"""
        endpoint_url = "http://{}:{}/accounts/get_account_by_id/{}".format("127.0.0.1", "8000", account_id)
        user_data = make_api_get_request(endpoint_url, headers=headers)
        if "detail" in user_data:
            return None
        else:
            transactions = self.get_transactions(account_id)
            return AccountDTO(user_data["id"], user_data["uuid"], user_data["balance"], transactions)

    def get_transactions(self, account_id):
        """Get all transactions for a specific account"""
        endpoint_url = "http://{}:{}/transactions/get_transactions/{}".format("127.0.0.1", "8000", account_id)
        return make_api_get_request(endpoint_url, headers=headers)


    def remove_account(self):
        """Remove an account"""
        transaction_controller = TransactionController(self.view, self)
        transaction_controller.delete_transaction_by_acc_id(self.view.account_dto.account_id)
        endpoint_url = "http://{}:{}/accounts/delete_account/{}/{}".format("127.0.0.1", "8000", self.view.cb_dropdown.currentText(), self.view.user.id)
        make_api_delete_request(endpoint_url, headers=headers)
        self.view.cb_dropdown.removeItem(self.view.cb_dropdown.currentIndex())

    def get_current_account_id(self):# modify into api one
        """Get the current account id"""
        curr_text = self.view.cb_dropdown.currentText() # CURRENT DROPDOWN TEXT
        endpoint_url = "http://{}:{}/accounts/get_account_id/{}/{}".format("127.0.0.1", "8000", curr_text, self.view.user.id)
        user_data = make_api_get_request(endpoint_url, headers=headers)
        return user_data

    def create_account_poup(self):
        """Create a new account popup"""
        self.view.popup = PopUpWindowAcc(self.view)

    def create_account_info_popup(self):
        """Create a new account info popup"""
        self.view.popup = AccountInfoPopup(self.view)

    @staticmethod
    def total_balance_of_a_user(user_id):
        """Get total balance of a user"""
        endpoint_url = "http://{}:{}/users/get_total_balance/{}".format("127.0.0.1", "8000", user_id)
        user_data = make_api_get_request(endpoint_url, headers=headers)
        return user_data

    @staticmethod
    def get_monthly_spendings(user_id, month, year):
        """Get monthly spendings"""
        endpoint_url = "http://{}:{}/users/get_spending_by_month/{}/{}/{}".format("127.0.0.1", "8000", user_id, month, year)
        user_data = make_api_get_request(endpoint_url, headers=headers)
        return user_data