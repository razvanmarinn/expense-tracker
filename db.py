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
    cursor.execute("CREATE TABLE accounts_test (accounts_id SERIAL PRIMARY KEY, name TEXT , balance INT ,iban character varying(34) NOT NULL, userid INT, CONSTRAINT fk_user FOREIGN KEY(userid) REFERENCES users(id))")
def create_transaction_table():
    cursor.execute("CREATE TABLE transactions (transaction_id SERIAL PRIMARY KEY, name TEXT , value float ,date date, type_of TEXT , account_id INT,CONSTRAINT fk_account FOREIGN KEY(account_id) REFERENCES accounts_test(accounts_id))")
def create_transfers_table():
    cursor.execute("CREATE TABLE transfers (transfer_id SERIAL PRIMARY KEY , sender_acc_id INT, receiver_iban character varying(34) NOT NULL, value INT, description TEXT)")
create_transaction_table()

