from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "secrets"

@app.route("/") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def root():
    if isLoggedIn():#if logged in
        return redirect(url_for('home'))
    else:#if not logged in
        return render_template('login.html')

@app.route("/login", methods = ['POST']) #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def login():
    d = request.form
    if isValidLogin(d["username"], d["pass"]):
        session["user"] = d["username"]
        return redirect(url_for('home')) #successful login
    return redirect(url_for('root')) #reload the login form

@app.route("/register", methods = ['POST']) #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def register():
    d = request.form
    if isValidRegister(d["pass1"], d["pass2"], d["username"]):
        #writeToAccountInfo(d)
        #writeToPeople(d)
        session["user"] = d["userName"]
        return redirect(url_for('home'))
    return redirect(url_for('root'))

@app.route('/home') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def homePage():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    return render_template('home.html', username = username)


#executed by a form
@app.route('/search', methods = ['GET']) #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def search():
    d = request.form
    if len(d["query"]) > 0:
        render_template("search.html", query = d["query"])
    #render_template()

    
@app.route('/library') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def genLibrary():
    return 0

@app.route('/library/<string:idHash>')#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def storyPage(storyID, idHash):
    d = request.form
    if "newPost" in request.args:
        # CODE TO PUT FORM INFO INTO DB
        # CODE TO DISPLAY POST
        return render_template('storyPage.html', username = username)
    else:
        return render_template('storyPage.html', username = username)


@app.route('/create') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def createStory(title, timestamp, usrID, editcontent):
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    return 0

    
@app.route('/settings') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def settings():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    return 0


#HELPERS
def isLoggedIn():
    return "user" in session

def getUser():
    return session["user"]



if __name__ == "__main__":
    app.debug = True
    app.run()

