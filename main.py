from PyQt6.QtWidgets import QMainWindow, QApplication, QStackedWidget, QDialog, QLabel
import sys
from UI.Login import Ui_LoginForm
from templates.Acc import AccountsFormTab
import sqlite3
import time


class LoginFormWindow(QDialog, Ui_LoginForm):
    idd = []
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.show()
        self.b_login.clicked.connect(self.loginButtonExec)
        self.b_createacc.clicked.connect(self.createAccount)

    def loginButtonExec(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("""SELECT username, password FROM users WHERE username =:username AND password=:password """, 
            {
            'username' : self.le_username.text(),
            'password': self.le_password.text()
            })

        result = d.fetchone()
        if result == None:
            self.l_loggedin.setText("Error")
        else:
            self.l_loggedin.setText("Logged in")
            d.execute("""SELECT id from users WHERE username = :username""",
            {'username': self.le_username.text()
            })
            dummy= d.fetchone()
            idofacc = ""
            for i in dummy:
                idofacc +=str(i)
            self.idd.append(int(idofacc))
            
            
            time.sleep(2)
            
            self.switch_to_accounts()
        db.commit()


    
    def switch_to_accounts(self):
        self.window= QMainWindow()
        self.ui= AccountsFormTab(LoginFormWindow)     #------------->creating an object 
        self.ui.setupUi(self.window, LoginFormWindow)
        # self.window.show()
        self.hide()

    def createAccount(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()

        name = self.le_username.text()
        password = self.le_password.text()

        #acc = templatesapp.Account(name, budget)
        d.execute("SELECT username from users WHERE username = :username", {'username': self.le_username.text()})
        result = d.fetchone()
        if result == None:
            d.execute("INSERT INTO users (username, password )VALUES (:username, :password)",
                {
                    'username': self.le_username.text(),
                    'password': self.le_password.text()
                }
            )  
        else:
            self.l_loggedin.setText("username already exists") 

        db.commit()



app = QApplication(sys.argv)


Login = LoginFormWindow()


sys.exit(app.exec())


