# -*- coding: utf-8 -*-
import os
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = "/home/spark/spark/miniconda3/bin/python3"

spark = SparkSession.builder.master("spark://spark001:7077").appName("test_production_es_data").getOrCreate()

df = spark.read\
    .format("org.elasticsearch.spark.sql")\
    .option("es.nodes", "192.168.0.111")\
    .option("es.port", "9288")\
    .option("es.resource", "data-warehouse-zhongzhao-huatai-bid-result-v2-201807/doc")\
    .load()

# 1.查看dataframe的数据结构--树状结构展示
df.printSchema()

# 2.获取title列数据(
# df.select("title").show()

# 3.访问dataframe列的两种形式(推荐使用后者)
# print(df.title)
# print(df['title'])

# 4.访问es中的object类型字段(object字段无法读取)
bid_company_df = df.select("bid_company")
print(bid_company_df, dir(bid_company_df))

# 5.访问es中的object类型字段的子字段(hardware.b)(无法检索到object类型子字段)
# df.select("bid_company.name").show()

# 创建es索引的临时视图(因object字段失败)
# df.createOrReplaceTempView("es_index")
# sqlDF = spark.sql("SELECT bid_company.name FROM es_index")
# sqlDF.show()
