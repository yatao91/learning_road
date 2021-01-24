# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession


spark = SparkSession.builder.master("spark://spark001:7077").appName("create_dataframe_demo").getOrCreate()

df = spark.read.json("people.json")

"""
# 展示dataframe内容
df.show()

# 使用树结构展示dataframe的schema
df.printSchema()

# select name列
df.select("name").show()

# 对年龄列值做加一处理
df.select(df["name"], df["age"] + 1).show()

# 查询年龄大于21的
df.filter(df["age"] > 21).show()

# 使用年龄分组并计数
df.groupBy("age").count().show()

# 注册dataframe作为一个SQL临时视图: session作用域, 如果创建临时视图的session结束了, 临时视图也将消失
df.createOrReplaceTempView("people")
sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()

# 注册dataframe作为一个全局临时视图
df.createGlobalTempView("people")

# 全局临时视图绑定到系统保留数据库`global_temp`上
spark.sql("SELECT * FROM global_temp.people").show()

# 全局临时视图是跨session使用的
spark.newSession().sql("SELECT * FROM global_temp.people").show()
"""
