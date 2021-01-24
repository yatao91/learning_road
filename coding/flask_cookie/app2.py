# -*- coding: utf-8 -*-
from flask import Flask, session

app = Flask(__name__)
app.secret_key = '123'


@app.route("/hello02", methods=["GET"])
def hello():
    session["test"] = "test"
    return "hello world"


if __name__ == '__main__':
    app.run(port=8001, debug=True)