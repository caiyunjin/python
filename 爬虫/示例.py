'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-26 17:34:55
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-04-26 20:09:31
FilePath: \python\爬虫\1.requests.py
Description: 

'''
import requests
from bs4 import BeautifulSoup

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}  # 伪装成浏览器
for start_num in range(0, 250, 25):
    content = requests.get(
        f'https://movie.douban.com/top250?start={start_num}', headers=head
    ).text
    soup = BeautifulSoup(content, 'html.parser')
    all_titles = soup.findAll('span', attrs={'class': 'title'})
    for title in all_titles:
        title_str = title.string
        if '/' not in title_str:
            print(title_str)
