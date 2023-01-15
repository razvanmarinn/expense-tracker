from PyQt6.QtWidgets import QDialog
from UI.popup import Ui_Form
from templates.Models import Account, AccountModel, Transaction, TransactionModel
from datetime import datetime

class PopUpWindowAcc(QDialog, Ui_Form):

    def __init__(self, accwindow):
        super().__init__(accwindow)
        self.setupUi(self)
        self.show()
        self.accwindow = accwindow
        self.loginform = self.accwindow.loginf
        self.pb_add.clicked.connect(self.create_user_account)
        self.account_model = AccountModel()
        self.transaction_model = TransactionModel()


    def create_user_account(self):
        """Create account method"""
        no_of_acc = self.account_model.count_accounts(self.accwindow.current_user_id)
        if no_of_acc >= self.accwindow.max_accounts_per_user:
            print("max accs")
        else:
            new_account = Account(self.le_accountname.text(), int(self.le_budgetname.text()), self.accwindow.current_user_id)
            self.account_model.create_account(new_account)
            account_id = self.account_model.get_account_id(self.le_accountname.text(), self.accwindow.current_user_id)

            dt_string = datetime.now().strftime("%d/%m/%Y")
            new_transaction = Transaction('Initial transaction', int(self.le_budgetname.text()),dt_string, 'none', account_id, self.accwindow.current_user_id)
            self.transaction_model.create_transaction(new_transaction)

            self.accwindow.cb_dropdown.addItem(self.le_accountname.text())
            self.accwindow.create_new()
            self.accwindow.cb_dropdown.update()
            self.hide()