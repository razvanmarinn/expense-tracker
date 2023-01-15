from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime
import bcrypt
from templates.Util import from_list_to_int, from_list_to_float, check_for_minus_or_plus
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
