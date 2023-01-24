"""Accounts form GUI functionality / Controller FOR ACCOUNTS """
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import QtWidgets
from UI.Accounts import Ui_AccountsForm
from src.models import AccountModel
from general.util import add_drop_down_items
from controllers.account_controller import AccountsController

class AccountsFormTab(QDialog, Ui_AccountsForm):
    """Accounts form GUI functionality"""
    def __init__(self, login_form, user):
        super().__init__()
        self.setupUi(self, login_form, user)
        self.show()
        self.user = user
        self.login_form = login_form
        self.max_accounts_per_user = 3 # STATIC VARIABLE
        self.account_model = AccountModel()
        self.current_nr_of_acc = self.account_model.count_accounts(user.id)
        add_drop_down_items(self)
        self.controller = AccountsController(self)
        self.account_dto = self.controller.get_account_data(self.controller.get_current_account_id())
        #self.cb_dropdown.currentIndexChanged.connect(partial(self.set_data, self.account_dto))
        self.cb_dropdown.currentIndexChanged.connect(self.set_data)
        self.pb_logout.clicked.connect(self.exit)
        #self.pb_createtransfer.clicked.connect(self.controller.create_transfer_popup)
        self.pb_createtransfer.clicked.connect(self.controller.create_transfer_popup)
        self.set_data()

    def exit(self):
        """Logout method"""
        QApplication.exit()

    def set_data(self):
        """Set data from database into accounts display table"""
        acc_id = self.controller.get_current_account_id()
        self.account_dto = self.controller.get_account_data(acc_id)
        if acc_id  is not None:
           # self.controller.get_current_account_uuid(self.account_dto.account_id)
            self.l_balance_value.setText(str(self.account_dto.balance))
            #transactions = self.transaction_model.get_transaction_by_acc_id(self.current_account_id)
            self.tw_showinfo.setRowCount(len(self.account_dto.transactions))

            for row, transaction in enumerate(self.account_dto.transactions):
                id_tabel = QtWidgets.QTableWidgetItem(str(transaction[0]))
                name_tabel = QtWidgets.QTableWidgetItem(transaction[1])
                value_tabel = QtWidgets.QTableWidgetItem(str(transaction[2]))
                type_tabel = QtWidgets.QTableWidgetItem(str(transaction[3]))
                date_tabel = QtWidgets.QTableWidgetItem(str(transaction[4]))
                self.tw_showinfo.setItem(row, 0, id_tabel)
                self.tw_showinfo.setItem(row, 1, name_tabel)
                self.tw_showinfo.setItem(row, 2, value_tabel)
                self.tw_showinfo.setItem(row, 3, date_tabel)
                self.tw_showinfo.setItem(row, 4, type_tabel)
