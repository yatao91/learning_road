# -*- coding: utf-8 -*-
from __future__ import print_function
import gevent
from gevent import monkey

monkey.patch_all()

import requests

urls = [
    'https://www.baidu.com',
    'https://www.zhihu.com',
    'https://www.python.org'
]


def print_head(url):
    print("starting {}".format(url))
    data = requests.get(url).text
    print("{}: {} bytes: {}".format(url, len(data), data[:50]))


jobs = [gevent.spawn(print_head, url) for url in urls]

gevent.wait(jobs)
