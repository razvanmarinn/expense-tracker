
from general.util import from_list_to_int, from_list_to_float, check_for_minus_or_plus, password_hashing, split_into_list, validate_credentials
from datetime import datetime
from src.models import User, UserModel, Transaction, TransactionModel, Account, AccountModel, TransferModel, Transfer
import pytest
from general.exceptions import TransferToSameAccountException


user_model = UserModel()
transaction_model = TransactionModel()
account_model = AccountModel()
transfer_model = TransferModel()

@pytest.fixture
def setup_test_data():
    user_model.create_user(User('sender', 'test'))
    acc = Account('sender_acc', 500, user_model.get_user_id_by_username("sender"))
    account_model.create_account(acc)
    user_model.create_user(User('receiver', 'test'))
    acc2 = Account('receive', 0 , user_model.get_user_id_by_username("receiver"))
    account_model.create_account(acc2)
    acc_id_receiver = account_model.get_account_id('receive', user_model.get_user_id_by_username("receiver"))
    uuid = account_model.get_uuid(acc_id_receiver)
    acc_id_sender = account_model.get_account_id('sender_acc', user_model.get_user_id_by_username("sender"))
    transfer_value = 250
    new_transfer = Transfer(acc_id_sender, uuid, transfer_value, "TEST")
    transfer_model.create_transfer(new_transfer)
    transfer_id = transfer_model.get_transfer_id(acc_id_sender, uuid, transfer_value)

    yield
    transaction_model.delete_transaction_by_acc_id(account_model.get_account_id('sender_acc', user_model.get_user_id_by_username("sender")))
    transaction_model.delete_transaction_by_acc_id(account_model.get_account_id('receive' , user_model.get_user_id_by_username("receiver")))
    account_model.delete_account('sender_acc', user_model.get_user_id_by_username("sender"))
    account_model.delete_account('receive', user_model.get_user_id_by_username("receiver"))
    user_model.delete_user_by_username('sender')
    user_model.delete_user_by_username('receiver')
    transfer_model.delete_transfer(transfer_id)

def test_create_users(setup_test_data):
    user1 = user_model.get_user_by_username("sender")
    user2 = user_model.get_user_by_username("receiver")
    assert user1 is not None
    assert user2 is not None

def test_uuid(setup_test_data):
    acc_id_receiver = account_model.get_account_id('receive', user_model.get_user_id_by_username("receiver"))
    uuid = account_model.get_uuid(acc_id_receiver)
    assert len(uuid) == 36


def test_create_accounts(setup_test_data):
    acc_id_sender = account_model.get_account_id('sender_acc', user_model.get_user_id_by_username("sender"))
    acc_id_receiver = account_model.get_account_id('receive', user_model.get_user_id_by_username("receiver"))
    assert acc_id_sender is not None
    assert acc_id_receiver is not None
    assert account_model.get_account_balance(acc_id_sender) == 500
    assert account_model.get_account_balance(acc_id_receiver) == 0

def test_transfer_between_users(setup_test_data):
    acc_id_sender = account_model.get_account_id('sender_acc', user_model.get_user_id_by_username("sender"))
    acc_id_receiver = account_model.get_account_id('receive', user_model.get_user_id_by_username("receiver"))
    uuid = account_model.get_uuid(acc_id_receiver)
    transfer_value = 250
    transfer_id = transfer_model.get_transfer_id(acc_id_sender, uuid, transfer_value)
    transfer_model.execute_the_transfer(transfer_id)
    assert account_model.get_account_balance(acc_id_sender) == 250
    assert account_model.get_account_balance(acc_id_receiver) == 250
    assert transaction_model.get_transaction_by_acc_id(acc_id_sender) is not None
    assert transaction_model.get_transaction_by_acc_id(acc_id_receiver) is not None


def test_approve_transfer(setup_test_data):
    acc_id_receiver = account_model.get_account_id('receive', user_model.get_user_id_by_username("receiver"))
    uuid = account_model.get_uuid(acc_id_receiver)
    acc_id_sender = account_model.get_account_id('sender_acc', user_model.get_user_id_by_username("sender"))
    transfer_value = 250
    transfer_id = transfer_model.get_transfer_id(acc_id_sender, uuid, transfer_value)
    transfer_model.approve_the_transfer(transfer_id)
    assert account_model.get_account_balance(acc_id_sender) == 250
    assert account_model.get_account_balance(acc_id_receiver) == 250
    assert transaction_model.get_transaction_by_acc_id(acc_id_sender) is not None
    assert transaction_model.get_transaction_by_acc_id(acc_id_receiver) is not None


def test_transfer_between_same_user(setup_test_data):
   with pytest.raises(TransferToSameAccountException):
        acc_id_receiver = account_model.get_account_id('receive', user_model.get_user_id_by_username("receiver"))
        uuid = account_model.get_uuid(acc_id_receiver)
        transfer_value = 2150
        new_transfer = Transfer(acc_id_receiver, uuid, transfer_value, "TEST")
        transfer_model.create_transfer(new_transfer)



def test_retreive_user_from_db():
    user_model.create_user(User('test_user', 'test_user'))
    assert len(user_model.get_user_by_username('test_user')) > 0
    assert user_model.get_user_by_username('test_user')[1] and user_model.get_user_by_username('test_user')[2] == 'test_user'
    user_model.delete_user_by_username('test_user')
    assert user_model.get_user_by_username('test_user') == None


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


def test_split_into_strings():

    result = split_into_list( "test hello asd" )
    assert result == ['test', 'hello', 'asd']
    assert result[0] == 'test'

def test_validate_password():
    test_pass_hashed = password_hashing("test_pass")
    assert validate_credentials("test_pass", test_pass_hashed) == True










