import sqlite3
import bcrypt

class Utility():
    def __init__(self, AccWindow):
        self.AccWindow = AccWindow



    def countCurrentNrOfAcs(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT count(*) FROM accounts_test WHERE userid = :id", {'id': self.AccWindow.current_acc_id})
        count = d.fetchone()
        return from_list_to_int(count)


    def get_name_of_acc(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT name FROM accounts_test WHERE userid = :id",
        {
            'id': self.AccWindow.current_acc_id,

        })
        result = d.fetchall()
        return (
            "".join(map(str, result))
            .replace("'", "")
            .replace("(", "")
            .replace(")", "")
            .replace(",", " ")
        )


    def get_name_of_acc_transaction(self, AccWindow):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        d.execute("SELECT name FROM accounts_test WHERE userid = :id",
        {
            'id': AccWindow.current_acc_id,

        })
        result = d.fetchall()
        return (
            "".join(map(str, result))
            .replace("'", "")
            .replace("(", "")
            .replace(")", "")
            .replace(",", " ")
        )



def passwordHashing(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14)).decode('utf-8')

def validateCredentials(password, password_hash):
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

def pass_id_to_acc_tab(LoginForm):
    db = sqlite3.connect("expense_tracker.db")
    db_cursor = db.cursor()
    db_cursor.execute("""SELECT id from users WHERE username = :username""",
    {'username': LoginForm.le_username.text()
    })

    dummy= db_cursor.fetchone()


    LoginForm.idd.append(from_list_to_int(dummy))


def from_list_to_int(string):
    res = ""
    for i in string:
        if len(res) > 1:
            break
        res +=str(i)
    return int(res)


def from_list_to_float(string):
    res = "".join(str(i) for i in string)
    return float(res)

def check_for_minus_or_plus(string):
    if type(string) in [int, float]:
        return "+" if string > 0 else "-"
    return "-" if string[0] == "-" else "+"

def splitIntoList(string): # to be modified
    return string.split(" ", 3)