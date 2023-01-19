"""This module contains the class for the popup window to add a custom category to the combobox"""
from datetime import datetime
from PyQt6.QtWidgets import QDialog
from UI.popup import Ui_Form
from src.models import Account, AccountModel, Transaction, TransactionModel

class PopUpWindowAcc(QDialog, Ui_Form):

    def __init__(self, acc_window):
        super().__init__(acc_window)
        self.setupUi(self)
        self.show()
        self.acc_window = acc_window
        self.pb_add.clicked.connect(self.create_user_account)
        self.account_model = AccountModel()
        self.transaction_model = TransactionModel()


    def create_user_account(self):
        """Create account method"""
        no_of_acc = self.account_model.count_accounts(self.acc_window.current_user_id)
        if no_of_acc >= self.acc_window.max_accounts_per_user:
            print("max accs")
        else:
            new_account = Account(self.le_accountname.text(), int(self.le_budgetname.text()), self.acc_window.current_user_id)
            self.account_model.create_account(new_account)
            account_id = self.account_model.get_account_id(self.le_accountname.text(), self.acc_window.current_user_id)

            dt_string = datetime.now().strftime("%d/%m/%Y")
            new_transaction = Transaction('Initial transaction', int(self.le_budgetname.text()),dt_string, 'none', account_id, self.acc_window.current_user_id)
            self.transaction_model.create_transaction(new_transaction)

            self.acc_window.cb_dropdown.addItem(self.le_accountname.text())
            self.acc_window.cb_dropdown.update()
            self.hide()
