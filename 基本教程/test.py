"""
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-05-02 21:50:16
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-05-03 17:25:09
FilePath: \py\基本教程\test.py
Description: 

Copyright (c) 2023 by 蔡沄金, All Rights Reserved. 
"""


def outer(logo):

    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner


fn1 = outer("黑马程序员")
fn1("大家好")