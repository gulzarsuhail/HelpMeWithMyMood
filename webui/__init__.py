from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.consumer.backend import BaseBackend

from credentials import Credentials 
import helpers as helper

# create flash instance
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'thisisasecretlol'

# set twitter keys
twitter_blueprint = make_twitter_blueprint(api_key=Credentials.twitter_consumer_api_key, api_secret=Credentials.twitter_consumer_api_secret)

# use the auth prefix for twitter
app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')

# set up routes
@app.route("/twitter")
def twitter_login():
    if not twitter.authorized:
        return redirect(url_for('twitter.login'))
    else:
        account_info = twitter.get('account/settings.json')
        if account_info.ok:
            account_info_json = account_info.json()
            return account_info_json
        else:
            return account_info

@app.route('/')
def homepage():
    if not twitter.authorized:
        return render_template("index.html")
    else: 
        # add username to database
        account_info = twitter.get('account/settings.json')
        if account_info.ok:
            account_info_json = account_info.json()
            screen_name = account_info_json['screen_name']
            helper.addUser(screen_name)
            mood = helper.getMood(screen_name)
            if (mood == 'sadness'):
                return render_template("sadness.html")
            elif (mood == 'joy'):
                return render_template("joy.html")
            elif (mood is 'fear'):
                return render_template("fear.html")
            elif (mood == 'disgust'):
                return render_template("disgust.html")
            elif (mood == 'anger'):
                return render_template("anger.html")
            else:
                return render_template("unknown.html")
        else:
            return render_template("index.html")


# start the server
app.run()
