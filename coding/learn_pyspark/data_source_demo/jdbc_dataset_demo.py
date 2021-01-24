# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("spark://spark001:7077").appName("jdbc_demo").getOrCreate()

# 1.通过read.option().load()形式
jdbcDF = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://192.168.0.111/su_spark") \
    .option("dbtable", "trips") \
    .option("user", "root") \
    .option("password", "123456") \
    .load()

jdbcDF.show()

# 2.通过read.jdbc()形式
jdbcDF2 = spark.read \
    .jdbc("jdbc:mysql://192.168.0.111", "su_spark.trips", properties={"user": "root", "password": "123456"})

jdbcDF2.show()

# 3.指定dataframe读取的列数据类型
jdbcDF3 = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://192.168.0.111") \
    .option("dbtable", "su_spark.trips") \
    .option("user", "root") \
    .option("password", "123456") \
    .option("customSchema", "dispatching_base_number STRING, trips INT") \
    .load()
jdbcDF3.show()

# Saving data to hardware JDBC source
jdbcDF.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql:dbserver") \
    .option("dbtable", "schema.tablename") \
    .option("user", "username") \
    .option("password", "password") \
    .save()

jdbcDF2.write \
    .jdbc("jdbc:postgresql:dbserver", "schema.tablename",
          properties={"user": "username", "password": "password"})

# Specifying create table column data types on write
jdbcDF.write \
    .option("createTableColumnTypes", "name CHAR(64), comments VARCHAR(1024)") \
    .jdbc("jdbc:postgresql:dbserver", "schema.tablename",
          properties={"user": "username", "password": "password"})
