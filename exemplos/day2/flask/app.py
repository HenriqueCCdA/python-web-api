from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    1 /  0
    return "<strong>Hello  World</strong>"
