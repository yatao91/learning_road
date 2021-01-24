# -*- coding: utf-8 -*-
from tornado.httpclient import HTTPClient


http_client = HTTPClient()
response = http_client.fetch('http://www.baidu.com')
print(response.body)
