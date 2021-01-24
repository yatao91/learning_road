# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext


conf = SparkConf().setMaster("spark://spark001:7077").setAppName("spark_on_es_conf_demo")

# 通过设置具体每项的值用来设置spark操作es时的配置项
conf.set("es.index.auto.create", "true")

sc = SparkContext(conf=conf)
