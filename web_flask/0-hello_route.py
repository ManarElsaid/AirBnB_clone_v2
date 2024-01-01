#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return Hello HBNB! """
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")