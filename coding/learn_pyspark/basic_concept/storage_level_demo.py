# -*- coding: utf-8 -*-
"""
StorageLevel:RDD存储级别
DISK_ONLY = StorageLevel(True, False, False, False, 1)
DISK_ONLY_2 = StorageLevel(True, False, False, False, 2)
MEMORY_AND_DISK = StorageLevel(True, True, False, False, 1)
MEMORY_AND_DISK_2 = StorageLevel(True, True, False, False, 2)
MEMORY_AND_DISK_SER = StorageLevel(True, True, False, False, 1)
MEMORY_AND_DISK_SER_2 = StorageLevel(True, True, False, False, 2)
MEMORY_ONLY = StorageLevel(False, True, False, False, 1)
MEMORY_ONLY_2 = StorageLevel(False, True, False, False, 2)
MEMORY_ONLY_SER = StorageLevel(False, True, False, False, 1)
MEMORY_ONLY_SER_2 = StorageLevel(False, True, False, False, 2)
OFF_HEAP = StorageLevel(True, True, True, False, 1)
"""
from pyspark import SparkContext
import pyspark


sc = SparkContext(master="spark://spark001:7077", appName="storage_level_app")

rdd1 = sc.parallelize([1, 2])
rdd1.persist(storageLevel=pyspark.StorageLevel.MEMORY_AND_DISK_2)
rdd1.getStorageLevel()
print(rdd1.getStorageLevel())
