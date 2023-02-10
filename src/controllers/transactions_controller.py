"""This module contains the controller for the transactions window"""
from general.util import  make_api_get_request, make_api_post_request
from src.headers import headers


class TransactionController():
    """This class contains the controller for the transactions window"""
    def __init__(self, view, account_frame):
        self.view = view
        self.account_frame = account_frame


    def create_transaction(self):
        endpoint_url = "http://{}:{}/transactions/create_transaction/{}/{}/{}/{}".format("127.0.0.1", "8000", self.view.le_nume.text(), self.view.le_value.text(), self.view.cb_typeoftacc.currentText(), self.view.parent.account_dto.account_id )
        user_data = make_api_post_request(endpoint_url, headers)
        self.account_frame.set_data()
        return user_data


    def delete_transaction_by_acc_id(self, account_id):
        """This function deletes a transaction"""
        endpoint_url = "http://{}:{}/transactions/delete_transactions_by_acc_id/{}".format("127.0.0.1", "8000", account_id)
        make_api_get_request(endpoint_url, headers)
        return True
    