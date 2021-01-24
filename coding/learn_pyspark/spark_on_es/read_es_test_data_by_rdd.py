# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("spark://spark001:7077").setAppName("demo")
sc = SparkContext(conf=conf)

# es相关配置
es_common_data_conf = {"es.nodes": "192.168.0.111",
                       "es.port": "9288",
                       "es.resource": "data-warehouse-zhongzhao-huatai-bid-result-v2-201807/doc",
                       "es.read.field.exclude": "html_text,content,manual_check,deduplication,deduplication_weight"}

es_company_info_conf = {"es.nodes": "192.168.0.111",
                        "es.port": "9288",
                        "es.resource": "data-warehouse-zhongzhao-company-info-v2-re-extract/doc",
                        "es.read.field.exclude": "address,province,city,total_count"}

rdd_01 = sc.newAPIHadoopRDD(inputFormatClass="org.elasticsearch.hadoop.mr.EsInputFormat",
                            keyClass="org.apache.hadoop.io.NullWritable",
                            valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
                            conf=es_common_data_conf)

rdd_02 = sc.newAPIHadoopRDD(inputFormatClass="org.elasticsearch.hadoop.mr.EsInputFormat",
                            keyClass="org.apache.hadoop.io.NullWritable",
                            valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
                            conf=es_company_info_conf)


def pop_id(element):
    """map使用此函数仅使用element中的doc数据"""
    if element:
        _id, doc = element
    return doc


rdd_01_1 = rdd_01.map(pop_id)
rdd_02_2 = rdd_02.map(pop_id)
