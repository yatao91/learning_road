# -*- coding: utf-8 -*-
import hashlib
import time
import json
import requests

zhongzhao_url = "http://test2.zhaobiao.cn/api/jiefeng/competitor"

# 计算签名
time_int = int(time.time())
time_str = str(time_int)
userId = "xywm009"
copsName = "黑龙江德治律师事务所"
token = "8moQzZA7ef5Bhkiu"
data_str = '{"userId":"xywm009","copsName":"黑龙江德治律师事务所"}'

content = data_str + token + time_str
sign = hashlib.md5(content.encode('utf-8')).hexdigest()
print(time_str, sign, data_str)

# 组装body
body = {"time": time_int,
        "sign": sign,
        "data": data_str}

# 发起请求
resp = requests.post(url=zhongzhao_url,
                     data=body,
                     headers={"Content-Type": "application/x-www-form-urlencoded"})
request_body = resp.request.body
response_text = resp.text
print(request_body)
print(response_text)

