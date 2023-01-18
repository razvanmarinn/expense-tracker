import psycopg2
from general.util import from_list_to_int, from_list_to_float, from_list_to_str
from faker import Faker
from datetime import datetime
from general.exceptions import TransferToSameAccountException, NoAccountException

fake = Faker()
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
            f"INSERT INTO transactions (name, value, type_of, account_id, date) VALUES ( '{Transaction.name}', {Transaction.value},'{Transaction.type_of}', {Transaction.account_id}, '{Transaction.date}');"
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
        if account_id is None:
            raise NoAccountException("No account with this id")
        c = self.conn.cursor()
        c.execute(f"DELETE FROM transactions WHERE account_id={account_id}")
        self.conn.commit()

    def get_transaction_by_acc_id(self, accid):
        if accid is None:
            raise NoAccountException("No account with this id")
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM transactions WHERE account_id={accid}")

        return c.fetchall()



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


        if (self.acc_model.get_iban(Transfer.sender_acc_id) == Transfer.iban_receiver):
            raise TransferToSameAccountException("You can't transfer to the same account")

        else:
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


