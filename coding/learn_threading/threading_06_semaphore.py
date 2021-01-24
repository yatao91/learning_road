# -*- coding: utf-8 -*-
import threading


def worker(n, sema):
    sema.acquire()
    print("Working", n)


sema = threading.Semaphore(0)
nworkers = 10
for i in range(nworkers):
    t = threading.Thread(target=worker, args=(i, sema, ))
    t.start()
