# -*- coding: utf-8 -*-
from flask import Flask
from redis import StrictRedis
import arrow

redis_client = StrictRedis(host="192.168.0.111",
                           port=6380,
                           db=0,
                           decode_responses=True)


def create_app():
    app = Flask(__name__)

    @app.route("/hello", methods=["GET", "POST"])
    def hello():
        date = arrow.now(tz="local").strftime("%Y%m%d")
        key = f"test_su_demo:{date}"
        if redis_client.exists(key):
            value = redis_client.incr(key)
            result = None
        else:
            value = redis_client.incr(key)
            result = redis_client.expire(key, 3600)
        return "incr_value:{},expire_value:{}".format(value, result)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
