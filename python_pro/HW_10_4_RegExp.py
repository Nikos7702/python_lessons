import re

def validate_login(login):
    pattern = r'^[A-Za-z0-9]{2,10}$'
    return re.search(pattern, login)

login = "mylogin123"
if validate_login(login):
    print("Login accepted")
else:
    print("Try another")
