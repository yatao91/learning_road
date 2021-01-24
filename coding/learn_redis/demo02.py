# -*- coding: utf-8 -*-
from redis import StrictRedis


redis = StrictRedis(host="192.168.0.111",
                    port=6380,
                    db=13,
                    decode_responses=True)

counter = redis.get(name="zhongzhao:cache:lru:counter")
print(counter, type(counter))
head = redis.hgetall(name="zhongzhao:cache:lru:head")
tail = redis.hgetall(name="zhongzhao:cache:lru:tail")
node01 = redis.hgetall(name="zhongzhao:cache:keyword:keyword_01")
print(head, tail, node01)


aaa = redis.get("abc")
print(aaa, type(aaa))
