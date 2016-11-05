import storyDBUtil

<<<<<<< HEAD
def getStoryIDs(userID): # returns all stories that a user has contributed to
    return storyDBUtil.getStoryIDs(userID)
=======
def getStoryIDs(userID):
    storiesString = storyDBUtil.getStoryIDs(userID)
    return [int(i) for i in storiesString.split()]
>>>>>>> 958b25115c98366535a28ed3f2b19cf7c44a4166

def getStoryUpdate(storyID): #gets the edits 
    return storyDBUtil.getStoryUpdateInfo(storyID)

<<<<<<< HEAD
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
    db.close()
    titles = {}
    for record in sel:
        titles.append(record[0])
    return titles

def getStoryIDs(): # returns a list of all story titles in order of most recently edited
	db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT * FROM Stories ORDER BY StoryID DESC;"
    sel = c.execute(cmd)
    db.close()
    IDs = {}
    for record in sel:
        IDs.append(record[1])
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

def randStoryID(): # returns a random story
=======
def getStory(storyID):
	return 0

def randStoryID():
>>>>>>> 958b25115c98366535a28ed3f2b19cf7c44a4166
    return storyDBUtil.randStoryID()

