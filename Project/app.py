from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3, hashlib
from utils import loginUtil, storyUtil


app = Flask(__name__)
app.secret_key = "secrets"

@app.route("/") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def root():
    if isLoggedIn():#if logged in
        return redirect(url_for('home'))
    else:#if not logged in
        return render_template('login.html')

@app.route("/login/", methods = ['POST']) #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def login():
    d = request.form
    if loginUtil.isValidLogin(d["username"], d["pass"]):
        session["userID"] = loginUtil.getUserID(d["username"])
        return redirect(url_for('home')) #successful login
    return redirect(url_for('root')) #reload the login form

@app.route("/register/", methods = ['POST']) #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def register():
    d = request.form
    if loginUtil.isValidRegister(d["pass1"], d["pass2"], d["username"]):#needs to check databases
        loginUtil.register(d["username"], d["pass1"])
        session["userID"] = loginUtil.getUserID(d["username"])
        print "userID set as %s"%(session["userID"])
        return redirect(url_for('home'))
    return redirect(url_for('root'))

@app.route('/home') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def home():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    #pull the relevant data from db, make list, pass to html
    stories = storyUtil.getStoryIDs(session["userID"])
    storyUpdates = [] #each update includes
    #storyTitles, original author, link (generate it), mostRecentText (use database), editTimeStamp
    for i in stories:
        storyUpdates.insert(storyUtil.getStoryUpdate(i))
    return render_template('home.html', feedStories = storyUpdates)
 
#TOOLBAR FUNCTIONS - Joel

#executed by a form
@app.route('/search', methods = ['GET']) #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def search():
    d = request.form
    ids = storyUtil.getMatchingStoryIDs(d["query"])
    storyUpdates = []
    for i in ids:
        storyUpdates.insert(storyUtil.getStoryUpdate(i))
    return render_template("search.html", feedStories = storyUpdates)
    
        
    #render_template()

@app.route('/toolbarLoggedIn/', methods = ['POST'])
def toolBarLoggedIn():
    d = request.form
    if (d["type"] == "Log Out"):
        logout()
        return redirect(url_for('root'))
    elif (d["type"] == "Settings"):
        return redirect(url_for('settings'))
    elif (d["type"] == "Library"):
        return redirect(url_for('library'))
    elif (d["type"] == "Random"):#FIX!
        randID = storyUtil.randStoryID()
        return redirect(url_for('storyPage', storyID = randID, idHash = pageHash(randID)))

    return redirect(url_for('home'))

def logout():
    session.pop('userID')
    print session.keys()



#OTHER PAGES - Maddie!!!


@app.route('/settings') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def settings():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    return render_template("settings.html", user = getUser())


@app.route('/library') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def library():
    stories = {}
    # CREATE A LIST OF ALL STORIES IN REVERSE ORDER (MOST RECENT @ TOP)
    return render_template("library.html", libList = stories)


@app.route('/library/<string:idHash>') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def storyPage(storyID, idHash):
    d = request.form
    #if "newPost" in request.args:
        # CODE TO PUT FORM INFO INTO DB
        # CODE TO DISPLAY POST
        #return render_template('storyPage.html', idHash = )
    #else:
    return render_template('storyPage.html', idHash = username)


@app.route('/create') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def createStory():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    getFullStory()
    return # title, timestamp, usrID, editcontent



#HELPERS-----------------------------------------------------------------------
def isLoggedIn():
    return "userID" in session

def getUserID():
    return session["userID"]

def pageHash(id):
    return hashlib.md5(str(id)).hexdigest()

if __name__ == "__main__":
    app.debug = True
    app.run()

