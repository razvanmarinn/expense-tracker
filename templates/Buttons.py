from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime
import time



class Button(ABC):
    @abstractmethod
    def functionality(self):
        pass

class AddAccButton(Button):
    def __init__(self, Accpop):
        self.accpop = Accpop

    def functionality(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT count(*) FROM accounts_test WHERE userid = :id", {'id': self.accpop.accwindow.current_acc_id})
        result = d.fetchone()
        noOfAcc = ""
        for i in result:
            noOfAcc +=str(i)
        noOfAcc = int(noOfAcc)
        if noOfAcc >= self.accpop.accwindow.MAX_ACCOUNTS_PER_USER:
            print("max accs")
        else:
            d.execute("INSERT INTO accounts_test (name, balance, userid) VALUES (:name,:balance,:id)", 
            { 'name' : self.accpop.le_accountname.text(), 
            'balance': int(self.accpop.le_budgetname.text()), 
            'id': self.accpop.accwindow.current_acc_id
            } )
            d.execute("SELECT accounts_id FROM accounts_test WHERE name = :name", 
            {'name': self.accpop.le_accountname.text()
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
            'balance': int(self.accpop.le_budgetname.text()),
            'value': int(self.accpop.le_budgetname.text()), 
            'id': accountIdInt,
            'date': dt_string
            } )
            
            self.accpop.accwindow.cb_dropdown.addItem(self.accpop.le_accountname.text()) 
            db.commit()
            self.accpop.accwindow.createNew()
            self.accpop.hide()


class RemoveAccButton(Button):
    def __init__(self, AccWindow):
        self.AccWindow = AccWindow

    def functionality(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        if(self.AccWindow.actual_element[0] == ""):
            print("No accounts to be removed")
        else:
            d.execute("DELETE FROM accounts_test WHERE name =:name", {'name': self.AccWindow.cb_dropdown.currentText()})
            # currentTextChanged signal will pass selected text to slot
            curr_index = self.AccWindow.cb_dropdown.currentIndex()
            self.AccWindow.cb_dropdown.removeItem(curr_index)  # remove item from index
            db.commit()
            self.AccWindow.createNew()


class AddTransaction(Button):
    def __init__(self, TransPopup):
        self.TransPopup = TransPopup

    def checkForMinusOrPlus(self, string):
        if string[0] == "-":
            return "-"
        else:
            return "+"

    def functionality(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT accounts_id FROM accounts_test WHERE name = :name AND userid = :userid" , 
        {'name': self.TransPopup.cb_accounts.currentText(),
        'userid': self.TransPopup.AccWindow.current_acc_id
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
        sign = self.checkForMinusOrPlus(self.TransPopup.le_value.text())
        if(sign == "-"):
            resInt = resInt - (-1 * float(self.TransPopup.le_value.text()))
            print(resInt)
        else:
            resInt = resInt + float(self.TransPopup.le_value.text())
            print(resInt)
        d.execute("INSERT INTO transactions (name, balance, value, date, account_id )VALUES (:name, :balance, :value, :date , :account_id)",
            {
                'name': self.TransPopup.le_nume.text(),
                'value': self.TransPopup.le_value.text(), 
                'balance': resInt,
                'account_id': accountIdInt,
                'date': dt_string
            } ) 
        d.execute("UPDATE accounts_test SET balance = :new_budget WHERE accounts_id = :accid", {'accid': accountIdInt, 'new_budget': resInt})

        db.commit()
        self.TransPopup.AccWindow.createNew()
        self.TransPopup.hide()


class LoginButton(Button):
    def __init__(self, LoginForm):
        self.LoginForm = LoginForm
    def functionality(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("""SELECT username, password FROM users WHERE username =:username AND password=:password """, 
            {
            'username' : self.LoginForm.le_username.text(),
            'password': self.LoginForm.le_password.text()
            })

        result = d.fetchone()
        if result == None:
            self.LoginForm.l_loggedin.setText("Error")
        else:
            self.LoginForm.l_loggedin.setText("Logged in")
            d.execute("""SELECT id from users WHERE username = :username""",
            {'username': self.LoginForm.le_username.text()
            })
            dummy= d.fetchone()
            idofacc = ""
            for i in dummy:
                idofacc +=str(i)
            self.LoginForm.idd.append(int(idofacc))
            time.sleep(2)
            self.LoginForm.switch_to_accounts()
        db.commit()

class CreateUserAcc(Button):
    def __init__(self, LoginForm):
        self.LoginForm = LoginForm
    def functionality(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT username from users WHERE username = :username", {'username': self.LoginForm.le_username.text()})
        result = d.fetchone()
        if result == None:
            d.execute("INSERT INTO users (username, password )VALUES (:username, :password)",
                {
                    'username': self.LoginForm.le_username.text(),
                    'password': self.LoginForm.le_password.text()
                }
            )  
        else:
            self.LoginForm.l_loggedin.setText("username already exists") 

        db.commit()

class AddRecTransaction(Button):
    def __init__(self, RecTrPopup):
        self.RecTrPopup = RecTrPopup

    def checkForMinusOrPlus(self, string):
        if string[0] == "-":
            return "-"
        else:
            return "+"

    def functionality(self): # TO BE MODIFIED
        pass
        # db = sqlite3.connect("expense_tracker.db") # 
        # d = db.cursor()
        # d.execute("SELECT accounts_id FROM accounts_test WHERE name = :name AND userid = :userid" , 
        # {'name': self.RecTrPopup.cb_accounts.currentText(),
        # 'userid': self.RecTrPopup.AccWindow.current_acc_id
        # })
        # accountId = d.fetchone()
        # accountIdInt = ""
        # for i in accountId:
        #     accountIdInt +=str(i)
        # accountIdInt = int(accountIdInt)
    

    

        # d.execute("SELECT balance FROM accounts_test WHERE accounts_id = :accid", {'accid': accountIdInt})
        # res = d.fetchone()
        # resInt = ""
        # for i in res:
        #     resInt +=str(i)
        # resInt = float(resInt)
        # sign = self.checkForMinusOrPlus(self.RecTrPopup.le_value.text())
        # if(sign == "-"):
        #     resInt = resInt - (-1 * float(self.RecTrPopup.le_value.text()))
        #     print(resInt)
        # else:
        #     resInt = resInt + float(self.RecTrPopup.le_value.text())
        #     print(resInt)

        # start_date = self.RecTrPopup.de_startdate.date()
        # actual_start_date = start_date.toPyDate()
        # print(actual_start_date)
        # d.execute("INSERT INTO transactions (name, balance, value, date, account_id )VALUES (:name, :balance, :value, :date , :account_id)",
        #     {
        #         'name': self.RecTrPopup.le_name.text(),
        #         'value': self.RecTrPopup.le_value.text(), 
        #         'balance': resInt,
        #         'account_id': accountIdInt,
        #         'date': actual_start_date
        #     } ) 
        # d.execute("UPDATE accounts_test SET balance = :new_budget WHERE accounts_id = :accid", {'accid': accountIdInt, 'new_budget': resInt})

        # db.commit()
        # self.RecTrPopup.AccWindow.createNew()
        # self.RecTrPopup.hide()