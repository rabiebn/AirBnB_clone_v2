#!/usr/bin/python3
"""C is fun! route"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    txt = text.replace('_', ' ')
    return "C {}".format(txt)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text='is cool'):
    txt = text.replace('_', ' ')
    return "Python {}".format(txt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
