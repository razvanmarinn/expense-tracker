import sqlite3

db = sqlite3.connect("expense_tracker.db")
d = db.cursor()

def create_table_users():
    d.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL, password TEXT NOT NULL)""")

def add_Values():
    d.execute("""INSERT INTO users(username, password) VALUES('asd','asd');""")
    db.commit()
def create_table_accounts():
    d.execute("""CREATE TABLE accounts_test (accounts_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT , balance REAL,userid INTEGER, FOREIGN KEY(userid) REFERENCES users(id))""")
def create_transaction_table():
    d.execute("""CREATE TABLE transactions (transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT , balance REAL, value REAL,date TEXT, account_id INTEGER, FOREIGN KEY(account_id) REFERENCES accounts_test(accounts_id))""")

create_transaction_table()