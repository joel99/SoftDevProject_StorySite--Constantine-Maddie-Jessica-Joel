from flask import Flask, request, session
import hashlib, sqlite3
import loginDBUtil

#given login information, check database
def isValidLogin(userName, password):
    hashedPass = hashlib.sha512(password).hexDigest()
    return loginDBUtil.isValidAccountInfo(userName, hashedPass)
    #return True

def getUserID(userName):
    return loginDBUtil.getUserID(username)
    
#making new account
def isValidRegister(pass1, pass2, username):
    return True
    #return pass1 == pass2 

def register(username, password):
    print("registering")
    hashedPass = hashlib.sha512(password).hexDigest()
    return loginDBUtil.registerAccountInfo(username, hashedPass)
