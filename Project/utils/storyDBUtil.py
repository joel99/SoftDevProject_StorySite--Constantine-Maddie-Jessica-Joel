import sqlite3, hashlib, random
from time import gmtime, strftime

def randStoryID():
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT StoryID FROM Stories ORDER BY StoryID DESC;"
    sel = c.execute(cmd).fetchone()#should be maxId, unless this is empty
    maxID = sel[0]

    randomID = random.randrange(maxID+1)

    randomID = random.randrange(maxID) + 1
    cmd = "SELECT StoryID FROM Stories WHERE StoryID = %d;"%(randomID)
    sel = c.execute(cmd).fetchone()
   
    return sel[0]
    db.close()

    
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

#updateInfo Format: story title, story content, timestamp, username, storyID
def getStoryUpdateInfo(storyID):
    updateInfo = []
    print storyID

    db = sqlite3.connect("data/DB.db")
    c = db.cursor()

    cmd = "SELECT * FROM Stories WHERE StoryID = %d;"%(storyID)
    sel = c.execute(cmd).fetchone()
    updateInfo.append(sel[0]) ##adds title
    ##latestEditID = sel[2]

    cmd2 = "SELECT * FROM Edits WHERE StoryID = %d ORDER BY EditID DESC;"%(storyID)
    latestEdit = c.execute(cmd2).fetchone()
    
    updateInfo.append(latestEdit[4])
    updateInfo.append(latestEdit[1]) #for latest edit timestamp
    userID = latestEdit[3] #pass into user database
    
    #print "Selecting userID %d from accountInfo"%(userID)
    cmd3 = "SELECT * FROM AccountInfo WHERE UserID = %d;"%(userID)
    selUser = c.execute(cmd3).fetchone()
    
    updateInfo.append(selUser[0])
    
    updateInfo.append(storyID)
    db.close()
    #print updateInfo
    return updateInfo

def editStory(storyID, userID, content):
    
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()

    cmd = "SELECT * FROM Stories WHERE StoryID = %d;"%(int(storyID))
    sel = c.execute(cmd).fetchone()
    mREID = sel[2] + 1

    cmdExtra = "UPDATE Stories SET mostRecentEditID = %d WHERE StoryID = %d;"%(int(mREID), int(storyID))
    c.execute(cmdExtra)


    cmd2 = "SELECT EditID FROM Edits ORDER BY EditID DESC;"

    sel2 = c.execute(cmd2).fetchone()
    
    newEditId = sel2[0] + 1
   

    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
   # timestamp = "'" + timestamp + "'"

    cmd3 = "INSERT INTO Edits VALUES (%d,'%s',%d,%d,'%s');"%(int(newEditId),timestamp, int(storyID), int(userID), content)
    #print cmd3
    c.execute(cmd3)

    cmd4 = "SELECT StoryIDs FROM People WHERE UserID = '%s';"%(userID)
    sel3 = c.execute(cmd4).fetchone()
    listOfStoryIds = sel3[0]


    listOfStoryIds ="'"+ listOfStoryIds + " "+ str(storyID)+"'"
    cmd4Extra = "UPDATE People Set StoryIDs = %s WHERE UserID = %d;"%(listOfStoryIds, userID)
    c.execute(cmd4Extra)

    
  
    db.commit()
    db.close()

#editStory(1,1,"i want to edit")
