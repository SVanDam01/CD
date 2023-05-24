# Import what we need from flask
from flask import Flask, render_template

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested


@app.route('/')
def index():
    return render_template("index.html", title="Dutch football fan chants")

@app.route('/feyenoord')
def feyenoord():
    return 'WIJ ZIJN KAMPIOEN! WIJ ZIJN KAMPIOEN!'

@app.route('/psv')
def psv():
    return 'Boerruhhhh!'

@app.route('/ajax')
def ajax():
    return 'Daar horen ze engelen zingen.... (helemaal niets in Amsterdam!)'