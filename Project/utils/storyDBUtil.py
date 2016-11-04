import sqlite3

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
    """
    updateInfo.insert(getStoryTitle(i))
    updateInfo.insert(getStoryAuthor(i))
    updateInfo.insert(hashlib.md5(str(i)).hexDigest())
    updateInfo.insert(getLatestEdit(i))
    updateInfo.insert(getLatestTimeStamp(i))
    """
    return updateInfo
   
