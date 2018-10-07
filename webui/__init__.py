from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter

from credentials import Credentials 
from helpers import db

# create flash instance
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'thisisasecretlol'

# set twitter keys
twitter_blueprint = make_twitter_blueprint(api_key=Credentials.twitter_consumer_api_key, api_secret=Credentials.twitter_consumer_api_secret)

# use the auth prefix for twitter
app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')

@app.route("/twitter")
def twitter_login():
    if not twitter.authorized:
        return redirect(url_for('twitter.login'))
    account_info = twitter.get('account/settings.json')

    if account_info.ok:
        account_info_json = account_info.json()
        return '<h1> Twitter bame is @{}'.format(account_info_json['screen_name'])

    return '<h1>request failed</h1>'

# @app.route('/')
# def homepage():
#     return render_template("home.html")

# start the server
app.run()
