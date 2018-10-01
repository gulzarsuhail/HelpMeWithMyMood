# import module dependencies
import tweepy
import datetime

import json
# get the credentials
from Credentials import Credentials

class Twitter:

    # setup tweepy in constructor
    def __init__(self):

        # initialize tweepy with credentials
        auth = tweepy.OAuthHandler(Credentials.twitter_consumer_api_key, Credentials.twitter_consumer_api_secret)
        auth.set_access_token(Credentials.twitter_access_token, Credentials.twitter_access_token_secret)

        self.api = tweepy.API(auth)

    # gets tweets of an author since a time
    def getLastTweets(self, author):

        # get data from twitter api
        tweets = self.api.user_timeline(screen_name=author, count=200, include_rts=False, tweet_mode="extended")
       
        return self.filterTweetData(tweets)

    # gets tweets since the said tweet id 
    def getTweetsSinceTweetId(self, author, since_tweet_id):

        # get the tweets from api
        tweets = self.api.user_timeline(screen_name=author, count=2, since_id=since_tweet_id, include_rts=False, tweet_mode="extended")

        # filter and return the tweets
        return self.filterTweetData(tweets)

    # returns tweets with only the required data for the project
    def filterTweetData(self, tweets):
        filteredTweets = []
        for tweet in tweets:
            filteredTweets.append (Tweet(tweet))
        return filteredTweets


# defines data of a single tweet
class Tweet:
    def __init__(self, tweet):
        # store data from tweet into self
        self.screen_name = tweet.user.screen_name
        self.text = tweet.full_text
        self.favorited = tweet.favorited
        self.created_at = tweet.created_at
        self.id = tweet.id