#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
  """render html page that display states"""
  states = storage.all(State)
  return render_template("7-states_list.html", states = states)


@app.teardown_appcontext
def teardown(self):
  """ remove the current SQLAlchemy Session"""
  storage.close()

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
