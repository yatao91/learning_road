# -*- coding: utf-8 -*-
from pyspark import SparkContext

logFile = "README.md"
sc = SparkContext(master="spark://spark001:7077", appName="demo02")

logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'hardware' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with hardware: %i, lines with b: %i" % (numAs, numBs))
