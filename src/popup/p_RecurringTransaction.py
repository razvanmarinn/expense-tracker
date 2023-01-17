from PyQt6.QtWidgets import QDialog
from UI.r_transactions import Ui_ReccuringTransactionForm
from general.util import splitIntoList
from src.m_Models import AccountModel

class RecurringForm(QDialog, Ui_ReccuringTransactionForm):
    def __init__(self, TransactionsPopup):
        super().__init__(TransactionsPopup)
        self.setupUi(self, TransactionsPopup)
        self.AccWindow = TransactionsPopup.AccWindow
        self.account_model = AccountModel()

        element = self.account_model.get_name_of_acc(self.AccWindow.current_user_id) # NAMES OF THE ACCOUNTS
        actual_element = splitIntoList(element) # ACTUAL_ELEMENT
        self.cb_accounts.addItems(actual_element)
