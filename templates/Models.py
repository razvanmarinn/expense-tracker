import psycopg2
from templates.Util import from_list_to_int, from_list_to_float


class User:
    def __init__(self, username, password):
        self.id = None
        self.username = username
        self.password = password


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

    def get_user_id_by_username(self, username):
        c = self.conn.cursor()
        c.execute(f"SELECT id FROM users WHERE username='{username}'")
        return from_list_to_int(c.fetchone())

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
        self.userid = userid


class AccountModel:
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')

    def create_account(self, Account):
        c = self.conn.cursor()
        c.execute(
            f"INSERT INTO accounts_test (name, balance, userid) VALUES ( '{Account.name}', '{Account.balance}', '{Account.userid}') ;"
        )
        self.conn.commit()
        return c.lastrowid

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



    def set_new_balance(self, value, account_id):
        c = self.conn.cursor()
        c.execute(f"UPDATE accounts_test SET balance={value} WHERE accounts_id={account_id}")
        self.conn.commit()

    def delete_account(self, name ,user_id):
        c = self.conn.cursor()
        c.execute(f"DELETE FROM accounts_test WHERE userid={user_id} and name='{name}'")
        self.conn.commit()


class Transaction:
    def __init__(self, name, value, date, type_of, account_id, userid):
        self.id = None
        self.name = name
        self.value = value
        self.date = date
        self.type_of = type_of
        self.account_id = account_id
        self.userid = userid


class TransactionModel:
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')

    def create_transaction(self, Transaction):
        c = self.conn.cursor()
        c.execute(
            f"INSERT INTO transactions (name, value, type_of, account_id, date) VALUES ( '{Transaction.name}', {Transaction.value},'{Transaction.type_of}', {Transaction.account_id}, {Transaction.date});"
        )
        self.conn.commit()
        return c.lastrowid
    def get_transaction_id(self, name, account_id):
        c = self.conn.cursor()
        c.execute(f"SELECT transaction_id FROM transactions WHERE name='{name}' and account_id='{account_id}'")
        return c.fetchone()

    def delete_transaction(self, transaction_id):
        c = self.conn.cursor()
        c.execute(f"DELETE FROM transactions WHERE transaction_id={transaction_id}")
        self.conn.commit()

    def delete_transaction_by_acc_id(self, account_id ):
        c = self.conn.cursor()
        c.execute(f"DELETE FROM transactions WHERE account_id={account_id}")
        self.conn.commit()

    def get_transaction_by_acc_id(self, accid):
        if accid is None:
            return None
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM transactions WHERE account_id={accid}")
        return c.fetchall()


