# -*- coding: utf-8 -*-
import time
import threading

import redis_lock
from redis import StrictRedis

redis = StrictRedis(host="192.168.0.111",
                    port=6380,
                    db=13,
                    socket_timeout=5,
                    socket_connect_timeout=2,
                    decode_responses=True)


def func1():
    with redis_lock.Lock(redis_client=redis, name="test_key", expire=10):
        print("线程01获取到了锁")
        time.sleep(120)


def func2():
    with redis_lock.Lock(redis_client=redis, name="test_key", expire=10):
        print("线程02获取到了锁")
        time.sleep(120)


if __name__ == '__main__':
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
