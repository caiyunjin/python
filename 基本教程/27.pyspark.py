'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-24 20:28:14
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-04-25 19:00:27
FilePath: \python\基本教程\27.pyspark.py
Description: 

'''
# 大数据
'''
from pyspark import SparkContext, SparkConf
import os

os.environ[
    'PYSPARK_PYTHON'
] = 'C:/Users/caiyunjin/AppData/Local/Programs/Python/Python311/python.exe'
# 创建sparkconf类对象
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)
# 通过paralelize方法将python对象加载到spark，成为RDD对象
rdd1 = sc.parallelize(['1 2 3', '4 5 a'])
rdd2 = sc.parallelize((1, 2, 3))
rdd3 = sc.parallelize('abc')  # 字符会被拆分
rdd4 = sc.parallelize({1, 2, 3})
rdd5 = sc.parallelize({'key1': 'value1', 'key2': 'value2'})  # 只获取key

# 通过map方法处理，*10
def func(data):
    return data * 10

rdd6 = rdd1.map(func())

# rdd6 = rdd1.map(lambda x: x * 10)  # 简单函数直接用 lambda
# print(rdd6.collect())

# faltMap 去除嵌套
# rdd7 = rdd1.flatMap(lambda x: x.split(' '))
# print(rdd7.collect())

# reduceByKey 针对key-value RDD，按照key分组，然后根据提供的局和逻辑完成组内value的聚合操作
rdd8 = sc.parallelize([('男', 100), ('男', 99), ('女', 98), ('女', 97)])
res = rdd8.reduceByKey(lambda a, b: a + b)
print(res.collect())

# 查看RDD内容
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

# 通过textfile把文件内容转变为RDD对象
rdd = sc.textFile('./test.txt')
print(rdd.collect())
sc.stop()

# 实例
from pyspark import SparkContext, SparkConf
import os

os.environ[
    'PYSPARK_PYTHON'
] = 'C:/Users/caiyunjin/AppData/Local/Programs/Python/Python311/python.exe'

conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf=conf)
# 读取数据文件
rdd = sc.textFile('D:/test.txt')
# 取出全部单词
word_rdd = rdd.flatMap(lambda X: X.split(' '))
# 将所有单词转成元组，单词为key，value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# 分组求和，每个单词出现过几次
res = word_with_one_rdd.reduceByKey(lambda a, b: a + b)
print(res.collect())
sc.stop()


from pyspark import SparkContext, SparkConf
import os

os.environ[
    'PYSPARK_PYTHON'
] = 'C:/Users/caiyunjin/AppData/Local/Programs/Python/Python311/python.exe'

conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf=conf)
# Filter 过滤
rdd = sc.parallelize([1, 2, 3, 4, 5])
res = rdd.filter(lambda num: num % 2 == 0)
print(res.collect())
sc.stop()

# distinct 去重
# rdd = sc.parallelize([1, 2, 2, 3, 4, 5])
# res = rdd.distinct()

# sortby 数据排序
# 读取数据文件
rdd = sc.textFile('D:/test.txt')
# 取出全部单词
word_rdd = rdd.flatMap(lambda X: X.split(' '))
# 将所有单词转成元组，单词为key，value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# 分组求和，每个单词出现过几次
res = word_with_one_rdd.reduceByKey(lambda a, b: a + b)
# 对结果排序
final_rdd = res.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
# ascending=False 降序 True 升序
# numPartitions=1 全局排序需要设置分区数为1


# 数据输出
from pyspark import SparkContext, SparkConf
import os

os.environ[
    'PYSPARK_PYTHON'
] = 'C:/Users/caiyunjin/AppData/Local/Programs/Python/Python311/python.exe'
os.environ['HADOOP_HOME'] = 'D:/hadoop-3.3.5'
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
conf.set('spark.default.parallelism', '1')  # 修改分区数，数量为1
sc = SparkContext(conf=conf)
rdd = sc.parallelize([1, 2, 3, 4, 5])
# rdd = sc.parallelize([1, 2, 3, 4, 5],1)设置分区为1 同conf.set('spark.default.parallelism', '1')
# collect 输出RDD为list
# reduce  将RDD进行两两聚合
# take(N)  去前N个数据
# count 计算RDD总共多少条数据
rdd.saveAsTextFile('D:/1')
sc.stop()
'''
