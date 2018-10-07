# import module dependencies
import tweepy
import datetime

# get the credentials
from credentials import Credentials

# initialize tweepy with credentials
auth = tweepy.OAuthHandler(
    Credentials.twitter_consumer_api_key, Credentials.twitter_consumer_api_secret)
auth.set_access_token(Credentials.twitter_access_token,
                        Credentials.twitter_access_token_secret)

api = tweepy.API(auth)

# gets tweets of an author since a time
def getLastTweets(author):

    # get data from twitter api
    tweets = api.user_timeline(
        screen_name=author, count=20, include_rts=False, tweet_mode="extended")
    return filterTweetData(tweets)

# returns tweets with only the required data for the project
def filterTweetData(tweets):
    filteredTweets = []
    for tweet in tweets:
        filteredTweets.append({
            "screen_name": tweet.user.screen_name,
            "text": tweet.full_text,
            "favorited": tweet.favorited,
            "created_at": tweet.created_at,
            "id": tweet.id
        })
    return filteredTweets
