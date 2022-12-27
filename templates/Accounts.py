from PyQt6.QtWidgets import QApplication, QDialog
from UI.Accounts import Ui_AccountsForm
import sqlite3
from PyQt6 import QtWidgets
from templates.popup.TransactionsPopUp import TransactionPopup
from templates.popup.AccountPopUp import PopUpWindowAcc
from templates.Buttons import RemoveAccButton
from templates.Util import Utility
from templates.Graphs import GraphForm


class AccountsFormTab(QDialog, Ui_AccountsForm):
    
    def __init__(self, LoginForm):
        super().__init__()
        self.setupUi(self, LoginForm)
        self.show()
        self.loginf = LoginForm # LOGIN FORM PASSED TO GET INFO FROM IT
        self.MAX_ACCOUNTS_PER_USER = 3 # STATIC VARIABLE
        self.current_acc_id = LoginForm.idd[0] # CURRENT ID OF THE USER
        self.RemoveButton = RemoveAccButton(self)
        self.Utility = Utility(self)
        self.current_ACCOUNT_id = 0 # CURRENT ACCOUNT ID 
        self.pb_analyze.clicked.connect(self.create_analysis_popup)

        self.current_nr_of_acc = self.Utility.countCurrentNrOfAcs()
        #add items to dropdown box
        element = self.Utility.getNameOfTheAccountsOfThisId() # NAMES OF THE ACCOUNTS
        self.actual_element = self.Utility.splitIntoList(element) # ACTUAL_ELEMENT
        self.cb_dropdown.addItems(self.actual_element)

        self.pb_addacc.clicked.connect(self.create_popup)
        self.pb_removeacc.clicked.connect(self.RemoveButton.functionality)
        self.pb_logout.clicked.connect(self.logout)


        self.pb_addtransaction.clicked.connect(self.createTransactionPopup)

        self.setData() # SET DATA IN THE TABLE

        self.cb_dropdown.currentIndexChanged.connect(self.setData)
        
    
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
        self.current_ACCOUNT_id = accid
        d.execute("SELECT * from transactions WHERE account_id = :accid" , {'accid': accid})
        temp2 = d.fetchall()
        
        list_of_transactions = []
    
        if temp2 != None:
            for i in temp2:
                list_of_transactions.append(i)
        id = []
        name = []
        value = []
        budget = []
        type = []
        date = []
        if list_of_transactions != None:
            for i in range(len(list_of_transactions)):
                    id.append(list_of_transactions[i][0])
                    name.append(list_of_transactions[i][1])
                    value.append(list_of_transactions[i][2]) 
                    budget.append(list_of_transactions[i][3])
                    type.append(list_of_transactions[i][4])
                    date.append(list_of_transactions[i][5])


            self.tw_showinfo.setRowCount(len(list_of_transactions))
          
            row = 0
           
            for j in range(len(id)):
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
                
                row+=1


    def createTransactionPopup(self):
        if(self.actual_element[0] == ""):
            print("No accounts on this user")
        else:
            transaction = TransactionPopup(self)
            transaction.show()

    def create_popup(self):
        pop = PopUpWindowAcc(self)
        pop.show()
    def create_analysis_popup(self):
        analysis = GraphForm(self)
        analysis.show()


    def logout(self):
        QApplication.exit()
        
    def createNew(self):
        self.hide()
        self.__init__(self.loginf)
    
 
        


 
       
