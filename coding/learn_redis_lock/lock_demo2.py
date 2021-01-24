# -*- coding: utf-8 -*-
from redis import StrictRedis
import redis_lock
import time


redis = StrictRedis(host="127.0.0.1",
                    port=6379,
                    db=0)

with redis_lock.Lock(redis, "test") as lock:
    print("获取锁")
    time.sleep(30)
