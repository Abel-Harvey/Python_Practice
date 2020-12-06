"""
author: abel
date: 12-01-2020
version: v0.1
"""
import urllib.request as req
import urllib.parse as par
from gzip import decompress as decode
import json


class GetCityForecast:
    """
    作用:当创建新的对象时，将返回表示该城市天气情况的相关信息\n
    内置方法: display() 调用后显示处理好的各种数据，其他方法无需显式调用\n
    """
    def __init__(self, city_name):
        """
        初始化相关的变量，进行数据的获取，对获取状态进行初步的判断\n
        进行初步的数据解析\n
        :param city_name: 城市名，在实例化对象时，需要加上该变量\n
        """
        self.city_name = city_name
        self.yesterday = []
        self.today = []
        self.forecast = []
        self.cold_reminder = []
        self.somatosensory_temperature = []
        # 分别为：城市名，昨日天气，今日天气，未来4天天气，感冒提醒，体感温度

        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + par.quote(city_name)
        self.url_data = req.urlopen(url).read()
        # 解析该城市数据，将反馈的数据存在该变量中
        self.url_data = decode(self.url_data).decode('utf-8')
        # 将数据解码，使人类可读

        self.data_dict = json.loads(self.url_data)
        # 拓展为字典类型，便于后续的进一步处理
        if self.data_dict['desc'] == 'OK':
            # 判断数据状态，如果成功，则状态码为1000，并进行下一步的处理
            self.status_code = 1000
            self.data_process()
        else:
            # 否则得到该状态码，并报错
            self.status_code = 1002
            # self.error_status()

    def data_process(self):
        """
        一旦检测到返回状态正常，则立即着手进行数据的解析\n
        解析后，将会把init中的五个列表填充完毕，供其他使用\n
        :return: None But Normal
        """
        city_info = self.data_dict.get('data').copy()
        # 城市天气详情
        self.yesterday = city_info.get('yesterday')
        # 得到昨天的天气情况
        temp = ['日期', self.yesterday['date'], '最高温度', self.yesterday['high'], '风向',
                self.yesterday['fx'], '最低温度', self.yesterday['low'], '风力']

        fl = self.yesterday['fl']
        fl = fl.replace('<![CDATA[', '')
        fl = fl.replace(']]>', '')
        temp.append(fl)

        temp.append('天气类型')
        temp.append(self.yesterday['type'])

        self.yesterday = temp
        # 通过一系列处理后，得到新的列表类型的"昨日"数据
        del temp

        self.cold_reminder = city_info.get('ganmao')
        # 感冒提醒
        self.somatosensory_temperature = city_info.get('wendu')
        # 体感温度

        self.forecast = city_info.get('forecast')
        # 城市未来且包括今天在内的5天天气预报（临时的）

        # 解析数据
        forecast_list = []
        # 设置一个数据的列表，记录五天的预报数据
        for i in range(5):
            forecast_list.append('日期')
            forecast_list.append(self.forecast[i].get('date'))

            forecast_list.append('最高温度')
            forecast_list.append(self.forecast[i].get('high'))

            forecast_list.append('风向')
            forecast_list.append(self.forecast[i].get('fengxiang'))

            forecast_list.append('最低温度')
            forecast_list.append(self.forecast[i].get('low'))

            forecast_list.append('风力')
            fl = self.forecast[i].get('fengli')
            fl = fl.replace('<![CDATA[', '')
            fl = fl.replace(']]>', '')
            forecast_list.append(fl)

            forecast_list.append('天气类型')
            forecast_list.append(self.forecast[i].get('type'))
        self.forecast = forecast_list
        # 将此赋值给类的属性
        del forecast_list

        self.today = self.forecast[0:12]
        # 将第一个数据给today，作为"今日天气"
        self.forecast = self.forecast[12::]
        # "预测天气"
        del city_info
        # print(self.somatosensory_temperature)

    # def error_status(self):
    #     """
    #     天气查询出错时，将调用该函数，并使程序结束\n
    #     该函数作测试用，后续将取消\n
    #     :return:abort
    #     """
    #     status_code = self.status_code
    #     print("Error::{}! 无法查询到相关城市，请检测输入或网络连接!".format(status_code))
    #     exit(3)

    def display(self):
        print('{}的天气状况'.format(self.city_name))
        print('昨日天气情况：', self.yesterday)
        print('今日天气：', self.today)
        print('未来天气：', self.forecast)
        print('感冒提醒：', self.cold_reminder)
        print('体感温度：', self.somatosensory_temperature)


if __name__ == '__main__':
    city = '沈阳'
    data = GetCityForecast(city)
    # data.display()
