import storyDBUtil

def getStoryIDs(userID):
    storiesString = storyDBUtil.getStoryIDs(userID)
    return [int(i) for i in storiesString.split()]

def getStoryUpdate(storyID):
    return storyDBUtil.getStoryUpdateInfo(storyID)

def randStoryID():
    return storyDBUtil.randStoryID()
