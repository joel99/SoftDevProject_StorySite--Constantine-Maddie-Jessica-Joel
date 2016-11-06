import sqlite3, hashlib, random
from time import gmtime, strftime

def randStoryID():
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT * FROM Stories;"
    sel = c.execute(cmd).fetchone()
    maxID = sel[1]
    db.close()
    return random.randrange(maxID)
    
def getStoryIDs(userID):
    print "getting story IDs from database"
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
#apparently this is insecure but w/e
    cmd = "SELECT * FROM People WHERE UserID = %d;"%(userID)
    sel = c.execute(cmd).fetchone()
    #turn blob into array
    #print "SELECTION IS " + str(sel)
    db.close()
    return sel[1]

#updateInfo Format: story title, edit content, edit timestamp, edit author, url hash, storyID
def getStoryUpdateInfo(storyID):
    updateInfo = []

    db = sqlite3.connect("data/DB.db")
    c = db.cursor()

    cmd = "SELECT * FROM Stories WHERE StoryID = %d;"%(storyID)
    sel = c.execute(cmd).fetchone()
    updateInfo.append(sel[0])
    latestEditID = sel[2]

    cmd2 = "SELECT * FROM Edits WHERE EditID = %d AND StoryID = %d;"%(latestEditID, storyID)
    sel2 = c.execute(cmd2).fetchone()
    #print "sel2 is %s"%(sel2,)
    latestEdit = sel2
    updateInfo.append(latestEdit[4]) #for latest edit content
    updateInfo.append(latestEdit[1]) #for latest edit timestamp
    userID = latestEdit[3] #pass into user database

    #print "Selecting userID %d from accountInfo"%(userID)
    cmd3 = "SELECT * FROM AccountInfo WHERE UserID = %d;"%(userID)
    sel3 = c.execute(cmd3).fetchone()
    selUser = sel3
    
    updateInfo.append(selUser[0])
    updateInfo.append(hashlib.md5(str(storyID)).hexdigest())
    updateInfo.append(storyID)
    db.close()
    return updateInfo


def editStory(storyID, userID, content):
    
    db = sqlite3.connect("../data/DB.db")
    c = db.cursor()

 

    cmd = "SELECT * FROM Stories WHERE StoryID = %d;"%(storyID)
    sel = c.execute(cmd).fetchone()
    mREID = sel[2] + 1

    cmdExtra = "UPDATE Stories SET mostRecentEditID = %d WHERE StoryID = %d;"%(mREID, storyID)
    c.execute(cmdExtra)


    cmd2 = "SELECT EditID FROM Edits ORDER BY EditID DESC;"

    sel2 = c.execute(cmd2).fetchone()
    
    newEditId = sel2[0] + 1
   

    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    timestamp = "'" + timestamp + "'"

    cmd3 = "INSERT INTO Edits VALUES (%d,%s,%d,%d,%s);"%(newEditId, timestamp, storyID, userID, content)
    c.execute(cmd3)

    cmd4 = "SELECT StoryIDs FROM People WHERE UserID = userID;"
    sel3 = c.execute(cmd4).fetchone()
    listOfStoryIds = sel3[0]


    listOfStoryIds = listOfStoryIds + " "+ str(storyID)
    cmd4Extra = "UPDATE People Set StoryIDs = %s WHERE UserID = %d;"%(listOfStoryIds, userID)

    
  
    db.commit()
    db.close()

<<<<<<< HEAD
editStory(1, 1, "'this is the fifth edit content'")
=======
>>>>>>> 7b3460aa10466dd9f5ba4ded2c148960799141dd
