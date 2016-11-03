import sqlite3


##being given username and hashed password
##if found, return userid
def isValidAccountInfo(uN, hP):
    db = sqlite3.connect("../data/DB.db")
    c = db.cursor()

    cmd = "SELECT * FROM AccountInfo;"
    sel = c.execute(cmd)
    for record in sel:
        if uN == record[0] and hP == record[1]:
            return True

##def getUserID(uN):
    

def registerAccountInfo(uN, hP):
    db = sqlite3.connect("../data/DB.db")
    c = db.cursor()

    cmd = "SELECT UserID FROM AccountInfo ORDER BY UserID DESC;"
    sel = c.execute(cmd)
    userID = 1
    for record in sel:
        userID = userID + record[0]
        break
        
    add2AT = "INSERT INTO AccountInfo VALUES (%s,%s,%d);"%(uN,hP,userID)
    c.execute(add2AT)

    storyList = "'1,3,4'"

    ##FIND STRING FORMATTING FOR LIST
    add2PT = "INSERT INTO People VALUES (%d,%s);"%(userID, storyList)
    c.execute(add2PT)

    db.commit()
    db.close()

registerAccountInfo("'User2'","'hashedPass2'")
