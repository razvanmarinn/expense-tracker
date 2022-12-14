from PyQt6.QtWidgets import QMainWindow, QApplication, QStackedWidget, QDialog, QLabel
import sys
from UI.Accounts import Ui_AccountsForm
import sqlite3
import time
from PyQt6 import QtWidgets
from UI.popup import Ui_PopupForm
from templates.classes import Account

class AccountsFormTab(QDialog, Ui_AccountsForm):
    
    def __init__(self, LoginForm):
        super().__init__()
        self.setupUi(self, LoginForm)
        self.show()
        self.loginf = LoginForm
        self.pb_addacc.clicked.connect(self.create_popup)
        #self.id = LoginForm.idofacc
        self.MAX_ACCOUNTS_PER_USER = 322
        self.current_acc_id = LoginForm.idd[0]
        self.l_accounts.setText(str(self.current_acc_id))
        self.pb_addtransaction.clicked.connect(self.populateDropBox)
        self.current_nr_of_acc = self.countCurrentNrOfAcs()
        element = self.populateDropBox()
        actual_element = self.splitIntoList(element)
        print(actual_element)
        self.cb_dropdown.addItems(actual_element)


        self.pb_logout.clicked.connect(self.switch_to_accounts)



    def switch_to_accounts(self):
        self.window= QMainWindow()
        self.ui= self.loginf()     #------------->creating an object 
        self.ui.setupUi(self.window)
        # self.window.show()
        self.hide()
        

    def __del__():
        print("deleted")

    def splitIntoList(self, string):
        split_result = string.split(" ", 2)
        return split_result


    def createNew(self):
        self.hide()
        self.__init__(self.loginf)
        
    def countCurrentNrOfAcs(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT count(*) FROM accounts_test WHERE userid = :id", {'id': self.current_acc_id})
        count = d.fetchone()
        noOfAcc = ""

        for i in count:
            noOfAcc +=str(i)
        noOfAcc = int(noOfAcc)

        return noOfAcc


    def populateDropBox(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT name FROM accounts_test WHERE userid = :id", 
        {
            'id': self.current_acc_id,
            
        })
        result = d.fetchall()
        print(result)
        str_result = "".join(map(str, result)).replace("'", "").replace("(", "").replace(")", "").replace(",", " ")
        

        # for i in range(noOfAcc):
            
        #     print(str_result)
            # self.cb_dropdown.addItem()
        return str_result



    def create_popup(self):
        pop = PopUpWindowAcc(self)
        pop.show()
       


class PopUpWindowAcc(QDialog, Ui_PopupForm):
    def __init__(self, accwindow):
        super().__init__(accwindow)
        self.setupUi(self)
        self.show()
        self.accwindow = accwindow
        self.loginform = self.accwindow.loginf
        self.pb_add.clicked.connect(self.create_acc)
    def create_acc(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT count(*) FROM accounts_test WHERE userid = :id", {'id': self.accwindow.current_acc_id})
        result = d.fetchone()
        noOfAcc = ""
        for i in result:
            noOfAcc +=str(i)
        noOfAcc = int(noOfAcc)
        if noOfAcc >= self.accwindow.MAX_ACCOUNTS_PER_USER:
            print("max accs")
        else:
            d.execute("INSERT INTO accounts_test (name, balance, userid) VALUES (:name,:balance,:id)", 
            { 'name' : self.le_accountname.text(), 
            'balance': int(self.le_budgetname.text()), 
            'id': self.accwindow.current_acc_id
            } )
            
            self.accwindow.cb_dropdown.addItem(self.le_accountname.text()) 
            db.commit()
            self.accwindow.createNew()
            self.hide()
        

# app = QApplication(sys.argv)
# Account = AccountsFormTab()

# sys.exit(app.exec())
