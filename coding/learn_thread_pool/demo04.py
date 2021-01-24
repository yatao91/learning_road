# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor


def wait_on_future():
    print("准备执行pow")
    f = executor.submit(pow, 5, 2)
    print("等待pow结果")
    print(f.result())


executor = ThreadPoolExecutor(max_workers=1)
executor.submit(wait_on_future)
