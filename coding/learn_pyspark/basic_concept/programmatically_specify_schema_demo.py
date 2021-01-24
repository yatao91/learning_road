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
from pyspark.sql import SparkSession
from pyspark.sql.types import *

os.environ['PYSPARK_PYTHON'] = '/home/spark/miniconda3/bin/python3'

spark = SparkSession.builder.master("spark://spark001:7077").appName("programmatically_schema_app").getOrCreate()
sc = spark.sparkContext

# 加载文本文件然后转换文本文件的每一行为Row对象
lines = sc.textFile("people.txt")
parts = lines.map(lambda l: l.split(","))

# 每行转换为一个元组
people = parts.map(lambda p: (p[0], p[1].strip()))

# schema编码到一个string
schemaString = "name age"

fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
schema = StructType(fields)

# 应用schema到RDD上
schemaPeople = spark.createDataFrame(data=people, schema=schema)

# 使用dataframe创建一个临时视图
schemaPeople.createOrReplaceTempView("people")

# SQL可以在dataframe上执行
results = spark.sql("SELECT name FROM people")

results.show()
