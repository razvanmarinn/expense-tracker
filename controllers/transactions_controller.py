from src.popup.p_recurring_transactions import RecurringForm
from src.models import TransactionModel , AccountModel, Transaction
from src.popup.p_custom_category import PopUpAddCategory
from datetime import datetime
from general.util import check_for_minus_or_plus
from dtos.transactions_dto import TransactionDTO

class TransactionController():
    def __init__(self, view, acc_window):
        self.view = view
        self.acc_window = acc_window
        self.account_model = AccountModel()
        self.transaction_model = TransactionModel()
        self.view.pb_addTransactions.clicked.connect(self.create_transaction)
        self.view.pb_add_type_of_category.clicked.connect(self.create_popup_add_category)

    def create_popup_recurring(self):
        pop = RecurringForm(self)
        pop.show()

    def create_popup_add_category(self):
        pop = PopUpAddCategory(self)
        pop.show()

    def create_transaction(self):
        """This function creates a new transaction"""
        new_transaction = self.create_new_transaction()
        self.transaction_model.create_transaction(new_transaction)
        self.update_account_balance(new_transaction)
        self.acc_window.create_new()
        self.view.hide()

    def create_new_transaction(self):
        """This function creates a new transaction"""
        time = datetime.now()
        dt_string = time.strftime("%d/%m/%Y")

        sign = check_for_minus_or_plus(self.view.le_value.text())
        value = float(self.view.le_value.text())
        if sign == "-":
            value =  - (-1 * float(self.view.le_value.text()))


        new_transaction = Transaction(self.view.le_nume.text(), value, dt_string, self.view.cb_typeoftacc.currentText(),  self.acc_window.account_dto.account_id, self.acc_window.current_user_id)

        transaction_dto = TransactionDTO(new_transaction)
        return transaction_dto

    def update_account_balance(self, new_transaction):
        """This function updates the account balance with the new transaction"""
        self.acc_window.account_dto.balance += new_transaction.value
        self.acc_window.account_dto.transactions.append(new_transaction)
        self.account_model.set_new_balance(self.acc_window.account_dto.balance, self.acc_window.account_dto.account_id)

