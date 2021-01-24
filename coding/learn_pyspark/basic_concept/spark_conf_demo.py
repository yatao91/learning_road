# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("spark_conf_app").setMaster("spark://spark001:7077")

sc = SparkContext(conf=conf)
