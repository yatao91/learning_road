# -*- coding: UTF-8 -*-
from functools import reduce
from operator import mul


def fact_lambda(n):
    return reduce(lambda a, b: a * b, range(1, n+1))


def fact_mul(n):
    return reduce(mul, range(1, n+1))
