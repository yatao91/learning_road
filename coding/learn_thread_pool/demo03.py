# -*- coding: utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor


def wait_on_b():
    time.sleep(5)
    print("等待b的结果")
    print(b.result())
    return 5


def wait_on_a():
    time.sleep(5)
    print("等待a的结果")
    print(a.result())
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)
