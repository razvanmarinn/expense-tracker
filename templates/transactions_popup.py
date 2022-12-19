from PyQt6.QtWidgets import QMainWindow, QApplication, QStackedWidget, QDialog, QLabel,QTableWidget,QTableWidgetItem
import sqlite3
from datetime import datetime
from PyQt6 import QtWidgets
from UI.transactions import Ui_PopUpTransactions



class TransactionPopup(QDialog, Ui_PopUpTransactions):
    def __init__(self, AccWindow):
        super().__init__(AccWindow)
        self.setupUi(self, AccWindow)
        self.AccWindow = AccWindow
        self.show()
        self.pb_addTransactions.clicked.connect(self.add_Transaction)
    def checkForMinusOrPlus(self, string):
        if string[0] == "-":
            return "-"
        else:
            return "+"

    def add_Transaction(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        
        d.execute("SELECT accounts_id FROM accounts_test WHERE name = :name AND userid = :userid" , 
        {'name': self.le_accname.text(),
        'userid': self.AccWindow.current_acc_id
        })
        accountId = d.fetchone()
        accountIdInt = ""
        for i in accountId:
            accountIdInt +=str(i)
        accountIdInt = int(accountIdInt)
        print(accountIdInt)

        curdate = datetime.now()
        dt_string = curdate.strftime("%d/%m/%Y")

        d.execute("SELECT balance FROM accounts_test WHERE accounts_id = :accid", {'accid': accountIdInt})
        res = d.fetchone()
        resInt = ""
        for i in res:
            resInt +=str(i)
        resInt = float(resInt)
        sign = self.checkForMinusOrPlus(self.le_value.text())
        if(sign == "-"):
            resInt = resInt - (-1 * float(self.le_value.text()))
            print(resInt)
        else:
            resInt = resInt + float(self.le_value.text())
            print(resInt)
        d.execute("INSERT INTO transactions (name, balance, value, date, account_id )VALUES (:name, :balance, :value, :date , :account_id)",
            {
                'name': self.le_nume.text(),
                'value': self.le_value.text(), 
                'balance': resInt,
                'account_id': accountIdInt,
                'date': dt_string
            } ) 
        d.execute("UPDATE accounts_test SET balance = :new_budget WHERE accounts_id = :accid", {'accid': accountIdInt, 'new_budget': resInt})

        db.commit()
        self.AccWindow.createNew()
        self.hide()
        