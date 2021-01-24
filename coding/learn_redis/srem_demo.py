# -*- coding: utf-8 -*-
from redis import StrictRedis


redis = StrictRedis(host='192.168.33.20',
                    port=6379,
                    db=0,
                    decode_responses=True)

# redis.sadd('test_key', 'hardware')
# redis.sadd('test_key', 'b')
# redis.sadd('test_key', 'c')

redis.srem('test_key', *['hardware', 'c'])
