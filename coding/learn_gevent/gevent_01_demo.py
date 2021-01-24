# -*- coding: utf-8 -*-
import gevent
from gevent import socket
import time

s_time = time.time()
urls = ['www.baidu.com', 'www.zhihu.com', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=2)

job_values = [job.value for job in jobs]
for value in job_values:
    print(value)
e_time = time.time()
print("time:{}".format(e_time - s_time))
