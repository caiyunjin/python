"""
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-05-02 13:50:20
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-05-02 14:54:48
FilePath: \py\Django\mysite\myapp\models.py
Description: 

Copyright (c) 2023 by 蔡沄金, All Rights Reserved. 
"""
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
