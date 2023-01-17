import bcrypt

def passwordHashing(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14)).decode('utf-8')

def validateCredentials(password, password_hash):
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))


def from_list_to_int(string):
    if string is None:
        return None
    res = ""
    for i in string:
        if len(res) > 1:
            break
        res +=str(i)
    return int(res)

def from_list_to_str(string):
    if string is None:
        return None
    res = ""
    for i in string:
        if len(res) > 1:
            break
        res +=str(i)
    return res

def from_list_to_float(string):
    res = "".join(str(i) for i in string)
    return float(res)

def check_for_minus_or_plus(string):
    if string == None:
        return None
    if type(string) in [int, float]:
        return "+" if string > 0 else "-"
    return "-" if string[0] == "-" else "+"

def splitIntoList(string): # to be modified
    if string == None:
        return None
    return string.split(" ", 3)


