'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-27 17:46:21
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-04-28 07:44:58
FilePath: \python\爬虫\百度文库.py
Description: 
88c69e6a0740be1e640e9a35
'''

import re
import requests

session = requests.session()
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}


# https://wenku.baidu.com/gsearch/rec/pcviewdocrec2023?sessionId=2188684108-2188684108--&docId=85cf2f9b66ec102de2bd960590c69ec3d4bbdb10&query=故事大全睡前故事&recPositions=catalog,toplist
# 发送请求
def fetch_url(url):
    print(session.get(url).content.decode('utf-8'))
    return session.get(url).content.decode('utf-8')


def get_doc_id(url):
    print()
    re.findall(r'doc_id=(\d+)', url)[0]


# 主函数
def main():
    url = input(r'输入网址:')
    # 请求
    content = fetch_url(url)
    doc_id = get_doc_id(url)



if __name__ == '__main__':
    main()
