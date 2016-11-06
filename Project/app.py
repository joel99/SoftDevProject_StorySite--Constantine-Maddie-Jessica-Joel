from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3, hashlib
from time import gmtime, strftime
from utils import loginUtil, storyUtil, crtStry


app = Flask(__name__)
app.secret_key = "secrets"

@app.route("/") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def root():
    logout()
    if isLoggedIn():#if logged in
        return redirect(url_for('home'))
    else:#if not logged in
        return render_template('login.html', isLoggedIn = str(False))

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
        return redirect(url_for('home'))
    return redirect(url_for('root'))

@app.route('/home') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def home():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    #pull the relevant data from db, make list, pass to html
    stories = storyUtil.getStoryIDsForUser(session["userID"])
    if (len(stories) == 0):
        return render_template('home.html', isLoggedIn = 'True', isEmpty = True)
    else:
        storyUpdates = [] #each update includes
        #storyTitles, original author, link (generate it), mostRecentText (use database), editTimeStamp
        for i in stories:
            storyUpdates.append(storyUtil.getStoryUpdate(i))
        return render_template('home.html', isLoggedIn = 'True', feedStories = storyUpdates)
 
#TOOLBAR FUNCTIONS - Joel

#executed by a form
@app.route('/search/', methods = ['GET']) #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def search():
    query =  request.args.get("query")
    print query
    ids = storyUtil.getMatchingStoryTitles(query)
    if (len(ids) == 0):
        return render_template('search.html', isEmpty = True)
    storyUpdates = []
    for i in ids:
        storyUpdates.append(storyUtil.getStoryUpdate(i))
    return render_template("search.html", isLoggedIn = str(isLoggedIn()), feedStories = storyUpdates)


@app.route('/toolbar', methods = ['POST'])
def toolBar():
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
    return render_template("settings.html", user = getUserID(), isLoggedIn = 'True')

@app.route('/changePass') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def changePass():
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    d = request.form # pass, pass1, pass2
    OGpass = passHash(d["pass"])
    pass1 = d["pass1"]
    pass2 = d["pass2"]
    if OGPass == storyUtil.getPass(getUserID()) and pass1 == pass2:
        storyUtil.changePass(getUserID(), passHash(pass1))
    return redirect(url_for('settings'))
    

@app.route('/library') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def library():
    titles = getStoryTitles()
    IDs = getStoryIDs()
    hashedIDs = []
    for ID in IDs:
        hashedIDs.append(pageHash(ID))
    allOfEm = [titles, hashedIDs, IDs]
    return render_template("library.html", isLoggedIn = isLoggedIn(), libList = allOfEm)


@app.route('/library/<string:idHash>') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def storyPage(storyID, idHash):
    editors = getEditors(storyID)
    canEdit = True
    for ind in editors:
        if pageHash(ind) == idHash:
            canEdit = False
    story = getFullStory()
    return render_template('storyPage.html', title = getStory(storyID), canEdit = canEdit, isLoggedIn = str(isLoggedIn()), fullStory = story)


@app.route('/create') #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def createStory():
    d = request.form
    if (not isLoggedIn()):
        return redirect(url_for('root'))
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    crtStory.addStory(d["title"], time, session["userID"], d["editContent"])
    # addStory(title:)
    #return # title, timestamp, usrID, editcontent



#HELPERS-----------------------------------------------------------------------
def isLoggedIn():
    return "userID" in session

def getUserID():
    return session["userID"]

def pageHash(id):
    return hashlib.md5(str(id)).hexdigest()

def passHash(pwd):
    return hashlib.sha512(pwd).hexdigest()

if __name__ == "__main__":
    app.debug = True
    app.run()

