# -*- coding: utf-8 -*-
"""
sparkfile
spark通过SparkContext().addFile(path, recursive=False)来添加文件关联到这个spark job的每个节点上.
path:local file/HDFS file/HTTP URI/HTTPS URI/FTP URI.
访问这个文件通过: SparkFiles.get(fileName)来找到这个文件的下载地址
"""
from pyspark import SparkConf, SparkContext, SparkFiles

conf = SparkConf().setAppName("spark_file_demo").setMaster("spark://spark001:7077")
sc = SparkContext(conf=conf)

filename = "demo.txt"
filepath = "demo.txt"
sc.addFile(filepath)
print("文件绝对路径:{}".format(SparkFiles.get(filename)))
print("文件根路径:{}".format(SparkFiles.getRootDirectory()))
