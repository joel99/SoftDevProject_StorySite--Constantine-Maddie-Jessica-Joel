import storyDBUtil

def getStoryIDs(userID):
    return storyDBUtil.getStoryIDs(userID)

def getStoryUpdate(storyID):
    return storyDBUtil.getStoryUpdateInfo(storyID)

def randStoryID():
    return storyDBUtil.randStoryID()
