# -*- coding: utf-8 -*-
"""
pyspark序列化
    MarshalSerializer: 此序列化器比PickleSerializer快,但支持类型较少
    PickleSerializer: 支持几乎所有的python对象类型,但不如专门的序列化器快
"""
from pyspark.context import SparkContext
# from pyspark import SparkContext
from pyspark.serializers import MarshalSerializer


sc = SparkContext(master="spark://spark001:7077", appName="serializer_demo", serializer=MarshalSerializer())

print(sc.parallelize(list(range(1000))).map(lambda x: 2 * x).take(10))

sc.stop()
