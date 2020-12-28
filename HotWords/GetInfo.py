import requests
from lxml import etree
import re
import time


class GetInfo:
    def __init__(self, target):
        self.target = target
        # 目标类型--> [新闻、国内、国际、社会、法治、文娱、科技、生活]
        self.url_list = ['https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/news_1.jsonp?cb=news',
                         'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/china_1.jsonp?cb=china',
                         'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/world_1.jsonp?cb=world',
                         'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/society_1.jsonp?cb=society',
                         'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/law_1.jsonp?cb=law',
                         'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/ent_1.jsonp?cb=ent',
                         'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/tech_1.jsonp?cb=tech',
                         'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/life_1.jsonp?cb=life']
        self.url = self.url_list[self.target]
        # 请求网址
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                            AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.125 '
                          'Safari/537.36 Edg/84.0.522.59'
        }
        # 请求头
        self.text = ''
        # 文本文件
        self.cost_time = 0

    def get_web_info(self):
        file = open('test.txt', 'w', encoding='utf-8')
        # 爬取后的文件所保存的地址
        par_list = ['news', 'china', 'world', 'society', 'law', 'ent', 'tech', 'life']
        param = {'cb': '{}'.format(par_list[self.target])}
        # 请求参数
        start_time = time.time()
        resp = requests.get(url=self.url, params=param, headers=self.header)
        resp.encoding = 'utf-8'
        self.text = resp.text
        tag1 = '"id".*?"title":"(.*?)","keywords"'
        tag2 = '"brief".*?,"url":"(.*?)"'
        news_title = re.findall(tag1, self.text)
        news_url = re.findall(tag2, self.text)

        for i in range(len(news_url)):
            res = requests.get(url=news_url[i], headers=self.header)
            res.encoding = 'utf-8'
            resp = res.text
            tree = etree.HTML(resp)
            data = tree.xpath('//*[@id="content_area"]//text()')
            data = ''.join(data).strip().replace(' ', '')
            file.write(news_title[i] + '\n' + data)

        end_time = time.time()
        self.cost_time = end_time-start_time
        file.close()


if __name__ == '__main__':
    text = GetInfo(2)
    text.get_web_info()
    print(text.cost_time)
