# import dependencies
import pymongo

# import project credentials
from credentials import Credentials

# connect to mongodb
myclient = pymongo.MongoClient(Credentials.mongodb_path)

# select/create database and collections
mydb = myclient["helpMeWithMyMood"]
users = mydb["users"]
tweets = mydb["tweets"]

# creates a new user
def newUser(screen_name):
    # check if user alrady exists
    if users.find({'screen_name': screen_name}).count() > 0:
        return
    else:
        # user does not exist, create a new one
        users.insert_one({
            "screen_name": screen_name
        })

# add new tweets to the database
def newTweets(insert_tweets):

    # temporary tweets
    newTweets = []

    # insert required tweet data into newTweets
    for post in insert_tweets:
        newTweets.append({
            'screen_name': post['screen_name'],
            'text': post['text'],
            'favorited': post['favorited'],
            'created_at': post['created_at'],
            'tweet_id': post['id'],
            'emotion': post['emotion'],
            'sentiment': post['sentiment'],
            'emotion_score': post['emotion_score']
        })

    # insert tweets into database
    tweets.insert_many(newTweets)

# gets all users from the database
def getAllUsers():
    screen_names = []
    for x in users.find({},{ "_id": 0, "screen_name": 1 }):
        screen_names.append(x['screen_name'])
    return(screen_names)

# get the last tweet id
def getLastTweetID(screen_name):
    if tweets.find({'screen_name': screen_name}).count() > 0:
        x = tweets.find_one({'screen_name': screen_name},sort=[("created_at", -1)])
        return x['created_at']
    else:
        return 0

# find a user
def findUser(screen_name):
    x = users.find_one({'screen_name': screen_name},sort=[("created_at", -1)])
    return x

# checks if tweet exists in database
def checkExistTweet(tweet):
    if tweets.find({'tweet_id': tweet['id']}).count() > 0:
        return True
    else:
        return False

def getMoodOfUser(screen_name):
    x = tweets.find_one({'screen_name': screen_name},sort=[("created_at", -1)])
    return x['emotion']