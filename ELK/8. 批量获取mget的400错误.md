# mget的400错误

### 1. 使用mget进行批量获取

`es.mget(index=index, doc_type=doc_type, body=body, refresh=True)`

当传入的body体为空时, 会产生400异常.可以使用ignore忽略400异常

`es.mget(index=index, doc_type=doc_type, body=body, ignore=[400], refresh=True)`

