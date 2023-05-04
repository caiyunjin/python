'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-26 17:33:13
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-05-04 08:56:07
FilePath: \py\可视化\pyecharts\01_json数据格式.py
Description: json是一种轻量化数据存储，通用于各种编程语言

Copyright (c) 2023 by 蔡沄金, All Rights Reserved. 
'''

import json

# json格式是字典或是列表内部嵌套字典
# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [
    {"name": "张大山", "age": 11},
    {"name": "王大锤", "age": 13},
    {"name": "赵小虎", "age": 16},
]
json_str = json.dumps(data, ensure_ascii=False)  # 转成json，ensure_ascii=False为不使用ascii码
print(type(json_str))
print(json_str)
# 准备字典，将字典转换为JSON
d = {"name": "周杰轮", "addr": "台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)
# 将JSON字符串转换为Python数据类型[{k: v, k: v}, {k: v, k: v}]
s = '[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'
l = json.loads(s)
print(type(l))
print(l)
# 将JSON字符串转换为Python数据类型{k: v, k: v}
s = '{"name": "周杰轮", "addr": "台北"}'
d = json.loads(s)
print(type(d))
print(d)
