# -*- coding: utf-8 -*-
from redis import StrictRedis
import redis_lock
import time


redis = StrictRedis(host="127.0.0.1",
                    port=6379,
                    db=0)

lock = redis_lock.Lock(redis, "test")
while True:
    if lock.acquire(blocking=False):
        print("获得锁")
        time.sleep(1)
        break
    else:
        print("别人持有锁")
        time.sleep(1)
        continue
