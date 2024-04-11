#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello1(text):
    text_without_space = text.replace('_', ' ')
    return "C " + text_without_space


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
def hello2(text):
    text_without_space2 = text.replace('_', ' ')
    return "Python " + text_without_space2


@app.route("/number/<int:n>", strict_slashes=False)
def numb(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
