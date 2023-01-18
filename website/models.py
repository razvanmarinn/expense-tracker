from flask_login import LoginManager
import psycopg2
from datetime import datetime



def from_list_to_int(string):
    if string is None:
        return None
    res = ""
    for i in string:
        if len(res) > 1:
            break
        res +=str(i)
    return int(res)

def from_list_to_str(string):
    if string is None:
        return None
    res = ""
    for i in string:
        if len(res) > 1:
            break
        res +=str(i)
    return res

def from_list_to_float(string):
    res = "".join(str(i) for i in string)
    return float(res)

def check_for_minus_or_plus(string):
    if string == None:
        return None
    if type(string) in [int, float]:
        return "+" if string > 0 else "-"
    return "-" if string[0] == "-" else "+"

def splitIntoList(string): # to be modified
    if string == None:
        return None
    return [x for x in string.split(" ") if x != ""]






login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    # Return the user object for the user ID
    return User.get(user_id)

class User:
    def __init__(self,id , username, password):
        self.id = id
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @classmethod
    def get(cls, user_id):
        conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id=%s"%(user_id))
        actual_user = c.fetchone()
        # Retrieve the user object from the database
        user = User(actual_user[0], actual_user[1], actual_user[2])
        return user

class UserModel:
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')

    def create_user(self, user):
        c = self.conn.cursor()
        c.execute(
            f"INSERT INTO users (username, password) VALUES ('{user.username}', '{user.password}');"
        )
        self.conn.commit()
        return c.lastrowid

    def get_user(self, user_id):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM users WHERE id={user_id}")
        return c.fetchone()

    def get_user_by_username(self, username):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM users WHERE username='{username}'")
        return c.fetchone()


    def delete_user_by_username(self, username):
        c = self.conn.cursor()
        c.execute(f"DELETE FROM users WHERE username='{username}'")
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

class Account:
    def __init__(self, name, balance, userid):
        self.id = None
        self.name = name
        self.balance = balance
        self.iban = fake.iban()
        self.userid = userid


class AccountModel:
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')

    def create_account(self, Account):
        c = self.conn.cursor()
        c.execute(
            f"INSERT INTO accounts_test (name, balance,iban, userid) VALUES ( '{Account.name}', '{Account.balance}', '{Account.iban}','{Account.userid}') ;"
        )
        self.conn.commit()
        return c.lastrowid


    def get_iban(self, acc_id):
        if acc_id == None:
            return None
        c = self.conn.cursor()
        c.execute(f"SELECT iban from accounts_test WHERE accounts_id = {acc_id}")
        return from_list_to_str(c.fetchone())

    def count_accounts(self, userid):
        c = self.conn.cursor()
        c.execute(f"SELECT COUNT(*) FROM accounts_test WHERE userid={userid}")
        return from_list_to_int(c.fetchone())

    def get_account_id(self, name, userid):
        c = self.conn.cursor()
        c.execute(f"SELECT accounts_id FROM accounts_test WHERE name='{name}' and userid={userid}")
        return from_list_to_int(c.fetchone())

    def get_account_balance(self, account_id):
        c = self.conn.cursor()
        c.execute(f"SELECT balance FROM accounts_test WHERE accounts_id={account_id}")
        return from_list_to_float(c.fetchone())


    def get_name_of_acc(self, user_id):
        c = self.conn.cursor()
        c.execute(f"SELECT name FROM accounts_test WHERE userid={user_id};")
        return (
        "".join(map(str, c.fetchall()))
        .replace("'", "")
        .replace("(", "")
        .replace(")", "")
        .replace(",", " ")
        )

    def get_account_by_iban(self, IBAN):
        c = self.conn.cursor()
        c.execute(f"SELECT * from accounts_test WHERE iban = '{IBAN}'")
        return c.fetchone()

    def set_new_balance(self, value, account_id):
        c = self.conn.cursor()
        c.execute(f"UPDATE accounts_test SET balance={value} WHERE accounts_id={account_id}")
        self.conn.commit()

    def delete_account(self, name ,user_id):
        c = self.conn.cursor()
        c.execute(f"DELETE FROM accounts_test WHERE userid={user_id} and name='{name}'")
        self.conn.commit()


    def update_balance_by_iban(self, value , IBAN):
        c = self.conn.cursor()
        c.execute(f"UPDATE accounts_test SET balance={value}  WHERE iban = '{IBAN}'")
        self.conn.commit()

class Transfer:
    def __init__(self, sender_acc_id, iban_receiver, value, description) :
       self.sender_acc_id = sender_acc_id
       self.iban_receiver = str(iban_receiver)
       self.value = value
       self.description = description


class TransferModel:
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')
        self.acc_model = AccountModel()

    def get_transfer_id(self, sender_acc_id, iban_receiver, value):
        c = self.conn.cursor()
        c.execute(f"SELECT transfer_id FROM transfers WHERE sender_acc_id={sender_acc_id} and receiver_iban='{iban_receiver}' and value={value}")
        return from_list_to_int(c.fetchone())

    def execute_the_transfer(self, transfer_id):
        c = self.conn.cursor()
        Transfer = self.get_transfer_by_id(transfer_id)
        test = self.acc_model.get_account_balance(Transfer[1])
        self.acc_model.set_new_balance(test - Transfer[3], Transfer[1])
        balance = self.acc_model.get_account_by_iban(Transfer[2])[2]
        balance = balance + Transfer[3]
        self.acc_model.update_balance_by_iban(balance, Transfer[2])
        time = datetime.now().strftime("%d/%m/%Y")
        c.execute(f"INSERT INTO transactions (name, value, date, type_of, account_id) VALUES ('transfer to another acc', -{Transfer[3]}, '{time}' , 'Transfer', '{Transfer[1]}' )")
        c.execute(f"INSERT INTO transactions (name, value, date, type_of, account_id) VALUES ('Transfer Received', {Transfer[3]}, '{time}' , 'Transfer', '{self.acc_model.get_account_by_iban(Transfer[2])[0]}' )")
        self.conn.commit()

    def get_transfer_by_id(self, transfer_id):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM transfers WHERE transfer_id={transfer_id}")
        return c.fetchone()

    def create_transfer(self, Transfer):

        c = self.conn.cursor()
        c.execute(f"INSERT INTO transfers (sender_acc_id, receiver_iban, value,status,  description) VALUES ({Transfer.sender_acc_id}, '{Transfer.iban_receiver}', {Transfer.value},'pending', '{Transfer.description}')")

        self.conn.commit()
        return c.lastrowid

    def approve_the_transfer(self, transfer_id):
        c = self.conn.cursor()
        c.execute(f"UPDATE transfers SET status='approved' WHERE transfer_id={transfer_id}")
        self.execute_the_transfer(transfer_id)
        self.conn.commit()



    def delete_transfer(self, transfer_id):
        c = self.conn.cursor()
        c.execute(f"DELETE FROM transfers WHERE transfer_id = {transfer_id}")
        self.conn.commit()


    def get_all_transfers(self):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM transfers")
        return c.fetchall()

