# -*- coding: utf-8 -*-
from pyspark import SparkContext

sc = SparkContext(master="spark://spark001:7077", appName="appdemo")

words = sc.parallelize(["scala",
                        "java",
                        "hadoop",
                        "spark",
                        "akka",
                        "spark vs hadoop",
                        "pyspark",
                        "pyspark and spark"])

# 1.返回RDD中的元素数
# counts = words.count()
# print("单词个数:{}".format(counts))
#
# # 2.返回RDD中的所有元素
# coll = words.collect()
# print("RDD中所有数据:{}".format(coll))


# # 3.foreach(F):仅返回满足foreach内函数条件的元素
# def f(x): print(x)
# words.foreach(f)

# # 4.filter(F):返回一个新的RDD通过将F作用于每个元素后为True的元素
# words_filter = words.filter(lambda x: 'spark' in x)
# filtered = words_filter.collect()
# print("包含spark的单词:{}".format(filtered))

# # 5.map(F):返回一个新的RDD:通过将F作用于每个元素后返回的元素组成
# words_map = words.map(lambda x: (x, 1))  # 将每个元素转换为: key -> (key, 1)
# mapping = words_map.collect()
# print("经过map后的k-v对如下:{}".format(mapping))
