# -*- coding: utf-8 -*-
from flask import Flask, session

app = Flask(__name__)
app.secret_key = '123'
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"


@app.route("/hello01", methods=["GET"])
def hello():
    session["test"] = "test"
    return "hello world"


if __name__ == '__main__':
    app.run(port=8000, debug=True)