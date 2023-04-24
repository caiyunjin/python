'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-24 20:28:14
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-04-24 20:35:49
FilePath: \python\基本教程\27.pyspark.py
Description: 

'''
# 大数据

from pyspark import SparkContext, SparkConf

# 创建sparkconf类对象
conf = SparkConf().setMaster('local[*]').setAppName('test_spark_app')
# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)
print(sc.version)
sc.stop()
