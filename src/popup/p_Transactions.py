"""Transactions controller"""
from PyQt6.QtWidgets import QDialog
from UI.transactions import Ui_PopUpTransactions
from controllers.transactions_controller import TransactionController

class TransactionPopup(QDialog, Ui_PopUpTransactions):
    """Transactions popup class"""
    def __init__(self, acc_window):
        super().__init__(acc_window)
        self.setupUi(self, acc_window)
        self.acc_window = acc_window
        self.category_list = ['Food', 'Bills', 'Entertainment', 'Transport', 'Other']
        self.transaction_model = TransactionController(self, self.acc_window)
        self.show()

        #self.pb_CreateRecurringPopup.clicked.connect(lambda: self.create_popup("recurring_trans"))
        for i in self.category_list:
            self.cb_typeoftacc.addItem(i)

        #add_drop_down_items(self.acc_window)
        self.cb_typeoftacc.currentText()


