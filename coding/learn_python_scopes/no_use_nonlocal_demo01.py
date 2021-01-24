# -*- coding: utf-8 -*-
"""
不适用nonlocal/global的情形
各级scope使用各作用域的变量值
"""
x = 0


def outer():
    x = 1

    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
print("global:", x)
