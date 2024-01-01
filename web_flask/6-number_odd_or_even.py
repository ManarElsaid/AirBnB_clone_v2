#!/usr/bin/python3
"""a script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template

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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    """display Python, followed by the value of the text variabl"""
    return ("Python {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ display n is a number only if n is an integer"""
    if isinstance(n, int):
        return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def page(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return (render_template("5-number.html", n=n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """ display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY"""
    if isinstance(n, int):
        if (n % 2 == 0):
            s = "even"
        else:
            s = "odd"
        return (render_template("6-number_odd_or_even.html", n=n, s=s))


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
