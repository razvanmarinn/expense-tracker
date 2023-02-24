"""This module contains the controller for the transactions window"""
from general.util import make_api_get_request, make_api_post_request
from general.headers import headers, base_url


class TransactionController():
    """This class contains the controller for the transactions window"""
    def __init__(self, view, refresher):
        self.view = view
        self.refresher = refresher

    def create_transaction(self):
        """This function creates a transaction"""
        endpoint_url = f"{base_url}/transactions/create_transaction/{self.view.le_nume.text()}/{self.view.le_value.text()}/{self.view.cb_typeoftacc.currentText()}/{self.view.parent.account_dto.account_id }"
        user_data = make_api_post_request(endpoint_url, headers)
        self.refresher.refresh()
        return user_data

    @staticmethod
    def delete_transaction_by_acc_id(account_id):
        """This function deletes a transaction"""
        endpoint_url = f"{base_url}/transactions/delete_transactions_by_acc_id/{account_id}"
        make_api_get_request(endpoint_url, headers)
        return True
