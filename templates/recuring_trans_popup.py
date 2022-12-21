from PyQt6.QtWidgets import QDialog
from UI.r_transactions import Ui_ReccuringTransactionForm
from templates.Util import Utility
from templates.Buttons import AddRecTransaction

class RecurringForm(QDialog, Ui_ReccuringTransactionForm):
    def __init__(self, TransactionsPopup):
        super().__init__(TransactionsPopup)
        self.setupUi(self, TransactionsPopup)
        self.Utility = Utility(self)
        self.AddRecTransactionButton = AddRecTransaction(self)
        self.AccWindow = TransactionsPopup.AccWindow
        
        element = self.Utility.getNameOfTheAccountsOfThisIdTrans(self.AccWindow) # NAMES OF THE ACCOUNTS
        actual_element = self.Utility.splitIntoList(element) # ACTUAL_ELEMENT
        self.cb_accounts.addItems(actual_element)
        self.pb_addRecuringTrans.clicked.connect(self.AddRecTransactionButton.functionality)
        