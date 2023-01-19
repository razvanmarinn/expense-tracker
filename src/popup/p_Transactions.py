"""Transactions controller"""
from datetime import datetime
from PyQt6.QtWidgets import QDialog
from UI.transactions import Ui_PopUpTransactions
from src.popup.p_recurring_transactions import RecurringForm
from src.models import TransactionModel , AccountModel, Transaction
from src.popup.p_custom_category import PopUpAddCategory
from general.util import check_for_minus_or_plus, split_into_list

class TransactionPopup(QDialog, Ui_PopUpTransactions):
    """Transactions popup class"""
    def __init__(self, acc_window):
        super().__init__(acc_window)
        self.setupUi(self, acc_window)
        self.acc_window = acc_window
        self.category_list = ['Food', 'Bills', 'Entertainment', 'Transport', 'Other']
        self.transaction_model = TransactionModel()
        self.account_model = AccountModel()

        self.show()
        self.pb_addTransactions.clicked.connect(self.create_transaction)
        #self.pb_CreateRecurringPopup.clicked.connect(lambda: self.create_popup("recurring_trans"))
        for i in self.category_list:
            self.cb_typeoftacc.addItem(i)

        element = self.account_model.get_name_of_acc(self.acc_window.current_user_id) # NAMES OF THE ACCOUNTS
        actual_element = split_into_list(element) # ACTUAL_ELEMENT
        self.cb_accounts.addItems(actual_element)
        self.cb_typeoftacc.currentText()
        self.pb_add_type_of_category.clicked.connect(lambda: self.create_popup("add_categ"))

#  element = self.account_model.get_name_of_acc(user.id) # NAMES OF THE ACCOUNTS
#         self.actual_element = splitIntoList(element) # ACTUAL_ELEMENT
#         if self.actual_element is not None:
#             self.cb_dropdown.addItems(self.actual_element)


    def create_transaction(self):
        """This function creates a new transaction"""
        account_id = self.account_model.get_account_id(self.cb_accounts.currentText(), self.acc_window.current_user_id)

        time = datetime.now()
        dt_string = time.strftime("%d/%m/%Y")
        print(dt_string)
        acc_balance = self.account_model.get_account_balance(account_id)
        # try:
        #     asd = float(self.le_value.text())

        # except ValueError:
        #     print("Value error")
        #     return
        sign = check_for_minus_or_plus(self.le_value.text())
        if sign == "-":
            acc_balance = acc_balance - (-1 * float(self.le_value.text()))
        else:
            acc_balance = acc_balance + float(self.le_value.text())


        new_transaction = Transaction(self.le_nume.text(), float(self.le_value.text()), dt_string, self.cb_typeoftacc.currentText(), account_id, self.acc_window.current_user_id)
        self.transaction_model.create_transaction(new_transaction)
        self.account_model.set_new_balance(acc_balance,account_id)
        self.acc_window.create_new()
        self.hide()

    def create_popup(self, popup_type):
        """This function creates a new popup window"""
        pop = None
        if popup_type == "add_categ":
            pop = PopUpAddCategory(self)
        if popup_type == "recurring_transfer":
            pop = RecurringForm(self)
        if pop:
            pop.show()
