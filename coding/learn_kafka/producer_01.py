# -*- coding: utf-8 -*-
"""
author:      苏亚涛
email:       yataosu@gmail.com
create_time: 2019/10/21 15:19
file:        producer_01.py
ide:         PyCharm
"""
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.0.111:9092')

while 1:
    future = producer.send('test-topic', key=b'foo', value=b'bar')

    record_metadata = future.get(timeout=10)

    print(record_metadata)

    time.sleep(0.5)
