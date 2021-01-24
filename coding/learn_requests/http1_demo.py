# -*- coding: utf-8 -*-
import requests

url = 'https://api.jiefengnews.com/zhongzhao/sidewise-bar/dashboard/config'

data = {
    "keyword": "钢管"
}

resp = requests.post(url=url, json=data)

data = resp
