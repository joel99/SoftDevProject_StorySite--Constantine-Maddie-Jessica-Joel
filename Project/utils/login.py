from flask import Flask, request, session, url_for, redirect
import hashlib, sqlite3

#given login information, check database
def isValidLogin(userName, password):
    hashedPass = hashlib.sha512(password)
    return isInDatabase(userName, hashedPass)
    
#making new account
def isValidRegister(pass1, pass2, username):
    return pass1 == pass2 and len(username) > 0 and len(pass1) > 0
