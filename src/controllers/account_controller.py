"""Account Controller"""
from src.views.popup.p_accounts import PopUpWindowAcc
from src.views.popup.p_account_info import AccountInfoPopup
from src.dtos.accounts_dto import AccountDTO
from src.controllers.transactions_controller import TransactionController
from general.util import make_api_get_request, make_api_delete_request
from general.headers import headers, base_url
from general.export import Exporter


class AccountsController():
    """Account controller class"""
    def __init__(self, view, main_page, refresher):
        self.view = view
        self.main_page = main_page
        self.refresher = refresher

    def get_account_data(self, account_id):
        """Get account data"""
        endpoint_url = f"{base_url}/accounts/get_account_by_id/{account_id}"
        user_data = make_api_get_request(endpoint_url, headers=headers)
        if "detail" in user_data:
            return None
        transactions = self.get_transactions(account_id)
        return AccountDTO(user_data["name"], user_data["id"], user_data["uuid"], user_data["balance"], transactions)

    def get_transactions(self, account_id):
        """Get all transactions for a specific account"""
        endpoint_url = f"{base_url}/transactions/get_transactions/{account_id}"
        return make_api_get_request(endpoint_url, headers=headers)

    def remove_account(self):
        """Remove an account"""
        TransactionController.delete_transaction_by_acc_id(self.view.account_dto.account_id)
        endpoint_url = f"{base_url}/accounts/delete_account/{self.view.cb_dropdown.currentText()}/{self.view.user.id}"
        make_api_delete_request(endpoint_url, headers=headers)
        self.refresher.refresh()  # refresh the info when an account is deleted
        self.view.cb_dropdown.removeItem(self.view.cb_dropdown.currentIndex())

    def get_current_account_id(self):
        """Get the current account id"""
        curr_text = self.view.cb_dropdown.currentText()
        endpoint_url = f"{base_url}/accounts/get_account_id/{curr_text}/{self.view.user.id}"
        user_data = make_api_get_request(endpoint_url, headers=headers)
        return user_data

    def create_account_poup(self):
        """Create a new account popup"""
        self.view.popup = PopUpWindowAcc(self.view)

    def create_account_info_popup(self):
        """Create a new account info popup"""
        self.view.popup = AccountInfoPopup(self.view)

    def export_file(self, exporter: Exporter, path):
        """Export to pdf"""
        exporter.create(self.view.account_dto, path)

    @staticmethod
    def total_balance_of_a_user(user_id):
        """Get total balance of a user"""
        endpoint_url = f"{base_url}/users/get_total_balance/{user_id}"
        user_data = make_api_get_request(endpoint_url, headers=headers)
        return user_data

    @staticmethod
    def get_monthly_spendings(user_id, month, year):
        """Get monthly spendings"""
        endpoint_url = f"{base_url}/users/get_spending_by_month/{user_id}/{month}/{year}"
        user_data = make_api_get_request(endpoint_url, headers=headers)
        return user_data

    @staticmethod
    def get_details_of_user(user_id):
        """Get details of a user"""
        endpoint_url = f"{base_url}/user/get_user_details/{user_id}"
        user_data = make_api_get_request(endpoint_url, headers=headers)
        return user_data
