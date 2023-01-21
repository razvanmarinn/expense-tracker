"""This module contains general functions that are used in the project"""
import bcrypt

def password_hashing(password):
    """Hashes the password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14)).decode('utf-8')

def validate_credentials(password, password_hash):
    """Validates the credentials"""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))


def from_list_to_int(string):
    """Converts components of the  list to an integer"""
    if string is None:
        return None
    res = ""
    for i in string:
        if len(res) > 1:
            break
        res +=str(i)
    return int(res)

def from_list_to_str(string):
    """Converts components of the  list to a string"""
    if string is None:
        return None
    res = ""
    for i in string:
        if len(res) > 1:
            break
        res +=str(i)
    return res

def from_list_to_float(string):
    """Converts components of the  list to a float"""
    if string is None:
        return None
    res = "".join(str(i) for i in string)
    return float(res)

def check_for_minus_or_plus(string):
    """Checks if the string has a minus or plus sign"""
    if string is None:
        return None
    if type(string) in [int, float]:
        return "+" if string > 0 else "-"
    return "-" if string[0] == "-" else "+"

def split_into_list(string):
    """Splits a string into a list"""
    if string is None:
        return None
    return [x for x in string.split(" ") if x != ""]



def add_drop_down_items(acc_window):
    element = acc_window.account_model.get_name_of_acc(acc_window.current_user_id) # NAMES OF THE ACCOUNTS
    acc_window.actual_element = split_into_list(element) # ACTUAL_ELEMENT
    if acc_window.actual_element is not None:
        acc_window.cb_dropdown.addItems(acc_window.actual_element)
