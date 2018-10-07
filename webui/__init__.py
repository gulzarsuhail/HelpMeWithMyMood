from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

app.run()
