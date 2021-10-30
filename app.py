"""
main app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Digital Library</p><div> * Add book to library</>"
