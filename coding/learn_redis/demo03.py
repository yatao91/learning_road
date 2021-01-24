# -*- coding: utf-8 -*-
from redis import StrictRedis

redis = StrictRedis(host="192.168.0.111",
                    port=6380,
                    db=13,
                    decode_responses=True)

LRU_HEAD = "zhongzhao:cache:lru:head"
LRU_TAIL = "zhongzhao:cache:lru:tail"
LRU_KEY_FORMAT = "zhongzhao:cache:keyword:{}"
LRU_COUNTER = "zhongzhao:cache:lru:counter"

head = {"key": LRU_HEAD,
        "value": 0,
        "next": LRU_TAIL,
        "prev": 0}

tail = {"key": LRU_TAIL,
        "value": 0,
        "next": 0,
        "prev": LRU_HEAD}
redis.hmset(name=LRU_HEAD, mapping=head)
redis.hmset(name=LRU_TAIL, mapping=tail)
redis.set(LRU_COUNTER, 0)
