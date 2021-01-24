# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch


es = Elasticsearch(hosts='39.104.188.56:9299')

print(0)
index = 'bi_da9ae629609135e55e4af697308f63b4'
resp = es.indices.get_mapping(index=index, doc_type='doc')
print(1)
mappings = resp[index]['mappings']['doc']['properties']
print(2)
field_list = mappings.keys()
print(3)
print(list(field_list))
