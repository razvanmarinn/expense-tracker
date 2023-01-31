"""This module contains the controller for the transactions window"""
from datetime import datetime
from src.models import TransactionModel , AccountModel, Transaction
from general.util import check_for_minus_or_plus, make_api_get_request
from src.dtos.transactions_dto import TransactionDTO

headers = {
    "Authorization": "Bearer " + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozLCJleHAiOjE2NzUyNjMwODAuNTY0NjM2Mn0.0GHX71PwEcdyZvx-IoBu_5VhJBsSOVd5hZo-Qf7rmgo}"
}


class TransactionController():
    """This class contains the controller for the transactions window"""
    def __init__(self, view, acc_window):
        self.view = view
        self.acc_window = acc_window
        self.account_model = AccountModel()
        self.transaction_model = TransactionModel()
        

    def create_transaction(self):
        """This function creates a new transaction"""
        new_transaction = self.create_new_transaction()
        self.transaction_model.create_transaction(new_transaction)
        self.update_account_balance(new_transaction)
        self.view.hide()
        self.acc_window.accounts_form.set_data()


    def create_new_transaction(self):
        """This function creates a new transaction"""
        time = datetime.now()
        dt_string = time.strftime("%d/%m/%Y")

        sign = check_for_minus_or_plus(self.view.le_value.text())
        value = float(self.view.le_value.text())
        if sign == "-":
            value =  - (-1 * float(self.view.le_value.text()))


        new_transaction = Transaction(self.view.le_nume.text(), value, dt_string, self.view.cb_typeoftacc.currentText(),  self.acc_window.account_dto.account_id, self.acc_window.user.id)

        transaction_dto = TransactionDTO(new_transaction)
        return transaction_dto

    def update_account_balance(self, new_transaction):
        """This function updates the account balance with the new transaction"""
        self.acc_window.account_dto.balance += new_transaction.value
        self.acc_window.account_dto.transactions.append(new_transaction)
        self.account_model.set_new_balance(self.acc_window.account_dto.balance, self.acc_window.account_dto.account_id)



    def delete_transaction_by_acc_id(self, account_id):
        """This function deletes a transaction"""
        endpoint_url = "http://{}:{}/transactions/delete_transactions_by_acc_id/{}".format("127.0.0.1", "8000", account_id)
        make_api_get_request(endpoint_url, headers)
        return True