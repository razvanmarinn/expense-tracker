from PyQt6.QtWidgets import QMainWindow, QApplication, QStackedWidget, QDialog, QLabel,QTableWidget,QTableWidgetItem
import sys
from UI.Accounts import Ui_AccountsForm
import sqlite3
import time
from datetime import datetime
from PyQt6 import QtWidgets
from UI.popup import Ui_PopupForm
from templates.transactions_popup import TransactionPopup

class AccountsFormTab(QDialog, Ui_AccountsForm):
    
    def __init__(self, LoginForm):
        super().__init__()
        self.setupUi(self, LoginForm)
        self.show()
        self.loginf = LoginForm # LOGIN FORM PASSED TO GET INFO FROM IT
        self.MAX_ACCOUNTS_PER_USER = 3 # STATIC VARIABLE
        self.current_acc_id = LoginForm.idd[0] # CURRENT ID OF THE USER ACC
       
        #
        self.current_nr_of_acc = self.countCurrentNrOfAcs()
        #add items to dropdown box
        element = self.getNameOfTheAccountsOfThisId() # NAMES OF THE ACCOUNTS
        actual_element = self.splitIntoList(element) # ACTUAL_ELEMENT
        self.cb_dropdown.addItems(actual_element)

        self.pb_addacc.clicked.connect(self.create_popup)
        self.pb_removeacc.clicked.connect(self.removeAcc)
        self.pb_logout.clicked.connect(self.logout)
        self.pb_addtransaction.clicked.connect(self.createTransactionPopup)
        self.setData() # SET DATA IN THE TABLE

        
        
    
    def setData(self): 
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        curr_text = self.cb_dropdown.currentText() # CURRENT DROPDOWN TEXT
        
        d.execute("SELECT accounts_id from accounts_test WHERE name = :name  AND userid = :userid" ,
        {'name': curr_text , 'userid': self.current_acc_id})
        temp = d.fetchone()
        accid = ""
        if temp != None:
            for i in temp:
                accid +=str(i)
                
            accid = int(accid)

        d.execute("SELECT * from transactions WHERE account_id = :accid" , {'accid': accid})
        temp2 = d.fetchall()
        
        list_of_transactions = []
    
        if temp2 != None:
            for i in temp2:
                list_of_transactions.append(i)
        #print(list_of_transactions)
        id = []
        name = []
        value = []
        budget = []
        date = []
        if list_of_transactions != None:
            for i in range(len(list_of_transactions)):
                    id.append(list_of_transactions[i][0])
                    name.append(list_of_transactions[i][1])
                    value.append(list_of_transactions[i][2]) 
                    budget.append(list_of_transactions[i][3])
                    date.append(list_of_transactions[i][4])


        


            
            self.tw_showinfo.setRowCount(len(list_of_transactions))
          
            row = 0
           
            for j in range(len(id)):
                id_tabel = QtWidgets.QTableWidgetItem(str(id[j]))
                name_tabel = QtWidgets.QTableWidgetItem(str(name[j]))
                value_tabel = QtWidgets.QTableWidgetItem(str(value[j]))
                budget_tabel = QtWidgets.QTableWidgetItem(str(budget[j]))
                date_tabel = QtWidgets.QTableWidgetItem(str(date[j]))
                self.tw_showinfo.setItem(row, 0, id_tabel)
                self.tw_showinfo.setItem(row, 3, value_tabel)
                self.tw_showinfo.setItem(row, 1, budget_tabel)
                self.tw_showinfo.setItem(row, 4, date_tabel)
                self.tw_showinfo.setItem(row, 2, name_tabel)
                row+=1

    def createTransactionPopup(self):
        transaction = TransactionPopup(self)
        transaction.show()



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


    def getNameOfTheAccountsOfThisId(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT name FROM accounts_test WHERE userid = :id", 
        {
            'id': self.current_acc_id,
            
        })
        result = d.fetchall()
        #print(result)
        str_result = "".join(map(str, result)).replace("'", "").replace("(", "").replace(")", "").replace(",", " ")
        
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
        




