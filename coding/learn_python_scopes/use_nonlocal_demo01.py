# -*- coding: utf-8 -*-
"""
使用nonlocal的情形:
    修改封闭作用域中的变量 不会对全局变量造成影响
"""
x = 0


def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
print("global:", x)
