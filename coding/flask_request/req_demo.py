# -*- coding: utf-8 -*-
import requests
import json
import arrow
import hashlib

data = {
    "jfOrder": "xywm001-data-1593422902",
    "result": "paid"
}
timestamp = arrow.now().timestamp
sign = hashlib.md5((json.dumps(data) + "8moQzZA7ef5Bhkiu" + str(timestamp)).encode("utf-8")).hexdigest()

req_data = {"time": timestamp, "sign": sign, "data": json.dumps(data)}

resp = requests.post(
    url="http://127.0.0.1:5000/hello",
    headers={"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"},
    data=req_data,
)

print(resp.text)
