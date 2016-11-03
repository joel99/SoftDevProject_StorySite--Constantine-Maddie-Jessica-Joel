from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3, hashlib
from utils import login

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
    if login.isValidLogin(d["username"], d["pass"]):
        session["userID"] = login.getUserID(d["username"])
        return redirect(url_for('home')) #successful login
    return redirect(url_for('root')) #reload the login form

@app.route("/register", methods = ['POST']) #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def register():
    d = request.form
    if login.isValidRegister(d["pass1"], d["pass2"], d["username"]):#needs to check databases
        login.register(d["username"], d["pass1"])
        session["userID"] = login.getUserID(d["username"])
        return redirect(url_for('home'))
    return redirect(url_for('root'))

@app.route('/home') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def homePage():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    #pull the relevant data from db, make list, pass to html
    stories = getStoryIDs(session["userID"])
    storyUpdates = [] #each update includes
    #storyTitles, original author, link (generate it), mostRecentText (use database), editTimeStamp
    for i in stories:
        storyUpdates.insert(getStoryUpdate(i))
    return render_template('home.html', username = username, feedStories = storyUpdates)


def getStoryUpdate(storyID):
    updateInfo = []
    updateInfo.insert(getStoryTitle(i))
    updateInfo.insert(getStoryAuthor(i))
    updateInfo.insert(hashlib.md5(str(i)).hexDigest())
    updateInfo.insert(getLatestEdit(i))
    updateInfo.insert(getLatestTimeStamp(i))
    return updateInfo
    
#TOOLBAR FUNCTIONS - Joel

#executed by a form
@app.route('/search', methods = ['GET']) #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def search():
    d = request.form
    if len(d["query"]) > 0:#should be passed anyway
        return render_template("search.html", query = d["query"])
    return 0
        
    #render_template()

@app.route('/settings') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def settings():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    return 0

    
#OTHER PAGES - Maddie

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

#HELPERS--------------------------------------
def isLoggedIn():
    return "userID" in session

def getUserID():
    return session["userID"]



if __name__ == "__main__":
    app.debug = True
    app.run()

