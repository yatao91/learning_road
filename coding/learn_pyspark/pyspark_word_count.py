# -*- coding: UTF-8 -*-
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("wordCount")
sc = SparkContext(conf=conf)

input_file = sc.textFile("input.txt")
words = input_file.flatMap(lambda line: line.split(" "))
counts = words.map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)
counts.saveAsTextFile("output.txt")
