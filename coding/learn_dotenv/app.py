# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv(override=True)

app = Flask(__name__)
app.config.from_object("config")


@app.route("/hello")
def hello():
    NUM = os.getenv("NUM")
    print("数值类型:{}".format(type(NUM)))
    return os.getenv("DEPLOY_ENV")


if __name__ == '__main__':
    app.run(host="192.168.0.111", port=8000)
