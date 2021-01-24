# -*- coding: utf-8 -*-
"""
使用global的情形:
    可对全局变量进行修改,修改后的结果会assign到全局变量上, 但不会改变封闭区域的变量值
"""
x = 0


def outer():
    x = 1

    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
print("global:", x)
