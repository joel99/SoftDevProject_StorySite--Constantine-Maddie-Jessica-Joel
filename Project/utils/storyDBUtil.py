import sqlite3,hashlib, random

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
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
#apparently this is insecure but w/e
    cmd = "SELECT * FROM People WHERE UserID = %d;"%(userID)
    sel = c.execute(cmd)
    ret = []
    for record in sel:
         ret = record[1]
         db.close()
         return ret

#updateInfo Format: story title, edit content, edit timestamp, edit author, url hash, storyID
def getStoryUpdateInfo(storyID):
    updateInfo = []

    db = sqlite3.connect("data/DB.db")
    c = db.cursor()

    cmd = "SELECT * FROM Stories WHERE StoryID = %d;"%(storyID)
    sel = c.execute(cmd)
    updateInfo.insert(sel[0][0])
    latestEditID = record[0][2]

    cmd2 = "SELECT * FROM Edits WHERE EditID = %d AND StoryID = %d;"%(latestEditID, storyID)
    sel2 = c.execute(cmd2)
    latestEdit = sel2[0]
    updateInfo.insert(latestEdit[4]) #for latest edit content
    updateInfo.insert(latestEdit[1]) #for latest edit timestamp
    userID = latestEdit[3] #pass into user database

    cmd3 = "SELECT * FROM AccountInfo WHERE UserID = %d;"%(userID)
    sel3 = c.execute(cmd3)
    selUser = sel3[0]
    updateInfo.insert(selUser[0])
    updateInfo.insert(hashlib.md5(str(storyID)).hexdigest())
    updateInfo.insert(storyID)
    
    return updateInfo
   
