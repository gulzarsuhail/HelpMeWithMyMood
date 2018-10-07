
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
        lastTweet = db.getLastTweetID(user)
        print(user)
        tweets = Twitter.getTweetsSinceTweetId(user, lastTweet)
        nluCheckedTweets = nluCheckTweets(tweets)
        db.newTweets(nluCheckedTweets)

# initialize the refresh schedule
scheduleTweetRefresh()