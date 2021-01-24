# -*- coding: UTF-8 -*-
import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write


with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

print(what)
