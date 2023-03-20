from flask import Flask 
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/about')
def about():
    return 'The student who wrote this code is Daniel Yowell. The current date is 3/19/2023'

@app.route('/assignment5')
def assignment5():
    return 'This is for assignment 5 in CS 3203'

@app.route('/ae04b68fd39f74afd2a4197da0e3b897')
def secret():
    return 'secret page! :)'

if __name__ == "__main__":
    app.run()