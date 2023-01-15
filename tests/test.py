
import sqlite3
from templates.Util import from_list_to_int, from_list_to_float, check_for_minus_or_plus, passwordHashing, splitIntoList, validateCredentials
from datetime import datetime
from templates.Models import User, UserModel, Transaction, TransactionModel, Account, AccountModel, TransferModel, Transfer

user_model = UserModel()
transaction_model = TransactionModel()
account_model = AccountModel()
transfer_model = TransferModel()




def test_retreive_user_from_db():
    user_model.create_user(User('test_user', 'test_user'))
    assert len(user_model.get_user_by_username('test_user')) > 0
    assert user_model.get_user_by_username('test_user')[1] and user_model.get_user_by_username('test_user')[2] == 'test_user'
    user_model.delete_user_by_username('test_user')
    assert user_model.get_user_by_username('test_user') == None


# def test_add_transaction_with_plus():

#     value_with_plus = 100

#     dummy_acc =Account("test", 0, user_id)

#     account_model.create_account(dummy_acc)
#     account_id = account_model.get_account_id("test", user_id)

#     #account_id_int = from_list_to_int(account_id)
#     assert account_id == 999

#     dt_string = datetime.now().strftime("%d/%m/%Y")
#     res_int = account_model.get_account_balance(account_id)

#     #res_int = from_list_to_float(res)

#     assert res_int == 0

#     res_int = res_int + float(value_with_plus)

#     assert res_int == 100
#     dummy_transaction = Transaction("test_transaction", value_with_plus, dt_string, 'test', account_id, 999)
#     transaction_model.create_transaction(dummy_transaction)
#     transaction_id = transaction_model.get_transaction_id("test_transaction", 999)
#     account_model.set_new_balance(res_int, account_id) ## TEST ALSO THE NEW BALANCE
#     account_model.delete_account(account_id)
#     transaction_model.delete_transaction(transaction_id)


def test_check_for_minus_or_plus():
    assert check_for_minus_or_plus(None) == None
    assert check_for_minus_or_plus(100) == "+"
    assert check_for_minus_or_plus(-100) == "-"
    assert check_for_minus_or_plus("100") == "+"
    assert check_for_minus_or_plus("-100") == "-"



def test_from_list_to_int():
    assert from_list_to_int(None) == None
    assert from_list_to_int([1]) == 1
    assert from_list_to_int([12, 3]) == 12



# def test_create_user_account():

#     db = sqlite3.connect("expense_tracker.db")
#     db_cursor = db.cursor()
#     db_cursor.execute("SELECT username from users WHERE username = :username",
#     {'username': "test_user999"})
#     result = db_cursor.fetchone()
#     if result is None:
#         hashed_pass = passwordHashing("test_password")
#         db_cursor.execute("INSERT INTO users (username, password )VALUES (:username, :password)",
#             {
#                 'username': "test_user999",
#                 'password': hashed_pass
#             }
#         )
#     db_cursor.execute(""" SELECT username, password from users WHERE username = "test_user999" """)
#     temp_result = db_cursor.fetchone()

#     assert temp_result[0] == "test_user999"
#     assert temp_result[1] == hashed_pass

#     db_cursor.execute("""DELETE FROM users WHERE username = "test_user999" """)

#     db.commit()
#     db_cursor.close()


def test_split_into_strings():

    result = splitIntoList( "test hello asd" )
    assert result == ['test', 'hello', 'asd']
    assert result[0] == 'test'


def test_validate_password():
    test_pass_hashed = passwordHashing("test_pass")
    assert validateCredentials("test_pass", test_pass_hashed) == True


def test_create_and_count_accounts():
    user_model.create_user(User("test_user2", "test_password"))

    id = user_model.get_user_id_by_username("test_user2")

    account_model.create_account(Account("test", 5 , id))

    acc_id = account_model.get_account_id("test", id)
    balance = account_model.get_account_balance(acc_id)
    assert balance == 5.0
    result = account_model.count_accounts(id)
    assert result == 1
    account_model.delete_account('test',id)
    user_model.delete_user_by_username('test_user2')
    assert user_model.get_user_by_username('test_user2') == None
    assert account_model.get_account_id("test", id) == None







def test_transfer_between_users():
    try:
        value = 250
        user_model.create_user(User('sender', 'test'))
        acc = Account('sender_acc', 500, user_model.get_user_id_by_username("sender"))
        account_model.create_account(acc)
        user_model.create_user(User('receiver', 'test'))
        acc2 = Account('receive', 0 , user_model.get_user_id_by_username("receiver"))
        account_model.create_account(acc2)
        acc_id_receiver = account_model.get_account_id('receive',user_model.get_user_id_by_username("receiver") )
        acc_id_sender = account_model.get_account_id('sender_acc', user_model.get_user_id_by_username("sender"))

        iban = account_model.get_iban(acc_id_receiver)

        new_transfer = Transfer(acc_id_sender, iban, value, "TEST")
        transfer_model.create_transfer(new_transfer)
        assert account_model.get_account_balance(acc_id_sender) == 250
        assert account_model.get_account_balance(acc_id_receiver) == 250

    finally:
        transaction_model.delete_transaction_by_acc_id(user_model.get_user_id_by_username("sender"))
        transaction_model.delete_transaction_by_acc_id(user_model.get_user_id_by_username("receiver"))
        account_model.delete_account('sender_acc', user_model.get_user_id_by_username("sender"))
        account_model.delete_account('receive', user_model.get_user_id_by_username("receiver"))
        user_model.delete_user_by_username('sender')
        user_model.delete_user_by_username('receiver')

