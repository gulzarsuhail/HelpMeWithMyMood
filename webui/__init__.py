from flask import Flask, render_template
import json

# create flash instance
app = Flask(__name__)
app.debug = True

@app.route('/')
def homepage():
    return render_template("home.html")

app.run()
