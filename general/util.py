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
        res += str(i)
    return int(res)


def from_list_to_str(string):
    """Converts components of the  list to a string"""
    if string is None:
        return None
    res = ""
    for i in string:
        if len(res) > 1:
            break
        res += str(i)
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
    actual_element = split_into_list(user_data)
    if actual_element is not None:
        acc_window.cb_dropdown.addItems(actual_element)


def make_api_get_request(endpoint_url, headers):
    """Makes an api request"""
    response = requests.get(endpoint_url, headers=headers, timeout=600)
    return response.json()


def make_api_post_request(endpoint_url, headers):
    """Makes an api request"""
    response = requests.post(endpoint_url, headers=headers, timeout=600)
    return response.json()


def make_api_delete_request(endpoint_url, headers):
    """Makes an api request"""
    requests.delete(endpoint_url, headers=headers, timeout=600)
    return "OK"


def make_api_put_request(endpoint_url, headers):
    """Makes an api request"""
    response = requests.put(endpoint_url, headers=headers, timeout=600)
    return response.json()


def update_env_file(key, value):
    """Updates the .env file"""
    with open('.env', 'r', encoding=None) as file:
        lines = file.readlines()

    with open('.env', 'w', encoding=None) as file:
        for line in lines:
            if line.startswith(key):
                line = f'{key}={value}\n'
            file.write(line)


def check_email_format(email: str):
    """Checks if the email is valid"""
    assert email.count("@") == 1, "Email must contain only one @ sign"
    assert email.count(".") >= 1, "Email must contain at least one dot"
    assert email.index("@") < email.index("."), "Email must contain a dot after the @ sign"
    return True


def check_phone_number_format(phone_number: str):
    """Checks if the phone number is valid"""
    assert len(phone_number) == 10, "Phone number must be 10 digits long"
    assert phone_number.isnumeric(), "Phone number must contain only digits"
    return True
