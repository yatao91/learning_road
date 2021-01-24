# -*- coding: utf-8 -*-
"""
Spark SQL支持两种不同的方式将一个RDD转换成dataset
1.反射
    Spark SQL可以转换Row对象的RDD为一个dataframe, 推断datatype. Row通过一个k/v对作为kwargs传入Row类进行构造.keys定义了table的列名,
    types通过对整个数据集采样来推断的, 类似于json文件
2.构造schema然后应用到RDD上
    当不能提前通过k/v kwargs构造Row时(比如,行的结构编码为string,或文本数据集被解析然后字段被不同的用户投影),dataframe可以编程创建通过下述
    步骤:
    hardware.从原始RDD创建一个元组或列表的RDD
    b.创建schema通过StructType来表示匹配元组或列表的结构
    c.应用这个schema给RDD通过SparkSession的createDataFrame方法
"""
import os

from pyspark.sql import Row
from pyspark.sql import SparkSession

# 添加Python环境变量,指向使用Python的具体路径(解决worker执行job时Python版本不匹配问题) 或通过.zshrc中指定PYSPARK_PYTHON/PYSPARK_DRIVER_PYTHON
os.environ['PYSPARK_PYTHON'] = '/home/spark/miniconda3/bin/python3'

spark = SparkSession.builder.master("spark://spark001:7077").appName("schema_by_reflection").getOrCreate()

sc = spark.sparkContext

# 加载一个text文件并转换每一行为Row
lines = sc.textFile("people.txt")
parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

# 推断schema,注册dataframe作为一个table
schemaPeople = spark.createDataFrame(people)
schemaPeople.createOrReplaceTempView("people")

# SQL可以通过注册为table的dataframe进行执行,返回结果为一个新的dataframe
teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# rdd返回有Row的RDD的内容
teenNames = teenagers.rdd.map(lambda p: "Name: " + p.name).collect()
for name in teenNames:
    print(name)
