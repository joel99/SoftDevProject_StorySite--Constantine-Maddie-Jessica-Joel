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
        storyUpdates.append(storyUtil.getStoryUpdate(i))
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


@app.route('/toolbar/', methods = ['POST'])
def toolBarLoggedIn():
    d = request.form
    if isLoggedIn():
        if (d["type"] == "Log Out"):
            logout()
            return redirect(url_for('root'))
        if (d["type"] == "Settings"):
            return redirect(url_for('settings'))
    else:
        if (d["type"] == "Log In"):
            return redirect(url_for('root'))
    if (d["type"] == "Library"):
        return redirect(url_for('library'))
    if (d["type"] == "Random"):
        randID = storyUtil.randStoryID()
        return redirect(url_for('storyPage', storyID = randID, idHash = pageHash(randID)))
    #somehow...    
    return redirect(url_for('home'))

def logout():
    session.pop('userID')
    print session.keys()



#OTHER PAGES - Maddie!!!


@app.route('/settings') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def settings():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    return render_template("settings.html", user = getUserID())


@app.route('/library') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def library():
    titles = getStoryTitles()
    IDs = getStoryIDs()
    hashedIDs = []
        for ID in IDs:
            hashedIDs.append(pageHash(ID))
    both = [titles, hashedIDs]
    return render_template("library.html", isLoggedIn = isLoggedIn() libList = both)


@app.route('/library/<string:idHash>') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def storyPage(storyID, idHash):
    editors = getEditors(storyID)
    canEdit = True
    for ind in editors:
        if pageHash(ind) == idHash:
            canEdit = False
    story = getFullStory()
    return render_template('storyPage.html', title = getStory(storyID), canEdit = canEdit, isLoggedIn = isLoggedIn(), fullStory = story)


@app.route('/create') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def createStory():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    # d.
    # addStory(title:)
    #return # title, timestamp, usrID, editcontent



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

