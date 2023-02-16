"""This module contains general functions that are used in the project"""
import requests
from general.headers import headers

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



def add_drop_down_items(userid, acc_window):
    """Adds the items to the drop down menu"""
    endpoint_url = "http://{}:{}/accounts/get_accounts_name/{}".format("127.0.0.1", "8000", userid)
    user_data = make_api_get_request(endpoint_url, headers=headers)
    #element = acc_window.account_model.get_name_of_acc(acc_window.user.id) # NAMES OF THE ACCOUNTS
    actual_element = split_into_list(user_data) # ACTUAL_ELEMENT
    if actual_element is not None:
       acc_window.cb_dropdown.addItems(actual_element)


def make_api_get_request(endpoint_url , headers):
    """Makes an api request"""
    response = requests.get(endpoint_url, headers=headers)
    return response.json()

def make_api_post_request(endpoint_url, headers):
    """Makes an api request"""
    response = requests.post(endpoint_url, headers=headers)
    return response.json()

def make_api_delete_request(endpoint_url, headers):
    """Makes an api request"""
    response = requests.delete(endpoint_url, headers=headers)
    return "OK"

def update_env_file(key, value):
    with open('.env', 'r') as file:
        lines = file.readlines()

    with open('.env', 'w') as file:
        for line in lines:
            if line.startswith(key):
                line = f'{key}={value}\n'
            file.write(line)