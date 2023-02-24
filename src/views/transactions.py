"""Transactions Frame"""
from UI.transactions import Ui_TransactionFrame
from src.controllers.transactions_controller import TransactionController


class TransactionsFrame(Ui_TransactionFrame):
    """Transaction Frame"""

    category_list = ['Food', 'Bills', 'Entertainment', 'Transport', 'Other']

    def __init__(self, parent, refresher):
        Ui_TransactionFrame.__init__(self, parent)
        self.parent = parent
        self.transaction_controller = TransactionController(self, refresher)
        self.show()

        self.pb_addtransaction.clicked.connect(self.transaction_controller.create_transaction)

        for i in self.category_list:
            self.cb_typeoftacc.addItem(i)
        self.cb_typeoftacc.currentText()
