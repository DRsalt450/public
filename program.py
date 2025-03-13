from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>i dont have drugs in my left shoe.</p>"
