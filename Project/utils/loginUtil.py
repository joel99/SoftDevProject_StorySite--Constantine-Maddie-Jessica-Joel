import hashlib, sqlite3
import loginDBUtil

#given login information, check database
def isValidLogin(userName, password):
    hashedPass = hashlib.sha512(password).hexdigest()
    return loginDBUtil.isValidAccountInfo(userName, hashedPass)

def getUserID(username):
    return loginDBUtil.getUserID(username)
    
#making new account
def isValidRegister(pass1, pass2, username):
    #also do database checks
    return pass1 == pass2 and (not loginDBUtil.doesUserExist(username))

def register(username, password):
    hashedPass = hashlib.sha512(password).hexdigest()
    return loginDBUtil.registerAccountInfo(username, hashedPass)
