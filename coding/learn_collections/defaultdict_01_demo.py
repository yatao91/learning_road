# -*- coding: utf-8 -*-
from collections import defaultdict


def default_factory():
    return "default value"


d = defaultdict(default_factory, foo="bar")
print("d: ", d)
print("foo => ", d["foo"])
print("bar => ", d["bar"])
