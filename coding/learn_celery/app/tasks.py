# -*- coding: utf-8 -*-
from celery_app import app
import psutil
from celery_app.libs import redis


@app.task
def test1():
    memory_per = psutil.virtual_memory().percent
    cpu_per = psutil.cpu_percent(interval=0.1)

    data = {
        'cpu_per': float(cpu_per),
        'mem_per': float(memory_per)
    }
    redis.hmset('test001', data)
