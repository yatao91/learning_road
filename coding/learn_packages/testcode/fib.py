# -*- coding: utf-8 -*-
print("I am fib")


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
