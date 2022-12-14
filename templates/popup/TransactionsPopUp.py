from PyQt6.QtWidgets import QDialog
from UI.transactions import Ui_PopUpTransactions
from templates.Buttons import AddTransaction
from templates.popup.RTransactionsPopUp import RecurringForm
from templates.Util import Utility, splitIntoList

class TransactionPopup(QDialog, Ui_PopUpTransactions):

    def __init__(self, AccWindow):
        super().__init__(AccWindow)
        self.setupUi(self, AccWindow)
        self.AccWindow = AccWindow
        self.addTransactionButton = AddTransaction(self)
        self.utility = Utility(self)
        self.show()
        self.pb_addTransactions.clicked.connect(self.addTransactionButton.functionality)
        self.pb_CreateRecurringPopup.clicked.connect(self.CreateRPopup)

        element = self.utility.get_name_of_acc_transaction(self.AccWindow) # NAMES OF THE ACCOUNTS
        actual_element = splitIntoList(element) # ACTUAL_ELEMENT
        self.cb_accounts.addItems(actual_element)
        self.cb_typeoftacc.currentText()

    def CreateRPopup(self):
        self.hide()
        r_trans = RecurringForm(self)
        r_trans.show()

