# -*- coding: UTF-8 -*-
import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()  # __enter__()
    try:
        yield
    finally:
        # __exit__()
        end = time.time()
        print('{}: {}'.format(label, end - start))


class timethis_cls:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))


with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1
