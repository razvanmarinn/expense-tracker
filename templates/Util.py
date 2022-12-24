import sqlite3
import bcrypt

class Utility():
    def __init__(self, AccWindow):
        self.AccWindow = AccWindow

    def splitIntoList(self, string): # to be modified
        split_result = string.split(" ", 3)
        
        return split_result

    def countCurrentNrOfAcs(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT count(*) FROM accounts_test WHERE userid = :id", {'id': self.AccWindow.current_acc_id})
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
            'id': self.AccWindow.current_acc_id,
            
        })
        result = d.fetchall()
        #print(result)
        str_result = "".join(map(str, result)).replace("'", "").replace("(", "").replace(")", "").replace(",", " ")
        return str_result


    def getNameOfTheAccountsOfThisIdTrans(self, AccWindow):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT name FROM accounts_test WHERE userid = :id", 
        {
            'id': AccWindow.current_acc_id,
            
        })
        result = d.fetchall()
        #print(result)
        str_result = "".join(map(str, result)).replace("'", "").replace("(", "").replace(")", "").replace(",", " ")
        return str_result

def passwordHashing(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14)).decode('utf-8')

def validateCredentials(password, password_hash):
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))






def exec(LoginForm):
    db = sqlite3.connect("expense_tracker.db")
    d = db.cursor()
    d.execute("""SELECT id from users WHERE username = :username""",
    {'username': LoginForm.le_username.text()
    })

    dummy= d.fetchone()
    idofacc = ""
    for i in dummy:
        idofacc +=str(i)
        
    LoginForm.idd.append(int(idofacc)) 

    