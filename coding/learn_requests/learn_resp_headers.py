# -*- coding: utf-8 -*-
import requests


data = {"keyword": "中标"}

url = "http://39.104.168.129:8080/gethuatai"

resp = requests.post(url=url, json=data)

print(resp.headers)
