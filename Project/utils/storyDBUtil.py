import sqlite3, hashlib, random

def randStoryID():
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT * FROM Stories;"
    sel = c.execute(cmd)
    maxID = sel[0][0]
    randomID = random.randRange(maxID)
    cmd = "SELECT * FROM Stories WHERE StoryID = %d;"%(randomID)
    sel = c.execute(cmd)
    db.close()
    for record in sel:
        return ret[0]
    
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
    print sel
    mREID = sel[2] + 1
    print mREID

    cmdExtra = "UPDATE Stories SET mostRecentEditID = 5 WHERE StoryID = %d;"(storyID)
    c.execute(cmdExtra)


    cmd2 = "SELECT EditID FROM Edits ORDER BY EditID DESC;"
    sel2 = c.execute(cmd2).fetchone()
    newEditId = sel2[0] + 1

    timestamp = "today"

    cmd3 = "INSERT INTO Edits VALUES (%d,%s,%d,%d,%s);"%(newEditId, timestamp, storyID, userID, content)
    c.execute(cmd3)

    cmd4 = "SELECT StoryIDs FROM People WHERE UserID = userID;"
    sel3 = c.execut(cmd4).fetchone()
    sel3[1] = sel3[1] + " " + storyID

    
    db.close()
    db.commit()

editStory(1, 1, "this is the second edit content")
   
