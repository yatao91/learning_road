# -*- coding: utf-8 -*-
import multiprocessing
import os

import requests

url = 'http://127.0.0.1:5000'


def req():
    pid = os.getpid()
    print(pid)
    response = requests.get(url)
    return response


if __name__ == '__main__':
    for i in range(20):
        t = multiprocessing.Process(target=req)
        t.start()
        t.join()
