from datetime import datetime
from src.models import Account, AccountModel, Transaction, TransactionModel
from dtos.transactions_dto import TransactionDTO

class PopUpAccountsController():
    def __init__(self, view, acc_window):
        self.view = view
        self.acc_window = acc_window
        self.view.pb_add.clicked.connect(self.create_user_account)
        self.account_model = AccountModel()
        self.transaction_model = TransactionModel()

    def create_user_account(self):
        """Create account method"""
        no_of_acc = self.account_model.count_accounts(self.acc_window.current_user_id)
        if no_of_acc >= self.acc_window.max_accounts_per_user:
            print("max accs")
        else:
            acc_id = self.create_new_account()
            self.create_inital_transaction(acc_id)
            self.acc_window.cb_dropdown.addItem(self.view.le_accountname.text())
            self.acc_window.cb_dropdown.update()
            self.view.hide()

    def create_new_account(self):
        """This function creates a new account"""
        new_account = Account(self.view.le_accountname.text(), int(self.view.le_budgetname.text()), self.acc_window.current_user_id)
        self.account_model.create_account(new_account)
        account_id = self.account_model.get_account_id(self.view.le_accountname.text(), self.acc_window.current_user_id)
        return account_id

    def create_inital_transaction(self, account_id):
        dt_string = datetime.now().strftime("%d/%m/%Y")
        new_transaction = Transaction('Initial transaction', int(self.view.le_budgetname.text()),dt_string, 'none', account_id, self.acc_window.current_user_id)
        transaction_dto = TransactionDTO(new_transaction)
        self.transaction_model.create_transaction(transaction_dto)
        return transaction_dto