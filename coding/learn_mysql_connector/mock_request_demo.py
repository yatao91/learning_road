# -*- coding: utf-8 -*-
import threading

import requests

url = 'http://127.0.0.1:5000'


def req():
    response = requests.get(url)
    return response


if __name__ == '__main__':
    for i in range(20):
        t = threading.Thread(target=req)
        t.start()
        t.join()
