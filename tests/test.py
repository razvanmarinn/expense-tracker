
import sqlite3
from templates.Util import from_list_to_int, from_list_to_float, check_for_minus_or_plus, passwordHashing, splitIntoList, validateCredentials
from datetime import datetime
from templates.User import User, UserModel

user_model = UserModel()

def test_retreive_user_from_db():
    user = User('test_user', 'test_user')
    user_model.create_user(user)
    result = user_model.get_user_by_username('test_user')
    assert len(result) > 0
    assert result[1] and result[2] == 'test_user'
    user_model.delete_user_by_username('test_user')
    user_model.close_connection()

def test_add_transaction_with_plus():

    value_with_plus = 100

    db = sqlite3.connect("expense_tracker.db")
    db_cursor = db.cursor()
    db_cursor.execute(" INSERT INTO accounts_test(accounts_id, name, balance, userid) VALUES(900, 'test', 0, 999); ")
    db_cursor.execute("""SELECT accounts_id FROM accounts_test WHERE name = "test" AND userid = 999""" )
    account_id = db_cursor.fetchone()

    account_id_int = from_list_to_int(account_id)
    assert account_id_int == 900

    curdate = datetime.now()
    dt_string = curdate.strftime("%d/%m/%Y")
    db_cursor.execute( "SELECT balance FROM accounts_test WHERE accounts_id = :accid",

    {'accid': account_id_int})

    res = db_cursor.fetchone()

    res_int = from_list_to_float(res)

    assert res_int == 0

    res_int = res_int + float(value_with_plus)

    assert res_int == 100

    db_cursor.execute("INSERT INTO transactions (name, balance, value, date, type_of , account_id )VALUES (:name, :balance, :value, :date , :type_of , :account_id)",

    {

    'name': "test_transaction",

    'value': value_with_plus,

    'balance': res_int,

    'account_id': account_id_int,

    'date': dt_string,

    'type_of': "Test"

    } )

    db_cursor.execute("UPDATE accounts_test SET balance = :new_budget WHERE accounts_id = :accid", {'accid': account_id_int, 'new_budget': res_int})
    db_cursor.execute("DELETE FROM accounts_test WHERE accounts_id = 900")
    db_cursor.execute("DELETE FROM transactions WHERE name = 'test_transaction'")
    db.commit()
    db_cursor.close()


def test_add_transaction_with_minus():


        value_with_minus = -100


        db = sqlite3.connect("expense_tracker.db")
        db_cursor = db.cursor()
        db_cursor.execute(" INSERT INTO accounts_test(accounts_id, name, balance, userid) VALUES(900, 'test', 0, 999); ")
        db_cursor.execute("""SELECT accounts_id FROM accounts_test WHERE name = "test" AND userid = 999""" )
        account_id = db_cursor.fetchone()

        account_id_int = from_list_to_int(account_id)
        assert account_id_int == 900

        curdate = datetime.now()
        dt_string = curdate.strftime("%d/%m/%Y")
        db_cursor.execute( "SELECT balance FROM accounts_test WHERE accounts_id = :accid",

        {'accid': account_id_int})

        res = db_cursor.fetchone()

        res_int = from_list_to_float(res)

        assert res_int == 0

        res_int = res_int + float(value_with_minus)

        assert res_int == -100

        db_cursor.execute("INSERT INTO transactions (name, balance, value, date, type_of , account_id )VALUES (:name, :balance, :value, :date , :type_of , :account_id)",
        {
        'name': "test_transaction",
        'value': value_with_minus,
        'balance': res_int,
        'account_id': account_id_int,
        'date': dt_string,
        'type_of': "Test"
        } )

        db_cursor.execute("SELECT name, balance, value, date, type_of , account_id FROM transactions WHERE name = 'test_transaction' ")
        temp = db_cursor.fetchall()

        assert temp[0] == ('test_transaction', -100.0, -100.0, dt_string, 'Test', 900)

        db_cursor.execute("UPDATE accounts_test SET balance = :new_budget WHERE accounts_id = :accid", {'accid': account_id_int, 'new_budget': res_int})
        db_cursor.execute("DELETE FROM accounts_test WHERE accounts_id = 900")
        db_cursor.execute("DELETE FROM transactions WHERE name = 'test_transaction'")
        db.commit()
        db_cursor.close()


