# -*- coding: utf-8 -*-
"""
author:      苏亚涛
email:       yataosu@gmail.com
create_time: 2019/10/23 11:06
file:        user_list.py
ide:         PyCharm
"""
from redis import StrictRedis

redis = StrictRedis(host='192.168.0.111',
                    port=6380,
                    db=2,
                    decode_responses=True)

try:
    a = 1 / 0
except Exception as e:
    exc_info = {"project_index": "test_index",
                "doc_id": "111111",
                "stage": "test",
                "reason": e}
    redis.rpush("data-warehouse:zhongzhao:exceptions", exc_info)

# data = redis.rpop("test_list")
# print(type(data), data)
