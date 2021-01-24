# -*- coding: utf-8 -*-
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
a = p[0] + p[1]
print(a)
x, y = p
print(x, y)
b = p.x + p.y
print(b)
print(p)
