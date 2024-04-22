#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
import models
from models import storage

print(models.storage)
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    # states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    states = storage.all(State)
    states_list = list(states.values())
    # print(states,states_list)
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
