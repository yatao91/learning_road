# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='39.104.81.187:9288')
target_es = Elasticsearch(hosts='39.104.48.117:9288')

index = "bi_001874312a13e362489382d9f7689596"

resp = es.indices.get_mapping(index=index)
mappings = resp[index]
settings = {
    "settings": {
        "index": {
            "number_of_shards": "1",
            "analysis": {
                "filter": {
                    "jieba_synonym": {
                        "type": "synonym",
                        "synonyms_path": "synonyms/synonyms.txt"
                    },
                    "jieba_stop": {
                        "type": "stop",
                        "stopwords_path": "stopwords/stopwords.txt"
                    }
                },
                "analyzer": {
                    "my_ana": {
                        "filter": [
                            "lowercase",
                            "jieba_stop",
                            "jieba_synonym"
                        ],
                        "tokenizer": "jieba_index"
                    }
                }
            },
            "number_of_replicas": "1",
        }
    }
}

body = {}
body.update(settings)
body.update(mappings)
print(body)

target_es.indices.create(index=index, body=body)
