"""This file contains the class for the recurring transactions popup window."""
from PyQt6.QtWidgets import QDialog
from UI.r_transactions import Ui_ReccuringTransactionForm
from general.util import split_into_list
from src.models import AccountModel

class RecurringForm(QDialog, Ui_ReccuringTransactionForm):
    """Recurring transactions popup class"""
    def __init__(self, transactions_window):
        super().__init__(transactions_window)
        self.setupUi(self, transactions_window)
        self.acc_window = transactions_window.acc_window
        self.account_model = AccountModel()

        element = self.account_model.get_name_of_acc(self.acc_window.current_user_id) # NAMES OF THE ACCOUNTS
        actual_element = split_into_list(element) # ACTUAL_ELEMENT
        self.cb_accounts.addItems(actual_element)
