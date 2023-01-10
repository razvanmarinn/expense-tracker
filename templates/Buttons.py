from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime
import time
import bcrypt
from templates.Util import passwordHashing, pass_id_to_acc_tab, from_list_to_int, from_list_to_float, check_for_minus_or_plus
import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port= '5432'
)
cursor = conn.cursor()
conn.autocommit = True


salt = bcrypt.gensalt()

class Button(ABC):
    @abstractmethod
    def functionality(self):
        pass

class AddAccButton(Button):
    """Add an account to a user"""
    def __init__(self, Accpop):
        self.accpop = Accpop

    def functionality(self):
        db = sqlite3.connect("expense_tracker.db")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT count(*) FROM accounts_test WHERE userid = :id", {'id': self.accpop.accwindow.current_acc_id})
        result = db_cursor.fetchone()
        no_of_acc = from_list_to_int(result)
        if no_of_acc >= self.accpop.accwindow.max_accounts_per_user:
            print("max accs")
        else:
            db_cursor.execute("INSERT INTO accounts_test (name,balance,userid) VALUES (:name,:balance,:id)",
            {'name' : self.accpop.le_accountname.text(),
            'balance': int(self.accpop.le_budgetname.text()),
            'id': self.accpop.accwindow.current_acc_id
            } )
            db_cursor.execute("SELECT accounts_id FROM accounts_test WHERE name = :name",
            {'name': self.accpop.le_accountname.text()
            })
            account_id = db_cursor.fetchone()
            account_id_int = from_list_to_int(account_id)

            curdate = datetime.now()
            dt_string = curdate.strftime("%d/%m/%Y")

            db_cursor.execute("INSERT INTO transactions (name, balance, value, account_id, date) VALUES (:name,:balance, :value ,:id , :date)",
            { 'name' : "init",
            'balance': int(self.accpop.le_budgetname.text()),
            'value': int(self.accpop.le_budgetname.text()),
            'id': account_id_int,
            'date': dt_string
            } )

            self.accpop.accwindow.cb_dropdown.addItem(self.accpop.le_accountname.text())
            db.commit()
            self.accpop.accwindow.create_new()
            self.accpop.hide()


class RemoveAccButton(Button):
    """Remove an accounts of user"""
    def __init__(self, AccWindow):
        self.AccWindow = AccWindow

    def functionality(self):
        db = sqlite3.connect("expense_tracker.db")
        db_cursor = db.cursor()
        if self.AccWindow.actual_element[0] == "":
            print("No accounts to be removed")
        else:
            db_cursor.execute("DELETE FROM accounts_test WHERE name =:name", {'name': self.AccWindow.cb_dropdown.currentText()})
            print(self.AccWindow.current_account_id)
            db_cursor.execute("DELETE FROM transactions WHERE account_id = :account_id", {'account_id': self.AccWindow.current_account_id})
            # currentTextChanged signal will pass selected text to slot
            curr_index = self.AccWindow.cb_dropdown.currentIndex()
            self.AccWindow.cb_dropdown.removeItem(curr_index)  # remove item from index
            db.commit()
            self.AccWindow.create_new()


class AddTransaction(Button):
    """Add an transaction to a specific account of a user"""
    def __init__(self, TransPopup):
        self.TransPopup = TransPopup

    def functionality(self):
        db = sqlite3.connect("expense_tracker.db")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT accounts_id FROM accounts_test WHERE name = :name AND userid = :userid" ,
        {'name': self.TransPopup.cb_accounts.currentText(),
        'userid': self.TransPopup.AccWindow.current_acc_id
        })
        account_id = db_cursor.fetchone()
        account_id_int = from_list_to_int(account_id)

        curdate = datetime.now()
        dt_string = curdate.strftime("%d/%m/%Y")

        db_cursor.execute(
            "SELECT balance FROM accounts_test WHERE accounts_id = :accid",
            {'accid': account_id_int})
        res = db_cursor.fetchone()
        res_int = from_list_to_float(res)
        sign = check_for_minus_or_plus(self.TransPopup.le_value.text())
        if sign == "-":
            res_int = res_int - (-1 * float(self.TransPopup.le_value.text()))
        else:
            res_int = res_int + float(self.TransPopup.le_value.text())

        db_cursor.execute("INSERT INTO transactions (name, balance, value, date, type_of , account_id )VALUES (:name, :balance, :value, :date , :type_of , :account_id)",
            {
                'name': self.TransPopup.le_nume.text(),
                'value': self.TransPopup.le_value.text(),
                'balance': res_int,
                'account_id': account_id_int,
                'date': dt_string,
                'type_of':self.TransPopup.cb_typeoftacc.currentText()
            } )
        db_cursor.execute("UPDATE accounts_test SET balance = :new_budget WHERE accounts_id = :accid", {'accid': account_id_int, 'new_budget': res_int})

        db.commit()
        self.TransPopup.AccWindow.create_new()
        self.TransPopup.hide()


