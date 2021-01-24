# -*- coding: utf-8 -*-
"""
通过pyspark dataframe索引数据至es
"""
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("spark://spark001:7077").appName("index_via_pyspark_dataframe").getOrCreate()

df = spark.createDataFrame([{"num": i} for i in range(10)])

df = df.drop("_id")

df.write\
    .format("org.elasticsearch.spark.sql")\
    .option("es.nodes", "192.168.0.111")\
    .option("es.port", "9288")\
    .option("es.resource", "spark/doc")\
    .save()
