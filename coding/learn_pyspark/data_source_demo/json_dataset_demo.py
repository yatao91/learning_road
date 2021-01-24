# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("json_dataset_demo").getOrCreate()

sc = spark.sparkContext

# json数据集指向路径. path可以是一个文本文件, 或者一个存储文本文件的字典
path = "people.json"
peopleDF = spark.read.json(path)

# 推断出的schema可以通过使用printSchema()来进行可视化
peopleDF.printSchema()

# 通过dataframe创建一个临时视图
peopleDF.createOrReplaceTempView("people")

# 执行SQL查询
teenagerNamesDF = spark.sql("SELECT name FROM people WHERE age BETWEEN 13 AND 19")
teenagerNamesDF.show()

# dataframe可以通过一个json数据集创建, json数据集表现为:一个RDD[string],一个string表示一个json对象
jsonStrings = ['{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}']
otherPeopleRDD = sc.parallelize(jsonStrings)
otherPeople = spark.read.json(otherPeopleRDD)
otherPeople.show()
