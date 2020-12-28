# import ssl
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# ssl._create_default_https_context = ssl._create_unverified_context
#
#
# class GetTitleInfo:
#     def __init__(self, url):
#         self.url = url
#         self.title_info = []
#
#     def get_info(self):
#         resp = urlopen(self.url)
#         soup = BeautifulSoup(resp.read(), 'lxml')
#         info = soup.find_all('a')
#         for tag in info:
#             if tag:
#                 if tag.text and len(tag.text) > 3:
#                     row = dict()
#                     row['title'] = tag.text
#                     row['href'] = tag.get('href')
#                     self.title_info.append(row)
#         return self.title_info

import requests
import re
from lxml import etree
import time

if __name__ == '__main__':
    start_time = time.time()
    # print('正在爬取。。。')
    fp = open('test.txt', 'w', encoding='utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59'
    }
    # url = 'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/china_1.jsonp?cb=world'
    url = 'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/world_1.jsonp?cb=world'
    params = {
        'cb': 'world'
    }
    response = requests.get(url=url, params=params, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    ex1 = '"id".*?"title":"(.*?)","keywords"'
    ex2 = '"brief".*?,"url":"(.*?)"'
    title = re.findall(ex1, page_text)
    url = re.findall(ex2, page_text)

    for i in range(len(url)):
        res = requests.get(url=url[i], headers=headers)
        res.encoding = 'utf-8'
        response = res.text
        tree = etree.HTML(response)
        data = tree.xpath('//*[@id="content_area"]//text()')
        data = ''.join(data).strip().replace(' ', '')
        fp.write(title[i] + '\n' + data)

    end_time = time.time()
    # print('爬取结束！用时{}s'.format(end_time - start_time))
