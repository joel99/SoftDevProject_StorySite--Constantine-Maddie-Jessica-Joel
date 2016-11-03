import sqlite3



###This file adds NEW stories to the database. It writes to both the stories
###and edits tables

###We must be given a dictionary with title, timestamp, userid, and editcontent.
###Since this is a new story, the mostRecentEditID and EditID are just 1.

##to test:
x = {"title":"'FirstStory'","timestamp":"'Today'", "userID":1, "editcontent":"'this is edit content.'"}

def addStory(d):
    db = sqlite3.connect("DB.db")
    c = db.cursor()
    
    addTitle = d["title"]
    addTime = d["timestamp"]
    addUser = d["userID"]
    edit = d["editcontent"]
    addMRE = 1
    addEid = 1

    ###findSI is supposed to find the last created storyID. 
    
    cmd = "SELECT storyID FROM Stories ORDER BY storyID DESC;"
    sel = c.execute(cmd)
    addStoryID = 1
    for record in sel:
        addStoryID = addStoryID + record[0]
        break

    e = "INSERT INTO Stories VALUES(%s,%d,%d);"%(addTitle, addStoryID,addMRE )

    c.execute(e)

    
    alpha = "INSERT INTO Edits VALUES(%d,%s,%d,%d,%s);"%(addEid, addTime, addStoryID, addUser, edit)
    c.execute(alpha)

    db.commit()
    db.close()

addStory(x)

