import requests
from pprint import pprint
import base64
import os
from docx import Document
import re
import json

url = 'https://wenku.baidu.com/gsearch/rec/pcviewdocrec2023?sessionId=0930167378-0933622666--&docId=d2bad21fe3bd960590c69ec3d5bbfd0a7956d5d8&query=20%E4%BB%A5%E5%86%85%E5%8A%A0%E5%87%8F%E6%B3%95%E7%BB%83%E4%B9%A0%E9%A2%98(100%E9%A2%98)50%E4%BB%BD-20%E4%BB%A5%E5%86%85%E5%8A%A0%E6%B3%95%E9%A2%98%E7%9B%AE&recPositions=catalog%2Ctoplist'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}
# 发送请求
response = requests.get(url=url, headers=headers)
for i in response.json()['data']['catalogDoc']:
    pic = i['pic']
    print(pic)
