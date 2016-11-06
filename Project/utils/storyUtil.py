import storyDBUtil, sqlite3, crtStry

def getStoryIDsForUser(userID):
    storiesString = storyDBUtil.getStoryIDs(userID)
    splitter = storiesString.split()
    ret = []
    for i in splitter:
        if not (i is ''):
            ret.append(int(float(i)))
    return ret
    #return [int(i) for i in storiesString.split()]

def getStoryUpdate(storyID): #gets the edits 
    return storyDBUtil.getStoryUpdateInfo(storyID)

def getStory(storyID): # returns a story with the given story ID
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT * FROM Stories WHERE StoryID = %d;"%(storyID)
    sel = c.execute(cmd)
    db.close()
    for record in sel:
        return ret[0]

def getStoryTitles(): # returns a list of all story titles in order of most recently edited
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT * FROM Stories ORDER BY StoryID DESC;"
    sel = c.execute(cmd)
    titles = []
    for record in sel:
        titles.append(record[0])
    db.close()
    return titles

def getMatchingStoryTitles(queryString):
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT * FROM Stories ORDER BY StoryID Desc;"
    sel = c.execute(cmd)
    matchingStories = []
    for record in sel:
        if (record[0].lower() in queryString.lower() or queryString.lower() in record[0].lower()):
            matchingStories.append(record[1])
    db.close()
    return matchingStories
    

def getStoryIDs(): # returns a list of all story titles in order of most recently edited
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT * FROM Stories ORDER BY StoryID DESC;"
    sel = c.execute(cmd)
    IDs = []
    for record in sel:
        IDs.append(record[1])
    db.close()
    return IDs

def getFullStory(storyID): # returns a string of the entire story
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT EditContent FROM Edits WHERE StoryID = %d;"%(storyID)
    sel = c.execute(cmd)
    db.close()
    story = ""
    for record in sel:
        story += record + " "
    return story

def getEditors(storyID):
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT UserID FROM Edits WHERE StoryID = %d;"%(storyID)
    sel = c.execute(cmd)
    db.close()
    editors = []
    for record in sel:
        editors.append(record[0])
    return editors

def randStoryID():
    return storyDBUtil.randStoryID()



def getPass(userID):
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT HashedPass FROM AccountInfo WHERE UserID = %d;"%(userID)
    sel = c.execute(cmd)

    
    for record in sel:
        return record[0]
    db.commit()
    db.close()

def changePass(userID, newPass):
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "UPDATE AccountInfo SET HashedPass = newPass WHERE UserID = %d;"%(userID)
    sel = c.execute(cmd)
    db.commit()
    db.close()
    

