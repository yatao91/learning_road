# -*- coding: utf-8 -*-
import requests
import base64
base64.b64encode()


url = 'http://127.0.0.1:8000/user/login'
data = {
    "username": "test",
    "password": "testtest"
}

resp = requests.post(url=url, json=data)

print(resp.text)
