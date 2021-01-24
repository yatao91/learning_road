# -*- coding: utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor


def func():
    global n
    print("线程:{}".format(n))
    time.sleep(10)
    n = n + 1
    print("执行好")


if __name__ == '__main__':
    n = 1
    pool = ThreadPoolExecutor(max_workers=1)
    for i in range(10):
        pool.submit(func)
    pool.shutdown(wait=True)