def test_check_for_minus_or_plus():
    assert check_for_minus_or_plus(100) == "+"
    assert check_for_minus_or_plus(-100) == "-"
    assert check_for_minus_or_plus("100") == "+"
    assert check_for_minus_or_plus("-100") == "-"
    assert check_for_minus_or_plus("100.0") == "+"
    assert check_for_minus_or_plus("-100.0") == "-"


def test_from_list_to_int():
    assert from_list_to_int([1]) == 1
    assert from_list_to_int([12]) == 12
    assert from_list_to_int([12, 3]) == 12
    assert from_list_to_int([12, 3, 4]) == 12



def test_create_user_account():

    db = sqlite3.connect("expense_tracker.db")
    db_cursor = db.cursor()
    db_cursor.execute("SELECT username from users WHERE username = :username",
    {'username': "test_user999"})
    result = db_cursor.fetchone()
    if result is None:
        hashed_pass = passwordHashing("test_password")
        db_cursor.execute("INSERT INTO users (username, password )VALUES (:username, :password)",
            {
                'username': "test_user999",
                'password': hashed_pass
            }
        )
    db_cursor.execute(""" SELECT username, password from users WHERE username = "test_user999" """)
    temp_result = db_cursor.fetchone()

    assert temp_result[0] == "test_user999"
    assert temp_result[1] == hashed_pass

    db_cursor.execute("""DELETE FROM users WHERE username = "test_user999" """)

    db.commit()
    db_cursor.close()


def test_split_into_strings():

    result = splitIntoList( "test hello asd" )
    assert result == ['test', 'hello', 'asd']
    assert result[0] == 'test'


def test_validate_credentials():
    test_pass_hashed = passwordHashing("test_pass")
    assert validateCredentials("test_pass", test_pass_hashed) == True


def test_get_name_of_acc_transaction():
        db = sqlite3.connect("expense_tracker.db")
        db_cursor= db.cursor()
        db_cursor.execute("INSERT INTO accounts_test(accounts_id, name, balance, userid) VALUES(900, 'test', 0, 999); ")
        db_cursor.execute("SELECT name FROM accounts_test WHERE userid = :id",
        {
            'id': 999

        })
        result = db_cursor.fetchall()
        #print(result)
        str_result = "".join(map(str, result)).replace("'", "").replace("(", "").replace(")", "").replace(",", "")
        assert str_result == "test"
        db_cursor.execute("DELETE FROM accounts_test WHERE accounts_id = 900 and userid = 999")
        db.commit()
        db_cursor.close()


def test_count_current_nr_of_acs():
        db = sqlite3.connect("expense_tracker.db")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT count(*) FROM accounts_test WHERE userid = :id", {'id': 999})
        count = db_cursor.fetchone()

        noOfAcc = from_list_to_int(count)
        assert noOfAcc == 0

        db_cursor.execute("INSERT INTO accounts_test(accounts_id, name, balance, userid) VALUES(900, 'test', 0, 999); ")
        db_cursor.execute("INSERT INTO accounts_test(accounts_id, name, balance, userid) VALUES(901, 'test2', 1, 999); ")
        db_cursor.execute("INSERT INTO accounts_test(accounts_id, name, balance, userid) VALUES(902, 'test3', 2, 999); ")

        db_cursor.execute("SELECT count(*) FROM accounts_test WHERE userid = :id", {'id': 999})
        count = db_cursor.fetchone()
        noOfAcc = from_list_to_int(count)
        assert noOfAcc == 3
        db_cursor.execute("DELETE FROM accounts_test WHERE accounts_id = 900 and userid = 999")
        db_cursor.execute("DELETE FROM accounts_test WHERE accounts_id = 901 and userid = 999")
        db_cursor.execute("DELETE FROM accounts_test WHERE accounts_id = 902 and userid = 999")
        db.commit()
        db_cursor.close()
