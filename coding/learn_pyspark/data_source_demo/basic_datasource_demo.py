# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession


def basic_datasource_example(spark):
    # generic load/save functions
    df = spark.read.load("users.parquet")
    df.select("name", "favorite_color").write.save("namesAndFavColors.parquet")

    # 分区可以用在save和saveAsTable方法上当用dataset API时
    df.write.partitionBy("favorite_color").format("parquet").save("namesPartByColor.parquet")

    # 可以在单表上同时使用分区和分桶
    df = spark.read.parquet("users.parquet")
    (df
     .write
     .partitionBy("favorite_color")
     .bucketBy(42, "name")
     .saveAsTable("people_partitioned_bucketed"))

    # 手动指定加载选项,例如:dataframe从其他数据源类型加载的可以转换为其他的类型
    df = spark.read.load("people.json", format="json")
    df.select("name", "age").write.save("namesAndAges.parquet", format="parquet")

    # 手动指定加载CSV文件选项
    df = spark.read.load("people.csv", format="csv", seq=":", inferSchema="True", header="true")

    # 手动指定加载ORC文件选项,例如:可以控制布隆过滤器和字典编码配置
    df = spark.read.orc("users.orc")
    (df.write.format("orc")
     .option("orc.bloom.filter.columns", "favorite_color")
     .option("orc.dictionary.key.threshold", "1.0")
     .save("users_with_options.orc"))

    # 基于文件的数据源,桶化和排序或分区在输出上可以作用在持久化表上
    df.write.bucketBy(42, "name").sortBy("age").saveAsTable("people_bucketed")

    # 除了用read API加载文件到一个dataframe然后查询dataframe之外, 可以直接使用SQL查询文件
    df = spark.sql("SELECT * FROM parquet.`users.parquet`")


if __name__ == '__main__':

    spark = SparkSession.builder.appName("python spark sql data source demo").getOrCreate()

    basic_datasource_example(spark)

    spark.stop()
