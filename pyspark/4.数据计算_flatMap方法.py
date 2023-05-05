'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-26 17:33:14
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-05-05 08:46:31
FilePath: \py\pyspark\4.数据计算_flatMap方法.py
Description: 

Copyright (c) 2023 by 蔡沄金, All Rights Reserved. 
'''
"""
演示RDD的flatMap成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(["itheima itcast 666", "itheima itheima itcast", "python itheima"])

# 需求，将RDD数据里面的一个个单词提取出来
rdd2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())
sc.stop()