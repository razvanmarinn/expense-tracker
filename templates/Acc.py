from PyQt6.QtWidgets import QMainWindow, QApplication, QStackedWidget, QDialog, QLabel,QTableWidget,QTableWidgetItem
import sys
from UI.Accounts import Ui_AccountsForm
import sqlite3
import time
from datetime import datetime
from PyQt6 import QtWidgets
from UI.popup import Ui_PopupForm
from templates.classes import Account

class AccountsFormTab(QDialog, Ui_AccountsForm):
    
    def __init__(self, LoginForm):
        data = []
        super().__init__()
        self.setupUi(self, LoginForm)
        self.show()
        self.loginf = LoginForm
        self.pb_addacc.clicked.connect(self.create_popup)
        #self.id = LoginForm.idofacc
        self.MAX_ACCOUNTS_PER_USER = 3
        self.current_acc_id = LoginForm.idd[0]
        self.l_accounts.setText(str(self.current_acc_id))
        self.pb_addtransaction.clicked.connect(self.populateDropBox)
        self.current_nr_of_acc = self.countCurrentNrOfAcs()
        element = self.populateDropBox()
        actual_element = self.splitIntoList(element)
        print(actual_element)
        self.cb_dropdown.addItems(actual_element)
        #self.cb_dropdown.removeItem()
        self.pb_removeacc.clicked.connect(self.removeAcc)
        self.pb_logout.clicked.connect(self.logout)
        self.setData()
        #self.tw_showinfo.setRowCount(3)
        #self.tw_showinfo.setItem(0,0, QtWidgets.QTableWidgetItem("TEST")
        self.data = data
    
    def setData(self): 
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        curr_text = self.cb_dropdown.currentText()
        print(curr_text)
        d.execute("SELECT accounts_id from accounts_test WHERE name = :name  AND userid = :userid" ,
        {'name': curr_text , 'userid': self.current_acc_id})
        temp = d.fetchone()
        accid = ""
        if temp != None:
            for i in temp:
                accid +=str(i)
            accid = int(accid)

        d.execute("SELECT * from transactions WHERE account_id = :accid" , {'accid': accid})
        temp2 = d.fetchone()
        list_of_transactions = []
    
        if temp2 != None:
            for i in temp2:
                list_of_transactions.append(i)
        dict = {"id": list_of_transactions[0] , "name" : list_of_transactions[1], "value" : list_of_transactions[2], "budget": list_of_transactions[3], "date": list_of_transactions[4]}
        print(dict)
        print(list_of_transactions)
        self.tw_showinfo.setRowCount(len(dict))
        # for i, name , value, budget, date in enumerate(list_of_trans):
        id = QtWidgets.QTableWidgetItem(dict["id"])
        name = QtWidgets.QTableWidgetItem(dict["name"])
        value = QtWidgets.QTableWidgetItem(str(dict["value"]))
        budget = QtWidgets.QTableWidgetItem(str(dict["budget"]))
        date = QtWidgets.QTableWidgetItem(dict["date"])
        self.tw_showinfo.setItem(1, 0, id)
        self.tw_showinfo.setItem(0, 3, value)
        self.tw_showinfo.setItem(0, 1, budget)
        self.tw_showinfo.setItem(0, 4, date)
        self.tw_showinfo.setItem(0,2, name)
    def logout(self):
        QApplication.exit()
        
        

    def removeAcc(self):
        
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("DELETE FROM accounts_test WHERE name =:name", {'name': ""})
        # currentTextChanged signal will pass selected text to slot
        curr_index = self.cb_dropdown.currentIndex()
        print(curr_index)
        self.cb_dropdown.removeItem(curr_index)  # remove item from index
        self.createNew()
        db.commit()

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
            d.execute("SELECT accounts_id FROM accounts_test WHERE name = :name", 
            {'name': self.le_accountname.text()
            })
            accountId = d.fetchone()
            accountIdInt = ""
            for i in accountId:
                accountIdInt +=str(i)
                accountIdInt = int(accountIdInt)
            curdate = datetime.now()
            dt_string = curdate.strftime("%d/%m/%Y")
            
            d.execute("INSERT INTO transactions (name, balance, value, account_id, date) VALUES (:name,:balance, :value ,:id , :date)", 
            { 'name' : "init", 
            'balance': int(self.le_budgetname.text()),
            'value': int(self.le_budgetname.text()), 
            'id': accountIdInt,
            'date': dt_string
            } )
            
            self.accwindow.cb_dropdown.addItem(self.le_accountname.text()) 


            
        


            db.commit()
            self.accwindow.createNew()
            self.hide()
        





# app = QApplication(sys.argv)
# Account = AccountsFormTab()

# sys.exit(app.exec())
