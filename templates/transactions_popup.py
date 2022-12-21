from PyQt6.QtWidgets import QDialog
from UI.transactions import Ui_PopUpTransactions
from templates.Buttons import AddTransaction
from templates.recuring_trans_popup import RecurringForm
from templates.Util import Utility

class TransactionPopup(QDialog, Ui_PopUpTransactions):

    def __init__(self, AccWindow):
        super().__init__(AccWindow)
        self.setupUi(self, AccWindow)
        self.AccWindow = AccWindow
        self.addTransactionButton = AddTransaction(self)
        self.Utility = Utility(self)
        self.show()
        self.pb_addTransactions.clicked.connect(self.addTransactionButton.functionality)
        self.pb_CreateRecurringPopup.clicked.connect(self.CreateRPopup)

        element = self.Utility.getNameOfTheAccountsOfThisIdTrans(self.AccWindow) # NAMES OF THE ACCOUNTS
        actual_element = self.Utility.splitIntoList(element) # ACTUAL_ELEMENT
        self.cb_accounts.addItems(actual_element)
        

    def CreateRPopup(self):
        self.hide()
        r_trans = RecurringForm(self)
        r_trans.show()

