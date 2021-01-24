# -*- coding: utf-8 -*-
import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


from threading import Thread

t = Thread(target=countdown, args=(10, ), daemon=True)
t.start()

if t.is_alive():
    print('sting running')
else:
    print('Completed')
