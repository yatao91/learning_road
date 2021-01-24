# -*- coding: utf-8 -*-
"""
通过pyspark.sql写入/读取es数据
"""
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.types import *


conf = SparkConf().setMaster("spark://spark001:7077").setAppName("pyspark-es-test")
sc = SparkContext(conf=conf)
sqlctx = SQLContext(sc)

schema = StructType([
    StructField("id", StringType(), True),
    StructField("uname", StringType(), True)
])

data = [('1', 'ss'), ('2', 'dd'), ('3', 'ff_update'), ('4', '嘻嘻嘻')]

save_df = sqlctx.createDataFrame(data, ['id', 'uname'])
save_df.show(truncate=False)

# 写入数据至es
save_df.write\
    .format("org.elasticsearch.spark.sql")\
    .option("es.nodes", "192.168.0.111")\
    .option("es.port", "9288")\
    .option("es.resource", "spark/doc")\
    .option("es.mapping.id", "id")\
    .mode("append")\
    .save()

# 从es读取数据
df = sqlctx.read\
    .format("org.elasticsearch.spark.sql")\
    .option("es.nodes", "192.168.0.111")\
    .option("es.port", "9288")\
    .option("es.resource", "spark/doc")\
    .load()

df.registerTempTable('spark_doc')

test_df = sqlctx.sql("SELECT * FROM spark_doc ORDER BY id DESC LIMIT 10")

test_df.show()
