# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession

logFile = "README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('hardware')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with hardware: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
