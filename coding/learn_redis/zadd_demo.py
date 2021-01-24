# -*- coding: utf-8 -*-
from redis import StrictRedis

redis = StrictRedis(host='192.168.0.111',
                    port=6380,
                    db=0)

pipe = redis.pipeline()

pipe.zadd("test", {"demo_id": 1578023418.658209})

pipe.execute()
