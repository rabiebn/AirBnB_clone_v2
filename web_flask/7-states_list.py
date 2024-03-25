#!/usr/bin/python3
"""States list module"""
from flask import Flask, render_template, g
from models import storage
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():

    return render_template('7-states_list.html',
                           states=storage.all("State").values().sort())

@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)