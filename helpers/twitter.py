# import module dependencies
import tweepy
import datetime

# get the credentials
from credentials import Credentials

# initialize tweepy with credentials
auth = tweepy.OAuthHandler(
    "AB4XvGYaDrGYUhV3Sti9RZiJB", "oaTkWJgNmKgWPribqVyF8XXj9DNwxszbOijXWexwT16ybQVdFT")
auth.set_access_token("279902624-RpUx58W9GQ0A3PWJOs8Ks6I1DSsuuyAzEXhvAOe4",
                        "bKVbAe6w4dfg9EnCCWgGlHv7GkcwDQAVze9vH5KlxPwSK")

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
