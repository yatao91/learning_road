# -*- coding: utf-8 -*-
"""
author:      苏亚涛
email:       yataosu@gmail.com
create_time: 2019/10/24 13:43
file:        demo01.py
ide:         PyCharm
"""
from itsdangerous import URLSafeSerializer

auth_s = URLSafeSerializer("secret_key", "auth")
token = auth_s.dumps({"id": 5, "name": "itsdangerous"})

# eyJpZCI6NSwibmFtZSI6Iml0c2Rhbmdlcm91cyJ9.yVM1mw_LiHJqFj1VOFi6xnsd3Js
print(token)

data = auth_s.loads(token)
print(data, data['name'])
