# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()  # 线程进程安全对象
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
