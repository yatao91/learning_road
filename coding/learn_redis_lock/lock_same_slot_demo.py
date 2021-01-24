# -*- coding: utf-8 -*-
import redis_lock
from redis import StrictRedis

redis = StrictRedis(host="r-hp3ojxc6skjau81163.redis.huhehaote.rds.aliyuncs.com",
                    db=99,
                    port=6379,
                    decode_responses=True)

key = "test:{lock}"

with redis_lock.Lock(redis, key, 10):
    print("获取redis锁")