class LoginButton(Button):
    """Login into account"""
    def __init__(self, login_form):
        self.login_form = login_form
    def functionality(self):


        cursor.execute(
            f"SELECT password FROM users WHERE username = '{self.login_form.le_username.text()}'"
        )

        temp = cursor.fetchall()
        if (len(temp) == 0):
            self.login_form.l_loggedin.setText("Username doesn't exist")
        else:
            temp2 = "".join(temp[0])
            if bcrypt.checkpw(self.login_form.le_password.text().encode('utf-8') , bytes(temp2 , 'utf-8')):
                self.login_form.l_loggedin.setText("Logged in")
                pass_id_to_acc_tab(self.login_form)

                time.sleep(2)
                self.login_form.switch_to_accounts()
            else:
                self.login_form.l_loggedin.setText("Password is not matching")

        conn.commit()

class CreateUserAcc(Button):
    """Create the user account and encrypt the password using BCRYPT"""
    def __init__(self, login_form):
        self.login_form = login_form
    def functionality(self):
        cursor.execute(
            f"SELECT username from users WHERE username = '{self.login_form.le_username.text()}';"
        )

        result = cursor.fetchone()
        if result is None:
            hashed_pass = passwordHashing(self.login_form.le_password.text())
            print(hashed_pass)
            cursor.execute(
                f"INSERT INTO users (username, password )VALUES ('{self.login_form.le_username.text()}', '{hashed_pass}');"
            )

            self.login_form.l_loggedin.setText("Account created")

        else:
            self.login_form.l_loggedin.setText("username already exists")

        conn.commit()

class AddRecTransaction(Button):
    """Add a recurring transactions which occurs every n of days."""
    def __init__(self, RecTrPopup):
        self.RecTrPopup = RecTrPopup

    def functionality(self): # TO BE MODIFIED

        db = sqlite3.connect("expense_tracker.db") #
        db_cursor = db.cursor()
        db_cursor.execute("SELECT accounts_id FROM accounts_test WHERE name = :name AND userid = :userid" ,
        {'name': self.RecTrPopup.cb_accounts.currentText(),
        'userid': self.RecTrPopup.AccWindow.current_acc_id
        })
        account_id = db_cursor.fetchone()
        account_id_int = from_list_to_int(account_id)

        db_cursor.execute("SELECT balance FROM accounts_test WHERE accounts_id = :accid", {'accid': account_id_int})
        res = db_cursor.fetchone()
        res_int = from_list_to_float(res)
        sign = check_for_minus_or_plus(self.RecTrPopup.le_value.text())
        if(sign == "-"):
            res_int = res_int - (-1 * float(self.RecTrPopup.le_value.text()))
        else:
            res_int = res_int + float(self.RecTrPopup.le_value.text())

        start_date = self.RecTrPopup.de_startdate.date()
        actual_start_date = start_date.toPyDate()

        db_cursor.execute("INSERT INTO transactions (name, balance, value, date, account_id )VALUES (:name, :balance, :value, :date , :account_id)",
        {
            'name': self.RecTrPopup.le_name.text(),
            'value': self.RecTrPopup.le_value.text(),
            'balance': res_int,
            'account_id': account_id_int,
            'date': actual_start_date
        } )




        end_date = self.RecTrPopup.de_enddate.date()
        actual_end_date = end_date.toPyDate()
        curdate = datetime.now()
        dt_string = curdate.strftime("%d/%m/%Y")


        while dt_string != actual_end_date:
            db_cursor.execute("INSERT INTO transactions (name, balance, value, date, account_id )VALUES (:name, :balance, :value, :date , :account_id)",
            {
                'name': self.RecTrPopup.le_name.text(),
                'value': self.RecTrPopup.le_value.text(),
                'balance': res_int,
                'account_id': account_id_int,
                'type_of':self.RecTrPopup.cb_accounts.currentText(),
                'date': curdate
            } )

        db_cursor.execute("UPDATE accounts_test SET balance = :new_budget WHERE accounts_id = :accid", {'accid': account_id_int, 'new_budget': res_int})

        db.commit()
        self.RecTrPopup.AccWindow.create_new()
        self.RecTrPopup.hide()