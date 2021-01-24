# -*- coding: utf-8 -*-
"""
通过pyspark RDD索引数据至es
"""
from pyspark import SparkContext
import json

sc = SparkContext(master="spark://spark001:7077",
                  appName="index_via_pyspark_rdd")

rdd = sc.parallelize([{"num": i} for i in range(10)])


def remove_id(doc):
    """
    剔除doc中的_id字段
    :param doc:
    :return:
    """
    doc.pop("_id", "")
    return doc


new_rdd = rdd.map(remove_id).map(json.dumps).map(lambda x: ('key', x))

new_rdd.saveAsNewAPIHadoopFile(
    path='-',
    outputFormatClass="org.elasticsearch.hadoop.mr.EsOutputFormat",
    keyClass="org.apache.hadoop.io.NullWritable",
    valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
    conf={
        "es.nodes": "192.168.0.111",
        "es.port": "9288",
        "es.resource": "spark/doc",
        "es.input.json": "true"
    }
)
