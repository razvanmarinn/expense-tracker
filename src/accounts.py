"""Accounts form GUI functionality / Controller FOR ACCOUNTS """
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import QtWidgets
from UI.Accounts import Ui_AccountsForm
from src.graphs import GraphForm
from src.models import AccountModel, TransactionModel
from general.util import add_drop_down_items
from controllers.account_controller import AccountsController
from functools import partial


# class AccountsFormTab(QDialog, Ui_AccountsForm):
#     """Accounts form GUI functionality"""
#     def __init__(self, login_form, user):
#         super().__init__()
#         self.setupUi(self, login_form, user)
#         self.show()
#         self.user =user
#         self.login_form = login_form # LOGIN FORM PASSED TO GET INFO FROM IT
#         self.max_accounts_per_user = 3 # STATIC VARIABLE
#         self.current_user_id = user.id # CURRENT USER ID
#         self.current_account_id = 0 # CURRENT ACCOUNT ID
#         self.current_account_uuid = "" # CURRENT ACCOUNT IBAN
#         self.account_model = AccountModel()
#         self.transaction_model = TransactionModel()

#         self.current_nr_of_acc = self.account_model.count_accounts(user.id) # CURRENT NUMBER OF ACCOUNTS
#         #add items to dropdown box
#         add_drop_down_items(self)

#         self.pb_removeacc.clicked.connect(self.remove_account)
#         self.pb_addacc.clicked.connect(lambda : self.create_popup("acc"))
#         self.pb_logout.clicked.connect(self.logout)
#         self.pb_analyze.clicked.connect(lambda : self.create_popup("graph"))
#         if self.actual_element is not None:
#             self.pb_addtransaction.clicked.connect(lambda : self.create_popup("transaction"))
#         else:
#             print("No account to add transaction to")
#         self.pb_createtransfer.clicked.connect(lambda : self.create_popup("transfer"))
#         self.pb_accountinfo.clicked.connect(lambda : self.create_popup("accinfo"))
#         self.set_data() # SET DATA IN THE TABLE
#         self.cb_dropdown.currentIndexChanged.connect(self.set_data)




#     def set_data(self):
#         """Set data from database into accounts display table"""

#         curr_text = self.cb_dropdown.currentText() # CURRENT DROPDOWN TEXT
#         accid = self.account_model.get_account_id(curr_text, self.current_user_id)
#         self.current_account_id = accid
#         self.current_account_uuid = self.account_model.get_uuid(accid)
#         self.l_balance_value.setText(str(self.account_model.get_account_balance(accid)))
#         transactions = self.transaction_model.get_transaction_by_acc_id(accid)
#         self.tw_showinfo.setRowCount(len(transactions))

#         for row, transaction in enumerate(transactions):
#             id_tabel = QtWidgets.QTableWidgetItem(str(transaction[0]))
#             name_tabel = QtWidgets.QTableWidgetItem(transaction[1])
#             value_tabel = QtWidgets.QTableWidgetItem(str(transaction[2]))
#             type_tabel = QtWidgets.QTableWidgetItem(str(transaction[3]))
#             date_tabel = QtWidgets.QTableWidgetItem(str(transaction[4]))
#             self.tw_showinfo.setItem(row, 0, id_tabel)
#             self.tw_showinfo.setItem(row, 1, name_tabel)
#             self.tw_showinfo.setItem(row, 2, value_tabel)
#             self.tw_showinfo.setItem(row, 3, date_tabel)
#             self.tw_showinfo.setItem(row, 4, type_tabel)


#     def logout(self):
#         """Logout method"""
#         QApplication.exit()


#     def create_new(self):
#         """Create a new instance of this class"""
#         self.hide()
#         self.__init__(self.login_form, self.user)


#     def remove_account(self): ## TO BE LOOKED AT
#         """Remove account from GUI and database"""
#         if self.actual_element[0] == "":
#             raise NoAccountException("No account to remove")
#         else:
#             self.transaction_model.delete_transaction_by_acc_id(self.current_account_id)
#             self.account_model.delete_account(self.cb_dropdown.currentText(), self.current_user_id)
#             self.cb_dropdown.removeItem(self.cb_dropdown.currentIndex())
#             #self.actual_element.remove(self.cb_dropdown.currentText())
#     def create_popup(self, popup_type):
#         pop = None
#         if popup_type == "acc":
#             pop = PopUpWindowAcc(self)
#         if popup_type == "transfer":
#             pop = TransferPopup(self)
#         if popup_type == "graph":
#             pop = GraphForm(self)
#         if popup_type == "transaction":
#             pop = TransactionPopup(self)
#         if popup_type == "accinfo":
#             pop = AccountInfoPopup(self)

#         if pop:
#             pop.show()



class AccountsFormTab(QDialog, Ui_AccountsForm):
    """Accounts form GUI functionality"""
    def __init__(self, login_form, user):
        super().__init__()
        self.setupUi(self, login_form, user)
        self.show()
        self.user =user
        self.login_form = login_form
        self.max_accounts_per_user = 3 # STATIC VARIABLE
        self.current_user_id = user.id # CURRENT USER ID
        self.account_model = AccountModel()
        self.current_nr_of_acc = self.account_model.count_accounts(user.id)

        add_drop_down_items(self)

        self.controller = AccountsController(self)
        self.pb_logout.clicked.connect(self.exit)
        self.account_dto = self.controller.get_account_data(self.controller.get_current_account_id())
        #self.cb_dropdown.currentIndexChanged.connect(partial(self.set_data, self.account_dto))
        self.cb_dropdown.currentIndexChanged.connect(self.set_data)

        self.set_data()

    def exit(self):
        """Logout method"""
        QApplication.exit()

    def create_new(self):
        """Create a new instance of this class"""
        self.hide()
        self.__init__(self.login_form, self.user)

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