# -*- coding: utf-8 -*-
"""
author:      苏亚涛
email:       yataosu@gmail.com
create_time: 2019/10/24 13:58
file:        runtimeerror_demo.py
ide:         PyCharm
"""


def demo():
    raise RuntimeError("test")


rv = "192.168.0.111:8000"
rv = rv.rsplit(':', 1)[0].lstrip('.')
print(rv)
