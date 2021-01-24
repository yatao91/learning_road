# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)


@app.route("/hello", methods=["POST"])
def hello():
    print(request.form)
    params = {key: value for key, value in request.form.items()}
    print(params)
    params = request.get_json()
    print(params)
    print(request.form)
    print(request.get_json())
    if request.get_json(force=True):
        print("form")
    elif request.form:
        print("json")
    else:
        print(request.get_data())
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
