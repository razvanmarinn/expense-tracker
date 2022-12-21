import sqlite3


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