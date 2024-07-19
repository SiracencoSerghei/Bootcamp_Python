"""
look on https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/bye")
def bye():
    return "<p>Bye Bye</p>"

if __name__ == "__main__":
    app.run()
    