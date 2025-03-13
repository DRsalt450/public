from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>i dont have drugs in my left shoe.</p>"

@app.route("/page")
def page():
    return "<p>yo im a rapper, more like a wrapper. i eat banana, you eat canada</p>"
