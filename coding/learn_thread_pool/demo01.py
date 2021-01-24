# -*- coding: utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor

pool =  ThreadPoolExecutor(max_workers=5)
trs = []


def callback(future):
    trs.remove(future)
    print("完成的任务是:{}".format(future))


def task(i):
    print("第{}个任务".format(i))


def func():
    for i in range(10):
        future = pool.submit(task, i)
        trs.append(future)
        future.add_done_callback(callback)
        print("提交的任务是:{}".format(future))
        if len(trs) >= 6:
            time.sleep(10)


if __name__ == '__main__':
    func()
    pool.shutdown(wait=True)
