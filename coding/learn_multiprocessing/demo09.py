# -*- coding: utf-8 -*-
from multiprocessing import Process, freeze_support


def f():
    print('hello world')


if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()
