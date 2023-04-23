'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-23 20:47:32
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-04-23 21:28:36
FilePath: \python\基本教程\26.pyecharts.py
Description: 
'''
from pyecharts.charts import Line

line = Line()
line.add_xaxis(['中国', '美国', '韩国'])
line.add_yaxis('GDP', [120, 132, 101])
line.render()
