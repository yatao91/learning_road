# -*- coding: utf-8 -*-
from greenlet import greenlet


def func1():
    print(12)
    gr2.switch()
    print(34)


def func2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(func1)
gr2 = greenlet(func2)
gr1.switch()
print("final")
