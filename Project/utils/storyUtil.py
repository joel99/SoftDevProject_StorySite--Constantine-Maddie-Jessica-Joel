import storyDBUtil

def getStoryIDs(userID): # returns all stories that a user has contributed to
    return storyDBUtil.getStoryIDs(userID)

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
    return storyDBUtil.randStoryID()

