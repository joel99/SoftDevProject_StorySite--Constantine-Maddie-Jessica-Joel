import sqlite3
from time import gmtime, strftime



###This file adds NEW stories to the database. It writes to both the stories
###and edits tables

###We must be given a dictionary with title, userid, and editcontent.
###Since this is a new story, the mostRecentEditID and EditID are just 1.

##to test:
##x = {"title":"'FirstStory'","timestamp":"'Today'", "userID":1, "editcontent":"'this is edit content.'"}

def addStory(title, userID, editContent):
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    
    addTitle = title
    addTime =  strftime("%Y-%m-%d %H:%M:%S", gmtime())
    addUser = userID
    edit = editContent
    addMRE = 1
    addEid = 1

    addTitle = "'"+addTitle+"'"
    addTime = "'"+addTime+"'"
    edit="'"+edit+"'"
    
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

    cmd4 = "SELECT StoryIDs FROM People WHERE UserID = userID;"
    sel3 = c.execute(cmd4).fetchone()
    listOfStoryIds = sel3[0]


    listOfStoryIds ="'"+ listOfStoryIds + " "+ str(addStoryID)+"'"
    cmd4Extra = "UPDATE People Set StoryIDs = %s WHERE UserID = %d;"%(listOfStoryIds, userID)
    c.execute(cmd4Extra)

    
    db.commit()
    db.close()



