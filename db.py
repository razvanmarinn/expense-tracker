import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

def set_pragma():
    cursor.execute("""PRAGMA encoding="UTF-8";""")
def create_table_users():
    cursor.execute("""CREATE TABLE users (ID  SERIAL PRIMARY KEY,username TEXT NOT NULL, password bytea NOT NULL)""")

def add_Values():
    cursor.execute("INSERT INTO users(username, password) VALUES('asd','asd');")()
def create_table_accounts():
    cursor.execute("CREATE TABLE accounts_test (accounts_id SERIAL PRIMARY KEY, name TEXT , balance INT ,userid INT, CONSTRAINT fk_user FOREIGN KEY(userid) REFERENCES users(id))")
def create_transaction_table():
    cursor.execute("CREATE TABLE transactions (transaction_id SERIAL PRIMARY KEY, name TEXT , balance INT, value float ,date TEXT, type_of TEXT , account_id INT,CONSTRAINT fk_account FOREIGN KEY(account_id) REFERENCES accounts_test(accounts_id))")

create_transaction_table()

