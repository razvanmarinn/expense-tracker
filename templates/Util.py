import sqlite3
import bcrypt
import psycopg2


conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()



class Utility():
    def __init__(self, AccWindow):
        self.AccWindow = AccWindow



    def countCurrentNrOfAcs(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT count(*) FROM accounts_test WHERE userid = :id", {'id': self.AccWindow.current_acc_id})
        count = d.fetchone()
        noOfAcc = from_list_to_int(count)

        return noOfAcc


    def get_name_of_acc(self):
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


    def get_name_of_acc_transaction(self, AccWindow):
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

def pass_id_to_acc_tab(LoginForm):

    cursor.execute("SELECT id from users WHERE username = '%s'" %(LoginForm.le_username.text()))

    dummy= cursor.fetchone()


    LoginForm.idd.append(from_list_to_int(dummy))


def from_list_to_int(string):
    res = ""
    for i in string:
        if len(res) > 1:
            break
        res +=str(i)
    res = int(res)
    return res


def from_list_to_float(string):
    res = ""
    for i in string:
        res +=str(i)
    res = float(res)
    return res

def check_for_minus_or_plus(string):
    if type(string) == int or type(string) == float:
        if string > 0:
            return "+"
        else:
            return "-"
    if string[0] == "-":
        return "-"
    return "+"

def splitIntoList(string): # to be modified
        split_result = string.split(" ", 3)

        return split_result