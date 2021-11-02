def check_email(string):
    if ' ' in string:
        return False
    elif '@' not in string:
        return False
    elif '@.' in string:
        return False
    elif string.find('.', string.find('@')) == -1:
        return False
    return True
