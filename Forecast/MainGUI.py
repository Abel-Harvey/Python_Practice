"""
author: abel
date: 12-01-2020
version: v0.2
"""
import wx
import GetData


class MainWindow:
    def __init__(self):
        self.app = wx.App(False)
        # False: 表示出错不在窗口显示
        self.window = wx.Frame(None, title='简易天气预报查询系统', size=(300, 420))
        # 设置主窗口信息，并居中出现
        self.window.Centre()
        self.panel = wx.Panel(self.window)

        self.btn_exit = wx.Button(self.panel, 1, '退出程序', pos=(110, 360))
        # 退出按钮
        self.btn_exit.Bind(wx.EVT_BUTTON, self.exit_app)
        # 退出按钮的事件绑定，只要按下就调用

        self.text_1 = wx.StaticText(self.panel, 2, '请输入正确的城市名: ', pos=(90, 20))
        # 提示性语句显示
        self.text_city_name = wx.TextCtrl(self.panel, 2, pos=(90, 50), size=(124, 21))
        # 输入框，将得到城市名字
        self.weather_type_text = wx.TextCtrl(self.panel, 2, pos=(350, 30), style=wx.TE_READONLY)
        self.weather_type_text.Show(False)
        # 天气类型显示框

        self.btn_query = wx.Button(self.panel, 3, '查询', pos=(110, 72))
        # 查询按钮
        self.btn_query.Bind(wx.EVT_BUTTON, self.get_query_status)
        # 将查询按钮与状态按钮函数绑定，且默认显示今日天气

        self.btn_yest = wx.Button(self.panel, 4, '昨日天气', pos=(110, 30))
        # 昨日天气按钮，默认关闭
        self.btn_yest.Show(False)
        self.btn_yest.Bind(wx.EVT_BUTTON, self.yest_info)

        self.btn_fore = wx.Button(self.panel, 4, '未来天气', pos=(110, 60))
        # 未来天气按钮，默认关闭
        self.btn_fore.Show(False)
        self.btn_fore.Bind(wx.EVT_BUTTON, self.fore_info)
        # 查询未来天气按钮绑定

        self.btn_refresh = wx.Button(self.panel, 5, '重新查询', pos=(110, 90))
        # 刷新重查按钮，默认关闭
        self.btn_refresh.Show(False)
        self.btn_refresh.Bind(wx.EVT_BUTTON, self.refresh)
        # 刷新按钮绑定

        self.basic_data1 = wx.TextCtrl(self.panel, 6, pos=(180, 30), size=(150, 120),
                                       style=(wx.TE_READONLY | wx.TE_MULTILINE))
        # 今日和昨天的基本天气显示框,默认关闭
        self.basic_data1.Show(False)

        self.reminder_data = wx.TextCtrl(self.panel, 6, pos=(180, 140), size=(150, 90),
                                         style=(wx.TE_READONLY | wx.TE_MULTILINE))
        # 今日和昨天的提醒信息显示框，默认关闭
        self.reminder_data.Show(False)

        # 以下是一组常见天气图片
        self.no_img = wx.Image('img/today/test.jpg', wx.BITMAP_TYPE_ANY)
        self.no_img = self.no_img.ConvertToBitmap()
        # 测试用图
        self.sunny = wx.Image('img/sunny.png', wx.BITMAP_TYPE_ANY)
        self.sunny = self.sunny.ConvertToBitmap()
        # 晴天
        self.sunny_2 = wx.Image('img/today/晴.jpg', wx.BITMAP_TYPE_ANY)
        self.sunny_2 = self.sunny_2.ConvertToBitmap()
        # 今日和昨天的晴天
        self.cloudy = wx.Image('img/cloudy.png', wx.BITMAP_TYPE_ANY)
        self.cloudy = self.cloudy.ConvertToBitmap()
        # 多云
        self.gloomy = wx.Image('img/gloom.png', wx.BITMAP_TYPE_ANY)
        self.gloomy = self.gloomy.ConvertToBitmap()
        # 阴天
        self.flurry = wx.Image('img/flurry.png', wx.BITMAP_TYPE_ANY)
        self.flurry = self.flurry.ConvertToBitmap()
        # 小雨
        self.moderate_rain = wx.Image('img/moderate_rain.png', wx.BITMAP_TYPE_ANY)
        self.moderate_rain = self.moderate_rain.ConvertToBitmap()
        # 中雨
        self.spate = wx.Image('img/spate.png', wx.BITMAP_TYPE_ANY)
        self.spate = self.spate.ConvertToBitmap()
        # 大雨
        self.rainstorm = wx.Image('img/rainstorm.png', wx.BITMAP_TYPE_ANY)
        self.rainstorm = self.rainstorm.ConvertToBitmap()
        # 暴雨
        self.mist = wx.Image('img/mist.png', wx.BITMAP_TYPE_ANY)
        self.mist = self.mist.ConvertToBitmap()
        # 雾
        self.shower = wx.Image('img/shower.png', wx.BITMAP_TYPE_ANY)
        self.shower = self.shower.ConvertToBitmap()
        # 阵雨
        self.thunder_shower = wx.Image('img/thunder_shower.png', wx.BITMAP_TYPE_ANY)
        self.thunder_shower = self.thunder_shower.ConvertToBitmap()
        # 雷阵雨
        self.light_snow = wx.Image('img/light_snow.png', wx.BITMAP_TYPE_ANY)
        self.light_snow = self.light_snow.ConvertToBitmap()
        # 小雪
        self.moderate_snow = wx.Image('img/moderate_snow.png', wx.BITMAP_TYPE_ANY)
        self.moderate_snow = self.moderate_snow.ConvertToBitmap()
        # 中雪
        self.heavy_snow = wx.Image('img/heavy_snow.png', wx.BITMAP_TYPE_ANY)
        self.heavy_snow = self.heavy_snow.ConvertToBitmap()
        # 大雪
        self.thunderstorm = wx.Image('img/thunderstorm.png', wx.BITMAP_TYPE_ANY)
        self.thunderstorm = self.thunderstorm.ConvertToBitmap()
        # 暴雪
        self.hailstone = wx.Image('img/hailstone.png', wx.BITMAP_TYPE_ANY)
        self.hailstone = self.hailstone.ConvertToBitmap()
        # 冰雹
        self.sleety = wx.Image('img/sleety.png', wx.BITMAP_TYPE_ANY)
        self.sleety = self.sleety.ConvertToBitmap()
        # 雨夹雪

        self.show = wx.StaticBitmap(self.panel, 7, pos=(350, 50))
        self.show.Show(False)
        # 天气类型图形显示 测试用

        self.basic_data_f1 = wx.TextCtrl(self.panel, 6, pos=(180, 30), size=(170, 120),
                                         style=(wx.TE_READONLY | wx.TE_MULTILINE))
        self.basic_data_f1.Show(False)
        self.basic_data_f2 = wx.TextCtrl(self.panel, 6, pos=(380, 30), size=(170, 120),
                                         style=(wx.TE_READONLY | wx.TE_MULTILINE))
        self.basic_data_f2.Show(False)
        self.basic_data_f3 = wx.TextCtrl(self.panel, 6, pos=(580, 30), size=(170, 120),
                                         style=(wx.TE_READONLY | wx.TE_MULTILINE))
        self.basic_data_f3.Show(False)
        self.basic_data_f4 = wx.TextCtrl(self.panel, 6, pos=(780, 30), size=(170, 120),
                                         style=(wx.TE_READONLY | wx.TE_MULTILINE))
        self.basic_data_f4.Show(False)
        # 未来天气所显示的四天情况，默认关闭

        self.show_f1 = wx.StaticBitmap(self.panel, 7, pos=(200, 155))
        self.show_f1.Show(False)
        self.show_f2 = wx.StaticBitmap(self.panel, 7, pos=(400, 155))
        self.show_f2.Show(False)
        self.show_f3 = wx.StaticBitmap(self.panel, 7, pos=(600, 155))
        self.show_f3.Show(False)
        self.show_f4 = wx.StaticBitmap(self.panel, 7, pos=(800, 155))
        self.show_f4.Show(False)
        # 未来天气的图形显示，默认关闭

        # self.menubar = wx.MenuBar()
        # self.btn_today = wx.Button(self.panel, 5, '重新查询', pos=(110, 120))
        # self.btn_today.Bind(wx.EVT_BUTTON, self.get_query_status)
        self.window.Show(True)
        # 窗口显示
        self.app.MainLoop()
        # 程序主循环

        self.info = object()

    def get_query_status(self, e):
        """
        该方法将获取查询状态\n
        如果查询失败，将进行提醒，并让用户重新查询\n
        如果查询成功，则将为用户提供多种选择\n
        :param e:
        :return:
        """
        city_name = self.text_city_name.GetValue()
        # 获取文本框中输入的城市名
        self.info = GetData.GetCityForecast(city_name)
        # 将该信息存在类中的info属性中

        if city_name == '':
            # 判断输入信息是否为空
            msg = wx.MessageDialog(None, '请输入城市名!', 'Confirm', wx.OK | wx.ICON_ERROR)
            msg.ShowModal()
            return

        if self.info.status_code == 1002:
            # 查询其状态码，判断是否成功获取到了天气信息
            msg = wx.MessageDialog(None, '查询失败，请检测城市名或网络连接!', 'Confirm', wx.OK | wx.ICON_ERROR)
            # 失败时的情况
            get_msg = msg.ShowModal()
            if get_msg == wx.OK:
                pass
            else:
                pass
            # print('Error')
        else:
            # self.info.display()
            # print(self.info.today)
            # print(self.info.cold_reminder)
            # print(self.info.somatosensory_temperature)
            # 测试输出部分

            self.btn_query.Show(False)
            self.text_city_name.Clear()
            self.text_city_name.Update()
            # 查询按钮关闭及输入框信息更新

            self.text_1.Show(False)
            self.text_city_name.Show(False)
            # 提醒文字及输入框显示关闭

            self.btn_fore.Show(True)
            self.btn_yest.Show(True)
            self.btn_refresh.Show(True)
            # 其他查询功能按钮显示开启

            self.display(e, 1)
            # 调用

        e.Skip()

    def refresh(self, e):
        """
        状态刷新函数\n
        当按刷新按钮后，将初始化全部信息\n
        :return: None
        """
        self.btn_query.Show(True)
        self.text_city_name.Clear()
        # 查询按钮开启

        self.text_city_name.Show(True)
        self.text_1.Show(True)
        # 打开相关按钮

        self.btn_yest.Show(False)
        self.btn_fore.Show(False)
        self.btn_refresh.Show(False)
        # 关闭相关按钮
        # 思考：可能需要有初始化天气显示区域的情况，待完成后进行设置

        self.basic_data1.Clear()
        self.basic_data1.Show(False)
        self.reminder_data.Clear()
        self.reminder_data.Show(False)
        self.basic_data_f1.Show(False)
        self.basic_data_f2.Show(False)
        self.basic_data_f3.Show(False)
        self.basic_data_f4.Show(False)
        # 信息显示框关闭

        self.window.SetSize(300, 420)
        self.window.Centre()
        # 窗口调整

        self.btn_exit.SetPosition((110, 360))
        self.btn_yest.SetPosition((110, 30))
        self.btn_fore.SetPosition((110, 60))
        self.btn_refresh.SetPosition((110, 90))
        # 按钮调整

        self.show.Show(False)
        self.show.ClearBackground()

        self.clear()
        # 关掉未来天气的相关信息

        e.Skip()

    def today_info(self, e):
        """
        该函数仅调用今天的天气展示\n
        :param e:event
        :return:None
        """
        self.display(e, 1)
        # 显示今日天气

    def fore_info(self, e):
        """
        进行未来天气的查询\n
        目前会出现warning，如何解决？\n
        :param e:
        :return:
        """

        self.show.ClearBackground()
        self.show.Show(False)
        # 天气图片显示关闭

        self.weather_type_text.Clear()
        self.weather_type_text.Show(False)
        # 天气类型显示关闭

        self.basic_data_f1.Show(False)
        self.basic_data_f2.Show(False)
        self.basic_data_f3.Show(False)
        self.basic_data_f4.Show(False)
        # 未来天气的显示框关闭

        self.clear()
        # 清除未来天气的信息，避免残留

        self.display(e, 3)
        # 在主界面上显示未来天气

        e.Skip()

    def yest_info(self, e):
        """
        查询昨天的天气情况\n
        :param e:
        :return:
        """
        # yest_data = self.info.yesterday
        # print('昨日天气: ')
        # print(yest_data)

        self.basic_data_f1.Show(False)
        self.basic_data_f2.Show(False)
        self.basic_data_f3.Show(False)
        self.basic_data_f4.Show(False)
        # 未来天气的显示框关闭

        self.show.ClearBackground()
        # 点击昨天按钮，清楚当前的天气图像
        self.display(e, 2)

        self.clear()
        # 清除未来天气的信息

        e.Skip()

    def display(self, e, flag):
        """
        该函数按照自己被调用的情况，进而调整窗体，以及调用不同的信息显示函数\n
        :param e: 事件情况传递
        :param flag: 判断调用模式
        :return:None
        """

        self.btn_exit.SetPosition((30, 360))
        self.btn_yest.SetPosition((30, 30))
        self.btn_fore.SetPosition((30, 60))
        self.btn_refresh.SetPosition((30, 90))
        # 按钮位置调整

        if flag == 1:
            # 1则代表today
            self.window.SetSize(500, 420)
            self.window.Centre()
            # 重置尺寸

            self.today()
            # 显示今天的信息
        if flag == 2:
            # 2则代表昨天
            self.window.SetSize(500, 420)
            self.window.Centre()
            # 重置尺寸

            self.yesterday()
            # 显示今天的信息
        if flag == 3:
            # 3则代表未来天气
            self.window.SetSize(1000, 450)
            self.window.Centre()
            # 重置尺寸

            self.forecast()
            # 显示未来天气
        e.Skip()

    def exit_app(self, e):
        """
        退出该程序的函数\n
        :param e: wxPy的事件情况变量\n
        :return: Abort\n
        """
        msg = wx.MessageDialog(None, '是否确认退出？', 'Confirm', wx.YES_NO | wx.ICON_WARNING)
        get_msg = msg.ShowModal()
        # 消息盒子，避免误点击，提供反悔机会

        if get_msg == wx.ID_YES:
            self.window.Show(False)
            self.app.ExitMainLoop()
        else:
            e.Skip()
            pass

    def today(self):
        """
        该函数将在窗体上显示今天的天气状况\n
        :return:None
        """
        # 如果是1，则显示今日天气
        # 关闭查询自己的按钮
        self.basic_data1.Clear()
        self.basic_data1.Show(True)
        # 基本信息框开启

        self.basic_data1.AppendText('{}天气: '.format(self.info.city_name) + '\n')
        self.basic_data1.AppendText(self.info.today[0] + ': ')
        self.basic_data1.AppendText(self.info.today[1] + '\n')
        self.basic_data1.AppendText('风向： ' + self.info.today[5] + '\n')
        self.basic_data1.AppendText('风力： ' + self.info.today[9] + '\n')
        self.basic_data1.AppendText(self.info.today[2] + ': ')
        self.basic_data1.AppendText(self.info.today[3].replace('高温 ', '') + '\n')
        self.basic_data1.AppendText(self.info.today[6] + ': ')
        self.basic_data1.AppendText(self.info.today[7].replace('低温 ', '') + '\n')
        # 添加相关信息

        self.reminder_data.Clear()
        self.reminder_data.Show(True)
        # 提醒信息框开启
        self.reminder_data.AppendText('体感温度:  ')
        self.reminder_data.AppendText(self.info.somatosensory_temperature + '℃\n')
        self.reminder_data.AppendText('感冒提醒: \n')
        self.reminder_data.AppendText(self.info.cold_reminder)
        # 添加相关信息

        weather_type = self.info.today[11]
        self.weather_type_text.Clear()
        self.weather_type_text.Show(True)
        self.weather_type_text.AppendText('天气状况: {}'.format(weather_type))
        # 获取天气类型，并显示在主页面上
        self.show.Show(True)

        self.show.SetBitmap(self.return_weather_img(weather_type))
        # 将获取到的天气类型图片显示出来

        # 天气类型，供图形检索显示
        # wind_force = self.info.today[9]
        # 风力等级
        # wind_direction = self.info.today[5]
        # 风向
        # wx.StaticBitmap(self.panel, -1, bitmap=self.img, pos=(360, 30))

    def yesterday(self):
        """
        对昨天的天气显示进行格式化处理\n
        :return:None
        """

        self.basic_data1.Clear()
        self.basic_data1.Show(True)
        # 基本信息框开启

        self.basic_data1.AppendText('{}天气: '.format(self.info.city_name) + '\n')
        self.basic_data1.AppendText(self.info.yesterday[0] + ': ')
        self.basic_data1.AppendText(self.info.yesterday[1] + '\n')
        self.basic_data1.AppendText('风向： ' + self.info.yesterday[5] + '\n')
        self.basic_data1.AppendText('风力： ' + self.info.yesterday[9] + '\n')
        self.basic_data1.AppendText(self.info.yesterday[2] + ': ')
        self.basic_data1.AppendText(self.info.yesterday[3].replace('高温 ', '') + '\n')
        self.basic_data1.AppendText(self.info.yesterday[6] + ': ')
        self.basic_data1.AppendText(self.info.yesterday[7].replace('低温 ', '') + '\n')

        # 添加相关信息

        self.reminder_data.Clear()
        self.reminder_data.Show(False)
        # 提醒信息框关闭

        weather_type = self.info.yesterday[11]
        self.weather_type_text.Clear()
        self.weather_type_text.Show(True)
        self.weather_type_text.AppendText('天气状况: {}'.format(weather_type))
        # 获取天气类型，并显示在主页面上

        self.show.Show(True)
        self.show.SetBitmap(self.return_weather_img(weather_type))
        # 将获取到的天气类型图片显示出来

    def forecast(self):
        """
        该函数负责显示未来4天的各种信息\n
        即基本信息和天气对应的图片\n
        以及风力风向等\n
        :return: None
        """

        self.basic_data1.Clear()
        self.basic_data1.Show(False)
        self.reminder_data.Clear()
        self.reminder_data.Show(False)
        # 关闭各种显示

        self.basic_data_f1.Show(True)
        self.basic_data_f2.Show(True)
        self.basic_data_f3.Show(True)
        self.basic_data_f4.Show(True)
        # 打开未来天气的各个信息框

        self.basic_data_f1.AppendText('{} {}的天气： '.format(self.info.city_name, self.info.forecast[1]) + '\n')
        self.basic_data_f1.AppendText('风向： ' + self.info.forecast[5] + '\n')
        self.basic_data_f1.AppendText('风力： ' + self.info.forecast[9] + '\n')
        self.basic_data_f1.AppendText('最高温度： ' + self.info.forecast[3].replace('高温 ', '') + '\n')
        self.basic_data_f1.AppendText('最低温度： ' + self.info.forecast[7].replace('低温 ', '') + '\n')
        self.basic_data_f1.AppendText('天气类型： ' + self.info.forecast[11] + '\n')
        # 显示未来第一天的基本信息

        self.basic_data_f2.AppendText('{} {}的天气： '.format(self.info.city_name, self.info.forecast[13]) + '\n')
        self.basic_data_f2.AppendText('风向： ' + self.info.forecast[17] + '\n')
        self.basic_data_f2.AppendText('风力： ' + self.info.forecast[21] + '\n')
        self.basic_data_f2.AppendText('最高温度： ' + self.info.forecast[15].replace('高温 ', '') + '\n')
        self.basic_data_f2.AppendText('最低温度： ' + self.info.forecast[19].replace('低温 ', '') + '\n')
        self.basic_data_f2.AppendText('天气类型： ' + self.info.forecast[23] + '\n')
        # 显示未来第二天的基本信息

        self.basic_data_f3.AppendText('{} {}的天气： '.format(self.info.city_name, self.info.forecast[25]) + '\n')
        self.basic_data_f3.AppendText('风向： ' + self.info.forecast[29] + '\n')
        self.basic_data_f3.AppendText('风力： ' + self.info.forecast[33] + '\n')
        self.basic_data_f3.AppendText('最高温度： ' + self.info.forecast[27].replace('高温 ', '') + '\n')
        self.basic_data_f3.AppendText('最低温度： ' + self.info.forecast[31].replace('低温 ', '') + '\n')
        self.basic_data_f3.AppendText('天气类型： ' + self.info.forecast[35] + '\n')
        # 显示未来第三天的基本信息

        self.basic_data_f4.AppendText('{} {}的天气： '.format(self.info.city_name, self.info.forecast[37]) + '\n')
        self.basic_data_f4.AppendText('风向： ' + self.info.forecast[41] + '\n')
        self.basic_data_f4.AppendText('风力： ' + self.info.forecast[45] + '\n')
        self.basic_data_f4.AppendText('最高温度： ' + self.info.forecast[39].replace('高温 ', '') + '\n')
        self.basic_data_f4.AppendText('最低温度： ' + self.info.forecast[43].replace('低温 ', '') + '\n')
        self.basic_data_f4.AppendText('天气类型： ' + self.info.forecast[47] + '\n')
        # 显示未来第四天的基本信息

        self.show_f1.Show(True)
        self.show_f1.SetBitmap(self.return_weather_img(self.info.forecast[11]))
        self.show_f2.Show(True)
        self.show_f2.SetBitmap(self.return_weather_img(self.info.forecast[23]))
        self.show_f3.Show(True)
        self.show_f3.SetBitmap(self.return_weather_img(self.info.forecast[35]))
        self.show_f4.Show(True)
        self.show_f4.SetBitmap(self.return_weather_img(self.info.forecast[47]))
        # 将获取到的天气类型图片显示出来

    def return_weather_img(self, weather_type):
        """
        该函数对天气类型进行判断，并返回相应的天气图片\n
        :param weather_type:天气类型字符串\n
        :return:天气类型图片\n
        """
        types = [self.sunny, self.cloudy, self.flurry, self.gloomy,
                 self.hailstone, self.heavy_snow, self.light_snow,
                 self.mist, self.moderate_rain, self.moderate_snow,
                 self.rainstorm, self.shower, self.sleety, self.spate,
                 self.thunder_shower, self.thunderstorm]
        if weather_type.find('晴') >= 0:
            return types[0]
        elif weather_type.find('多云') >= 0:
            return types[1]
        elif weather_type.find('小雨') >= 0:
            return types[2]
        elif weather_type.find('阴') >= 0:
            return types[3]
        elif weather_type.find('冰雹') >= 0:
            return types[4]
        elif weather_type.find('大雪') >= 0:
            return types[5]
        elif weather_type.find('小雪') >= 0:
            return types[6]
        elif weather_type.find('雾') or weather_type.find('霾') >= 0:
            return types[7]
        elif weather_type.find('中雨') >= 0:
            return types[8]
        elif weather_type.find('中雪') >= 0:
            return types[9]
        elif weather_type.find('暴雨') >= 0:
            return types[10]
        elif weather_type.find('阵雨') >= 0:
            return types[11]
        elif weather_type.find('雨夹雪') >= 0:
            return types[12]
        elif weather_type.find('大雨') >= 0:
            return types[13]
        elif weather_type.find('雷阵雨') >= 0:
            return types[14]
        elif weather_type.find('暴雪') >= 0:
            return types[15]
        else:
            return self.no_img

    def clear(self):
        """
        该函数负责将各种信息清除，便于点击其他非刷新按钮时不会有冗余信息\n
        但是由于设计该函数时，很多函数已经嵌入了，因此该函数基本上就是负责清除未来天气的一个调用\n
        :return:None
        """
        self.basic_data_f1.Clear()
        self.basic_data_f2.Clear()
        self.basic_data_f3.Clear()
        self.basic_data_f4.Clear()
        # 清除未来天气的信息框

        self.show_f1.Show(False)
        self.show_f2.Show(False)
        self.show_f3.Show(False)
        self.show_f4.Show(False)
        # 未来天气的图形关闭


if __name__ == '__main__':
    w = MainWindow()
