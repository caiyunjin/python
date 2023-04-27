'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-27 17:46:21
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-04-27 18:04:19
FilePath: \python\爬虫\百度文库.py
Description: 

'''

import re
import requests

session = requests.session()


# 发送请求
def fetch_url(url):
    print(session.get(url).content.decode('utf-8'))
    return session.get(url).content.decode('utf-8')


def get_doc_id(url):
    re.findall(r'doc_id=(\d+)', url)[0]


# 主函数
def main():
    url = input(r'输入网址:')
    # 请求
    fetch_url(url)


if __name__ == '__main__':
    main()
