# -*- coding: utf-8 -*-
from redis import StrictRedis

redis = StrictRedis(host="192.168.0.111",
                    port=6380,
                    db=13,
                    socket_timeout=2,
                    retry_on_timeout=True,
                    decode_responses=True)

a = redis.blpop("test_key", timeout=10)
