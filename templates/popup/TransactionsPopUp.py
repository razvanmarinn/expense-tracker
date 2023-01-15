from PyQt6.QtWidgets import QDialog
from UI.transactions import Ui_PopUpTransactions
from templates.Buttons import AddTransaction
from templates.popup.RTransactionsPopUp import RecurringForm
from templates.Util import check_for_minus_or_plus, splitIntoList
from templates.Models import TransactionModel , AccountModel, Transaction
from datetime import datetime

class TransactionPopup(QDialog, Ui_PopUpTransactions):

    def __init__(self, AccWindow):
        super().__init__(AccWindow)
        self.setupUi(self, AccWindow)
        self.AccWindow = AccWindow
        self.addTransactionButton = AddTransaction(self)
        self.transaction_model = TransactionModel()
        self.account_model = AccountModel()

        self.show()
        self.pb_addTransactions.clicked.connect(self.create_transaction)
        # self.pb_CreateRecurringPopup.clicked.connect(self.CreateRPopup)

        element = self.account_model.get_name_of_acc(self.AccWindow.current_user_id) # NAMES OF THE ACCOUNTS
        actual_element = splitIntoList(element) # ACTUAL_ELEMENT
        self.cb_accounts.addItems(actual_element)
        self.cb_typeoftacc.currentText()

#  element = self.account_model.get_name_of_acc(user.id) # NAMES OF THE ACCOUNTS
#         self.actual_element = splitIntoList(element) # ACTUAL_ELEMENT
#         if self.actual_element is not None:
#             self.cb_dropdown.addItems(self.actual_element)






    def CreateRPopup(self):
        self.hide()
        r_trans = RecurringForm(self)
        r_trans.show()

    def create_transaction(self):
        account_id = self.account_model.get_account_id(self.cb_accounts.currentText(), self.AccWindow.current_user_id)

        time = datetime.now()
        dt_string = time.strftime("%d/%m/%Y")
        print(dt_string)


        acc_balance = self.account_model.get_account_balance(account_id)

        sign = check_for_minus_or_plus(self.le_value.text())
        if sign == "-":
            acc_balance = acc_balance - (-1 * float(self.le_value.text()))
        else:
            acc_balance = acc_balance + float(self.le_value.text())
        new_transaction = Transaction(self.le_nume.text(), float(self.le_value.text()), dt_string, self.cb_typeoftacc.currentText(), account_id, self.AccWindow.current_user_id)
        self.transaction_model.create_transaction(new_transaction)
        self.account_model.set_new_balance(acc_balance,account_id)
        self.AccWindow.create_new()
        self.hide()