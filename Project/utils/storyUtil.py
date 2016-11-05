import storyDBUtil

def getStoryIDs(userID):
    storiesString = storyDBUtil.getStoryIDs(userID)
    return [int(i) for i in storiesString.split()]

def getStoryUpdate(storyID):
    return storyDBUtil.getStoryUpdateInfo(storyID)

<<<<<<< HEAD
def getStory(storyID):
	return

def 
=======
def randStoryID():
    return storyDBUtil.randStoryID()
>>>>>>> a4879583223701dbb59f60bf496960842cf914bc
