# -*- coding: utf-8 -*-
from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/hello", methods=["POST"])
def hello():
    params = request.get_data()
    print(type(params), params)

    # bytes类型的响应: 可以直接通过json.loads进行反序列化
    params_01 = json.loads(params)
    print(type(params_01), params_01)

    # bytes类型的响应: 可以先进行解码,然后再进行反序列化(不过有点多此一举)
    params_02 = json.loads(params.decode(encoding="utf-8"))
    print(type(params_02), params_02)
    return "hello flask"


if __name__ == '__main__':
    app.run(debug=True)
