#!/usr/bin/python3
"""a script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return Hello HBNB! """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return HBNB"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """display C  followed by the value of the text variable"""
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    """display Python, followed by the value of the text variabl"""
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
