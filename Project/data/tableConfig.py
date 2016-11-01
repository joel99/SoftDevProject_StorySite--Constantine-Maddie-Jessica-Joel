import sqlite3

###ONE TIME USE TO CREATE THE DATABASE AND TABLES


db = sqlite3.connect("DB.db")
c = db.cursor()


storyTable = "CREATE TABLE Stories(title TEXT, StoryID INTEGER, mostRecentEditID INTEGER);"
c.execute(storyTable)

editsTable = "CREATE TABLE Edits(EditID INTEGER, timeStamp TEXT, StoryID INTEGER, UserID INTEGER, EditContent TEXT);"
c.execute(editsTable)

peopleTable = "CREATE TABLE People(UserID INTEGER, StoryIDs BLOB);"
c.execute(peopleTable)

accntTable = "CREATE TABLE AccountInfo(Username TEXT, HashedPass TEXT, UserID INTEGER);"
c.execute(accntTable)

db.commit()
db.close()
