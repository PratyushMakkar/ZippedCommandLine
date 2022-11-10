import os

def ReturnUsernameAndPassword():
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    return username, password

def SetUsernameAndPassword(username, password):
    os.environ['USERNAME'] = str(username)
    os.environ['PASSWORD'] = str(password)
   
    