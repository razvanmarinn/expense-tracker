"""This module contains the controller for the transactions window"""
from general.util import make_api_get_request, make_api_post_request
from general.headers import headers, base_url


class TransactionController():
    """This class contains the controller for the transactions window"""
    def __init__(self, view, account_frame, main_page):
        self.view = view
        self.account_frame = account_frame
        self.main_page = main_page

    def create_transaction(self):
        """This function creates a transaction"""
        endpoint_url = f"{base_url}/transactions/create_transaction/{self.view.le_nume.text()}/{self.view.le_value.text()}/{self.view.cb_typeoftacc.currentText()}/{self.view.parent.account_dto.account_id }"
        user_data = make_api_post_request(endpoint_url, headers)
        self.refresh_transactions()
        return user_data

    def delete_transaction_by_acc_id(self, account_id):
        """This function deletes a transaction"""
        endpoint_url = f"{base_url}/transactions/delete_transactions_by_acc_id/{account_id}"
        make_api_get_request(endpoint_url, headers)
        return True

    def refresh_transactions(self):
        """This function refreshes the transactions"""
        self.account_frame.set_data()
        self.main_page.get_total_balance()
        self.main_page.get_this_month_spending()
