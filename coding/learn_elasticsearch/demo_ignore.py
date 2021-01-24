# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['39.104.48.117:9288'])

resp = es.search(index="data-warehouse-zhongzhao-sniffer-bid-result-v",
                 doc_type="doc",
                 body={"query": {"term": {"deduplication": "测试不存在"}}},
                 ignore=[404])
print(resp)
