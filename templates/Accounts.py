from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import QtWidgets
from UI.Accounts import Ui_AccountsForm
from templates.popup.TransactionsPopUp import TransactionPopup
from templates.popup.AccountPopUp import PopUpWindowAcc
from templates.Buttons import RemoveAccButton
from templates.Util import Utility, splitIntoList
from templates.Graphs import GraphForm
import sqlite3

class AccountsFormTab(QDialog, Ui_AccountsForm):
    """Accounts form GUI functionality"""
    def __init__(self, login_form, user):
        super().__init__()
        self.setupUi(self, login_form, user)
        self.show()
        self.loginf = login_form # LOGIN FORM PASSED TO GET INFO FROM IT
        self.max_accounts_per_user = 3 # STATIC VARIABLE
        self.current_acc_id = user.id # CURRENT USER ID
        self.remove_button = RemoveAccButton(self)
        self.utility = Utility(self)
        self.current_account_id = 0 # CURRENT ACCOUNT ID


        self.current_nr_of_acc = self.utility.countCurrentNrOfAcs()
        #add items to dropdown box
        element = self.utility.get_name_of_acc() # NAMES OF THE ACCOUNTS
        self.actual_element = splitIntoList(element) # ACTUAL_ELEMENT
        self.cb_dropdown.addItems(self.actual_element)

        self.pb_addacc.clicked.connect(self.create_popup)
        self.pb_removeacc.clicked.connect(self.remove_button.functionality)
        self.pb_logout.clicked.connect(self.logout)
        self.pb_analyze.clicked.connect(self.create_graph_popup)
        self.pb_addtransaction.clicked.connect(self.create_transaction_popup)
        self.set_data() # SET DATA IN THE TABLE
        self.cb_dropdown.currentIndexChanged.connect(self.set_data)


    def set_data(self):
        """Set data from database into accounts display table"""
        db = sqlite3.connect("expense_tracker.db")
        db_cursor= db.cursor()
        curr_text = self.cb_dropdown.currentText() # CURRENT DROPDOWN TEXT

        db_cursor.execute("SELECT accounts_id from accounts_test WHERE name = :name AND userid = :userid",
        {'name': curr_text , 'userid': self.current_acc_id})
        temp = db_cursor.fetchone()
        accid = ""
        if temp is not None:
            for i in temp:
                accid +=str(i)

            accid = int(accid)
        self.current_account_id = accid
        db_cursor.execute("SELECT * from transactions WHERE account_id = :accid" , {'accid': accid})
        temp2 = db_cursor.fetchall()

        list_of_transactions = []

        if temp2 is not None:
            list_of_transactions.extend(iter(temp2))
        if list_of_transactions is not None:
            id = []
            name = []
            value = []
            budget = []
            type = []
            date = []
            for list_of_transaction in list_of_transactions:
                id.append(list_of_transaction[0])
                name.append(list_of_transaction[1])
                value.append(list_of_transaction[2])
                budget.append(list_of_transaction[3])
                type.append(list_of_transaction[4])
                date.append(list_of_transaction[5])


            self.tw_showinfo.setRowCount(len(list_of_transactions))

            for row, j in enumerate(range(len(id))):
                id_tabel = QtWidgets.QTableWidgetItem(str(id[j]))
                name_tabel = QtWidgets.QTableWidgetItem(str(name[j]))
                value_tabel = QtWidgets.QTableWidgetItem(str(value[j]))
                budget_tabel = QtWidgets.QTableWidgetItem(str(budget[j]))
                type_tabel = QtWidgets.QTableWidgetItem(str(type[j]))
                date_tabel = QtWidgets.QTableWidgetItem(str(date[j]))
                self.tw_showinfo.setItem(row, 0, id_tabel)
                self.tw_showinfo.setItem(row, 2, budget_tabel)
                self.tw_showinfo.setItem(row, 1, name_tabel)
                self.tw_showinfo.setItem(row, 3, value_tabel)
                self.tw_showinfo.setItem(row, 5, type_tabel)
                self.tw_showinfo.setItem(row, 4, date_tabel)


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
        self.__init__(self.loginf)
