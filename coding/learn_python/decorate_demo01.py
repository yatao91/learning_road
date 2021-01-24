# -*- coding: utf-8 -*-
from functools import wraps


def cache(type=None):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if type == "hardware":
                print(type)
            elif type == "b":
                print(type)
            else:
                print("不走缓存")
                func(*args, **kwargs)
            return "test"
        return wrapper
    return decorate

@cache("hardware")
def hello_world():
    print("hello_world")


if __name__ == '__main__':
    hello_world()
