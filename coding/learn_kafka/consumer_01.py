# -*- coding: utf-8 -*-
"""
author:      苏亚涛
email:       yataosu@gmail.com
create_time: 2019/10/21 15:15
file:        consumer_01.py
ide:         PyCharm
"""
from kafka import KafkaConsumer

consumer = KafkaConsumer('test-topic', bootstrap_servers='192.168.0.111:9092', group_id='test-group')

# 消费消息
for message in consumer:
    print('%s:%d:%d: key=%s value=%s' % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
