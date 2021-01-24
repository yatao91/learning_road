# -*- coding: utf-8 -*-
from flask import Flask
from flask.views import MethodView

app = Flask(__name__)


def deco01(func):
    def wrapper(*args, **kwargs):
        print("deco01-in")
        a = func(*args, **kwargs)
        print("deco01-out")
        return a
    return wrapper


def deco02(func):
    def wrapper(*args, **kwargs):
        print("deco02-in")
        b = func(*args, **kwargs)
        print("deco02-out")
        return b
    return wrapper


def deco03(func):
    def wrapper(*args, **kwargs):
        print("deco03-in")
        a = func(*args, **kwargs)
        print("deco03-out")
        return a
    return wrapper


class BaseView(MethodView):
    decorators = [deco03, deco01, deco02]

    def dispatch_request(self, *args, **kwargs):
        result = super().dispatch_request(*args, **kwargs)
        return result


class UserView(BaseView):

    # @deco03
    def get(self):
        print("user")
        return "user"


app.add_url_rule("/user", view_func=UserView.as_view("user"))


if __name__ == '__main__':
    app.run(debug=True)
