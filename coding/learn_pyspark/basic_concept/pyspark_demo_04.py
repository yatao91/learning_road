# -*- coding: utf-8 -*-
from pyspark import SparkContext
from operator import add

sc = SparkContext(master="spark://spark001:7077", appName="appdemo")

# # 1.reduce(F):使用函数F聚合RDD中的元素--函数F接收两个参数返回一个
# nums = sc.parallelize([1, 2, 3, 4, 5])
# adding = nums.reduce(add)
# print("reduce计算后结果:{}".format(adding))

"""
2.join(otherDataset,[numPartitions]): 连接两个RDD,返回一个新的RDD.比如:rdd1:(k, v) rdd2:(k, w) new_rdd:(k, (v, w))
"""
# x = sc.parallelize([("spark", 1), ("hadoop", 4)])
# y = sc.parallelize([("spark", 2), ("hadoop", 5)])
#
# joined = x.join(y)
# final = joined.collect()
# print("x与y联结后的RDD元素为:{}".format(final))

"""
3.cache():使用默认存储级别缓存此RDD
"""
words = sc.parallelize(["scala", "java", "hadoop", "spark", "akka", "spark vs hadoop", "pyspark", "pyspark vs spark"])
words.cache()
caching = words.persist().is_cached
print("数据集是否被缓存:{}".format(caching))
