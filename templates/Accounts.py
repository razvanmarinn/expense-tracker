from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import QtWidgets
from UI.Accounts import Ui_AccountsForm
from templates.popup.TransactionsPopUp import TransactionPopup
from templates.popup.transferpopup import TransferPopup
from templates.popup.AccountPopUp import PopUpWindowAcc
from templates.Util import Utility, splitIntoList
from templates.Models import AccountModel, TransactionModel
from templates.Graphs import GraphForm
import sqlite3

class AccountsFormTab(QDialog, Ui_AccountsForm):
    """Accounts form GUI functionality"""
    def __init__(self, login_form, user):
        super().__init__()
        self.setupUi(self, login_form, user)
        self.show()
        self.user =user
        self.loginf = login_form # LOGIN FORM PASSED TO GET INFO FROM IT
        self.max_accounts_per_user = 3 # STATIC VARIABLE
        self.current_user_id = user.id # CURRENT USER ID
        self.current_account_id = 0 # CURRENT ACCOUNT ID

        self.account_model = AccountModel()
        self.transaction_model = TransactionModel()

        self.current_nr_of_acc = self.account_model.count_accounts(user.id) # CURRENT NUMBER OF ACCOUNTS
        #add items to dropdown box

        element = self.account_model.get_name_of_acc(user.id) # NAMES OF THE ACCOUNTS
        self.actual_element = splitIntoList(element) # ACTUAL_ELEMENT
        if self.actual_element is not None:
            self.cb_dropdown.addItems(self.actual_element)

        self.pb_addacc.clicked.connect(self.create_popup)
        self.pb_removeacc.clicked.connect(self.remove_account)
        self.pb_logout.clicked.connect(self.logout)
        self.pb_analyze.clicked.connect(self.create_graph_popup)
        self.pb_addtransaction.clicked.connect(self.create_transaction_popup)
        self.pb_createtransfer.clicked.connect(self.create_transfer_popup)

        self.set_data() # SET DATA IN THE TABLE
        self.cb_dropdown.currentIndexChanged.connect(self.set_data)




    def set_data(self):
        """Set data from database into accounts display table"""

        curr_text = self.cb_dropdown.currentText() # CURRENT DROPDOWN TEXT
        accid = self.account_model.get_account_id(curr_text, self.current_user_id)

        self.current_account_id = accid
        if accid is None:
            return 0
        self.l_balance_value.setText(str(self.account_model.get_account_balance(accid)))
        temp2 = self.transaction_model.get_transaction_by_acc_id(accid)

        list_of_transactions = []

        if temp2 is not None:
            list_of_transactions.extend(iter(temp2))

        if list_of_transactions is not None:
            id = []
            name = []
            value = []
            type = []
            date = []
            for list_of_transaction in list_of_transactions:
                id.append(list_of_transaction[0])
                name.append(list_of_transaction[1])
                value.append(list_of_transaction[2])
                type.append(list_of_transaction[3])
                date.append(list_of_transaction[4])


            self.tw_showinfo.setRowCount(len(list_of_transactions))

            for row, j in enumerate(range(len(id))):
                id_tabel = QtWidgets.QTableWidgetItem(str(id[j]))
                name_tabel = QtWidgets.QTableWidgetItem(str(name[j]))
                value_tabel = QtWidgets.QTableWidgetItem(str(value[j]))
                type_tabel = QtWidgets.QTableWidgetItem(str(type[j]))
                date_tabel = QtWidgets.QTableWidgetItem(str(date[j]))
                self.tw_showinfo.setItem(row, 0, id_tabel)
                self.tw_showinfo.setItem(row, 1, name_tabel)
                self.tw_showinfo.setItem(row, 2, value_tabel)
                self.tw_showinfo.setItem(row, 3, date_tabel)
                self.tw_showinfo.setItem(row, 4, type_tabel)



    def create_transaction_popup(self):
        """Create transaction popup"""
        if self.actual_element[0] == "":
            print("No accounts on this user")
        else:
            transaction = TransactionPopup(self)
            transaction.show()



    def create_popup(self):
        """Create popup window form"""
        pop = PopUpWindowAcc(self)
        pop.show()

    def create_transfer_popup(self):
        """Create popup window form"""
        pop = TransferPopup(self)
        pop.show()

    def create_graph_popup(self):
        """Create graph popup"""
        graph = GraphForm(self)
        graph.show()


    def logout(self):
        """Logout method"""
        QApplication.exit()


    def create_new(self):
        """Create a new instance of this class"""
        self.hide()
        self.__init__(self.loginf, self.user)




    def remove_account(self):
        if self.actual_element[0] == "":
            print("No accounts to be removed")
        else:
            self.transaction_model.delete_transaction_by_acc_id(self.current_account_id)
            self.account_model.delete_account(self.cb_dropdown.currentText(), self.current_user_id)
            self.cb_dropdown.removeItem(self.cb_dropdown.currentIndex())
            # self.create_new()

