# -*- coding: utf-8 -*-
"""
broadcast variable 共享广播变量
广播变量允许开发人员在每台机器上缓存一个只读变量.
例如:可以使用它们为每个节点提供一个大型输入数据集的副本
spark也尝试使用有效的广播算法来分配广播变量, 以降低通信成本
当多个不同计算阶段需要同样的数据时 可以显示的使用广播变量是比较有用的.
"""
from pyspark import SparkContext

sc = SparkContext(master="spark://spark001:7077", appName="broadcastdemo")

words_broad_var = sc.broadcast(value=["scala", "java", "hadoop", "spark", "akka"])

# value代表的是广播变量
broad_var_data = words_broad_var.value
print("广播变量:{}".format(broad_var_data))

# 可以使用index索引广播变量的具体值--因广播变量是list
element = words_broad_var.value[2]
print("广播变量的第3个元素:{}".format(element))
