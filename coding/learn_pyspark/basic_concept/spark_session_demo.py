# -*- coding: utf-8 -*-
"""
SparkSession:Spark功能入口
"""
from pyspark.sql import SparkSession

# 使用SparkSession.builder构造sparkSession
spark = SparkSession.builder.appName("spark_session_demo").config("spark.some.conf.option", "some-value").getOrCreate()
