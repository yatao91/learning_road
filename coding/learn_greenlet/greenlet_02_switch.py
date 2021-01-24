# -*- coding: utf-8 -*-
from greenlet import greenlet


def func1(x, y):
    z = gr2.switch(x + y)
    print(z)


def func2(u):
    print(u)
    gr1.switch(42)


gr1 = greenlet(run=func1)
gr2 = greenlet(run=func2)
gr1.switch("hello", " world")
