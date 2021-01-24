# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)

@app.after_request
def handle_response(r):
    resp = {
        "status": "1",
        "info": "success"
    }
    data = r.json
    resp['data'] = data
    r.json = resp
    print(type(r.data), type(r.json), r.data, r.json)
    return r


@app.route("/hello")
def hello():
    return {"hardware": 1, "b": 2}


if __name__ == '__main__':
    app.run(debug=True)
