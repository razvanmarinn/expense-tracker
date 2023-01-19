"""This module contains the models for the application."""
from datetime import datetime
import uuid
import psycopg2
from general.util import from_list_to_int, from_list_to_float, from_list_to_str
from general.exceptions import TransferToSameAccountException, NoAccountException

class User:
    """This class contains the user."""
    def __init__(self, username, password):
        self.id = None
        self.username = username
        self.password = password


class UserModel:
    """This class contains the methods for the user model."""
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')
        self.cursor = self.conn.cursor()
    def create_user(self, user):

        self.cursor.execute(
            f"INSERT INTO users (username, password) VALUES ('{user.username}', '{user.password}');"
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_user(self, user_id):
        """Get user by id"""
        self.cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
        return self.cursor.fetchone()

    def get_user_by_username(self, username):
        """Get user by username"""
        self.cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
        return self.cursor.fetchone()

    def get_user_id_by_username(self, username):
        """Get user id by username"""
        self.cursor.execute(f"SELECT id FROM users WHERE username='{username}'")
        return from_list_to_int(self.cursor.fetchone())

    def delete_user_by_username(self, username):
        """Delete user by username"""
        self.cursor.execute(f"DELETE FROM users WHERE username='{username}'")
        self.conn.commit()

    def close_connection(self):
        """Close connection"""
        self.conn.close()


class Account:
    """Account class"""
    def __init__(self, name, balance, userid):
        self.id = None
        self.name = name
        self.balance = balance
        self.uuid = uuid.uuid4()
        self.userid = userid


class AccountModel:
    """Account model class"""
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')
        self.cursor = self.conn.cursor()

    def create_account(self, account):
        """Create account"""
        self.cursor.execute(
            f"""INSERT INTO accounts_test (name, balance,uuid, userid) VALUES
             ( '{account.name}', '{account.balance}', '{account.uuid}','{account.userid}') ;"""
        )
        self.conn.commit()
        return self.cursor.lastrowid


    def get_uuid(self, acc_id):
        """Get uuid by account id"""
        if acc_id is None:
            return None
        self.cursor.execute(f"SELECT uuid from accounts_test WHERE accounts_id = {acc_id}")
        return from_list_to_str(self.cursor.fetchone())

    def count_accounts(self, userid):
        """Count accounts"""
        self.cursor.execute(f"SELECT COUNT(*) FROM accounts_test WHERE userid={userid}")
        return from_list_to_int(self.cursor.fetchone())

    def get_account_id(self, name, userid):
        """Get account id by name"""
        self.cursor.execute(f"SELECT accounts_id FROM accounts_test WHERE name='{name}' and userid={userid}")
        return from_list_to_int(self.cursor.fetchone())

    def get_account_balance(self, account_id):
        """Get account balance by account id"""
        self.cursor.execute(f"SELECT balance FROM accounts_test WHERE accounts_id={account_id}")
        return from_list_to_float(self.cursor.fetchone())


    def get_name_of_acc(self, user_id):
        """Get name of account by user id"""
        self.cursor.execute(f"SELECT name FROM accounts_test WHERE userid={user_id};")
        return (
        "".join(map(str, self.cursor.fetchall()))
        .replace("'", "")
        .replace("(", "")
        .replace(")", "")
        .replace(",", " ")
        )

    def get_account_by_uuid(self, uuid):
        """Get account by uuid"""
        self.cursor.execute(f"SELECT * from accounts_test WHERE uuid = '{uuid}'")
        return self.cursor.fetchone()

    def set_new_balance(self, value, account_id):
        """Set new balance"""
        self.cursor.execute(f"UPDATE accounts_test SET balance={value} WHERE accounts_id={account_id}")
        self.conn.commit()

    def delete_account(self, name ,user_id):
        """Delete account"""
        self.cursor.execute(f"DELETE FROM accounts_test WHERE userid={user_id} and name='{name}'")
        self.conn.commit()


    def update_balance_by_uuid(self, value , uuid):
        """Update balance by iban"""
        self.cursor.execute(f"UPDATE accounts_test SET balance={value}  WHERE uuid = '{uuid}'")
        self.conn.commit()


class Transaction:
    """Transaction class"""
    def __init__(self, name, value, date, type_of, account_id, userid):
        self.id = None
        self.name = name
        self.value = value
        self.date = date
        self.type_of = type_of
        self.account_id = account_id
        self.userid = userid


class TransactionModel:
    """Transaction model class"""
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')
        self.cursor = self.conn.cursor()

    def create_transaction(self, transaction):
        """Create a new transaction"""
        self.cursor.execute(
            f"""INSERT INTO transactions (name, value, type_of, account_id, date) VALUES
            ( '{transaction.name}',
            {transaction.value},
            '{transaction.type_of}',
            {transaction.account_id},
            '{transaction.date}');"""
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_transaction_id(self, name, account_id):
        """Get transaction id by name and account id"""
        self.cursor.execute(f"SELECT transaction_id FROM transactions WHERE name='{name}' and account_id='{account_id}'")
        return self.cursor.fetchone()

    def delete_transaction(self, transaction_id):
        """Delete a transaction by id"""
        self.cursor.execute(f"DELETE FROM transactions WHERE transaction_id={transaction_id}")
        self.conn.commit()

    def delete_transaction_by_acc_id(self, account_id ):
        """Delete all transactions from an account"""

        if account_id is None:
            raise NoAccountException("No account with this id")

        self.cursor.execute(f"DELETE FROM transactions WHERE account_id={account_id}")
        self.conn.commit()

    def get_transaction_by_acc_id(self, accid):
        """Get all transactions from an account"""
        if accid is None:
            raise NoAccountException("No account with this id")

        self.cursor.execute(f"SELECT * FROM transactions WHERE account_id={accid}")

        return self.cursor.fetchall()



class Transfer:
    """Transfer class"""
    def __init__(self, sender_acc_id, uuid_receiver, value, description):
        self.sender_acc_id = sender_acc_id
        self.uuid_receiver = str(uuid_receiver)
        self.value = value
        self.description = description

class TransferModel:
    """Model for the transfer table"""
    def __init__(self):
        self.conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432')
        self.acc_model = AccountModel()
        self.cursor = self.conn.cursor()
    def get_transfer_id(self, sender_acc_id, uuid_receiver, value):

        self.cursor.execute(f"SELECT transfer_id FROM transfers WHERE sender_acc_id={sender_acc_id} and receiver_uuid ='{uuid_receiver}' and value={value}")
        return from_list_to_int(self.cursor.fetchone())

    def execute_the_transfer(self, transfer_id):
        """Execute the actual transfer from one account to another"""
        actual_transfer = self.get_transfer_by_id(transfer_id)
        test = self.acc_model.get_account_balance(actual_transfer[1])
        self.acc_model.set_new_balance(test - actual_transfer[3], actual_transfer[1])
        balance = self.acc_model.get_account_by_uuid(actual_transfer[2])[2]
        balance = balance + actual_transfer[3]
        self.acc_model.update_balance_by_uuid(balance, actual_transfer[2])
        time = datetime.now().strftime("%d/%m/%Y")
        self.cursor.execute(f"""INSERT INTO transactions (name, value, date, type_of, account_id) VALUES
        ('transfer to another acc', -{actual_transfer[3]}, '{time}' ,
         'Transfer', '{actual_transfer[1]}' )""")
        self.cursor.execute(f"""INSERT INTO transactions (name, value, date, type_of, account_id) VALUES
        ('Transfer Received', {actual_transfer[3]},'{time}',
         'Transfer', '{self.acc_model.get_account_by_uuid(actual_transfer[2])[0]}' )""")
        self.conn.commit()

    def get_transfer_by_id(self, transfer_id):
        """Returns a transfer by its id"""

        self.cursor.execute(f"SELECT * FROM transfers WHERE transfer_id={transfer_id}")
        return self.cursor.fetchone()

    def create_transfer(self, transfer):
        """Creates a transfer"""

        if self.acc_model.get_uuid(transfer.sender_acc_id) == transfer.uuid_receiver:
            raise TransferToSameAccountException("You can't transfer to the same account")
        else:
            self.cursor.execute(f"INSERT INTO transfers (sender_acc_id, receiver_uuid, value,status,  description) VALUES ({transfer.sender_acc_id}, '{transfer.uuid_receiver}', {transfer.value},'pending', '{transfer.description}')")

            self.conn.commit()
            return self.cursor.lastrowid

    def approve_the_transfer(self, transfer_id):
        """Approves a transfer"""
        self.cursor.execute(f"UPDATE transfers SET status='approved' WHERE transfer_id={transfer_id}")
        self.execute_the_transfer(transfer_id)
        self.conn.commit()

    def delete_transfer(self, transfer_id):
        """Deletes a transfer"""
        self.cursor.execute(f"DELETE FROM transfers WHERE transfer_id = {transfer_id}")
        self.conn.commit()
