import sqlite3,hashlib

def randStoryID():
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
    cmd = "SELECT * FROM Stories;"
    sel = c.execute(cmd)
    maxID = sel[0][0]
    randomID = 
    cmd = "SELECT * FROM Stories WHERE StoryID = %d;"%(randomID)
    sel = c.execute(cmd)
    db.close()
    for record in sel:
        return ret[0]
    
def getStoryIDs(userID):
    db = sqlite3.connect("data/DB.db")
    c = db.cursor()
#apparently this is insecure but w/e
    cmd = "SELECT * FROM People WHERE UserID = %d;"%(int(userID))
    sel = c.execute(cmd)
    ret = []
    for record in sel:
         ret = record[1]
         db.close()
         return ret

def getStoryUpdateInfo(storyID):
    updateInfo = []

    db = sqlite3.connect("data/DB.db")
    c = db.cursor()

    latestEdit = 1
    
    cmd = "SELECT * FROM Stories"
    sel = c.execute(cmd)
    for record in sel:
        if record[1] == storyID:
            ##for story title
            updateInfo.insert(record[0])
            latestEdit = record[2]
            break;

    cmd2 = "SELECT * FROM Edits"
    sel2 = c.execute(cmd2)
    for record in sel2:
        if record[2] == storyID:
            ##for latest edit content
            updateInfo.insert(record[4])

            ##for latest edit timestamp
            updateInfo.insert(record[1])

            userID = record[3]
            break;
        
    
    """
    updateInfo.insert(getStoryTitle(i)) CHECK
    
    updateInfo.insert(getLatestEdit(i)) CHECK
    updateInfo.insert(getLatestTimeStamp(i)) CHECK
    updateInfo.insert(getStoryAuthor(i))
    updateInfo.insert(hashlib.md5(str(i)).hexDigest())
    """
    return updateInfo
   
