from mega import Mega

mega = Mega()

def ask_login():
    print('Enter your user:')
    user = input()
    print('Enter your password:')
    pwd = input()
    return [user,pwd]

cred = ask_login()

m = mega.login(cred[0], cred[1])