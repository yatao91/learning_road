# -*- coding: utf-8 -*-
from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    print(request.data)
    print(dir(request))
    print(request.environ)
    print(request.form)
    print(request.url)
    print(request.path)
    print(request.query_string)
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
