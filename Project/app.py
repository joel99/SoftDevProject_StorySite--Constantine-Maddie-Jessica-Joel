from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "secrets"

@app.route("/") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def root():
    if "user" in session:#if logged in
        return render_template('home.html', usr = session["user"])
    else:#if not logged in
        return render_template('login.html')

@app.route("/login") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def login():
    d = request.form
    if isValidLogin(d["username"], d["pass"]):
        session["user"] = d["username"]
    return redirect(url_for('root'))

@app.route("/register") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def register():
    d = request.form
    if isValidRegister(d["pass1"], d["pass2"], d["username"]):
        writeToAccountInfo(d)
        writeToPeople(d)
        session["user"] = d["userName"]
    return redirect(url_for('home'))

@app.route('/<string:username>') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def userPage(username):
    d = request.form
    if "newPost" in request.args:
        # CODE TO PUT FORM INFO INTO DB
        # CODE TO DISPLAY POST
        return render_template('userPage.html', username = username)
    else:
        return render_template('userPage.html', username = username)

if __name__ == "__main__":
    app.debug = True
    app.run()

