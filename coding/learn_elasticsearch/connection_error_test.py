# -*- coding: utf-8 -*-
"""
author:      苏亚涛
email:       yataosu@gmail.com
create_time: 2019/10/25 16:34
file:        connection_error_test.py
ide:         PyCharm
"""
from elasticsearch import Elasticsearch
from http.client import RemoteDisconnected
from urllib3.exceptions import NewConnectionError
from elasticsearch.exceptions import ConnectionError

es = Elasticsearch(hosts='192.168.0.111:9288')


try:
    data = es.cat.indices()
    print(data)
# except RemoteDisconnected as e:
#     print("*"*30, e)
#     pass
# except NewConnectionError as e:
#     print("-"*30, e)
#     pass
# except ConnectionError as e:
#     print("&"*30, e)
#     pass
except Exception as e:
    print("捕获异常", e, type(e))
    pass
