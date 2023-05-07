'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-05-06 19:13:56
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-05-07 13:49:04
FilePath: \py\基本教程\1.py
Description: 

Copyright (c) 2023 by 蔡沄金, All Rights Reserved. 
'''

s = "张三"
# gbk 编码中，一个中文占两个字节
print(s.encode(encoding="GBK"))
# utf-8 编码中，一个中文占三个字节
print(s.encode(encoding="utf-8"))
byte = s.encode(encoding="GBK")
print(byte.decode(encoding="GBK"))

byte = s.encode(encoding="utf-8")
print(byte.decode(encoding="utf-8"))
