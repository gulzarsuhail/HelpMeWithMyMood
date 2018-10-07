
# import dependencies
import threading

# import helper functions
import helpers.db as db
import helpers.watsonNLU as NLU
import helpers.twitter as Twitter

# do a NLU check on tweets
def nluCheckTweets(tweets):
    # result will be returned
    result = []
    for tweet in tweets:
        # analize the tweet
        analysis = NLU.analyze(tweet['text'])
        # set analysis fields to the tweet
        tweet['emotion'] = analysis['emotion']
        tweet['sentiment'] = analysis['sentiment']
        tweet['emotion_score'] = analysis['emotion_score']
        result.append(tweet)
    return result


# schedule tweet refresh and analysis timer
def scheduleTweetRefresh():
    print ("Starting twitter refresh schedule...")
    threading.Timer(1800.0, scheduleTweetRefresh).start()
    # get all user names
    users = db.getAllUsers()
    # refresh feed for each username
    for user in users:
        getUserTweets(user)
        

def addUser(screen_name):
    # create the user
    db.newUser(screen_name)
    # refresh the user feeds
    x = db.findUser(screen_name)
    # get user tweets
    getUserTweets(x)

def getUserTweets(user):
    newTweets = []
    tweets = Twitter.getLastTweets(user)
    for tweet in tweets:
        if not db.checkExistTweet(tweet):
            newTweets.append(tweet)
    if (len(newTweets)>0):
        nluCheckedTweets = nluCheckTweets(newTweets)
        db.newTweets(nluCheckedTweets)

# initialize the refresh schedule
scheduleTweetRefresh()

def getMood(screen_name):
    return db.getMoodOfUser(screen_name)
