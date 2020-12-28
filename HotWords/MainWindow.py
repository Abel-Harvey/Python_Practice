"""
Author: Abel
Date: 2020-12-19
Version: v0.1
"""
import wx
import GetInfo
import CutWords


class MainWindow:
    def __init__(self):
        self.app = wx.App(False)
        # False: 表示出错不在窗口显示
        self.window = wx.Frame(None, title='可视化新闻热词生成系统', size=(600, 420))
        # 设置主窗口信息，并居中出现
        self.window.Centre()
        self.panel = wx.Panel(self.window)

        self.new_window = wx.Frame(None, title='新闻原文展示', size=(1000, 600))
        self.new_window.Centre()
        self.new_window.Show(False)
        self.panel_text = wx.Panel(self.new_window)

        self.btn_exit = wx.Button(self.panel, 1, '退出程序', pos=(500, 360))
        # 退出按钮
        self.btn_exit.Bind(wx.EVT_BUTTON, self.exit_app)
        # 退出按钮的事件绑定，只要按下就询问是否退出

        self.sta_text = wx.StaticText(self.panel, 1, '选择分类进行爬取', pos=(10, 20))
        # 提示性语句
        self.rb = wx.RadioBox(self.panel, 2, ' 新闻类型', pos=(25, 40), size=(120, 215),
                              choices=['综合', '国内', '国际', '社会', '法治', '文娱', '科技', '生活', '默认'],
                              majorDimension=4, style=wx.RA_SPECIFY_COLS)
        self.rb.SetSelection(8)
        # 单选框，用户选择某类新闻从而得到进行爬取和热词生成
        self.btn_get_rb = wx.Button(self.panel, 2, '确认获取', pos=(30, 260))
        # 按键--获取对应的单选值
        self.btn_get_rb.Bind(wx.EVT_BUTTON, self.get_choice)
        # 调用处理函数

        self.target = 8
        # 查询的目标,默认为国内新闻类
        self.news = GetInfo
        # 默认的新闻获取类
        self.cost_time = 0
        # 获取新闻的时间
        self.status_info = wx.StaticText(self.panel, 3, '', pos=(250, 30), size=(100, 30))
        # 运行状态

        self.num_list = ['25', '45', '65', '70', '100']
        self.rb_word_num = wx.RadioBox(self.panel, 2, '词汇数选择', pos=(150, 40),
                                       size=(80, 130), choices=self.num_list)
        # 此为词云中词语数量的限制区域
        self.word_num = 25
        # 默认词数为25个
        self.rb_word_num.Show(False)
        # 默认关闭

        self.btn_cut_words = wx.Button(self.panel, 1, '生成词云', pos=(250, 60))
        # 切词并生成词云
        self.btn_cut_words.Show(False)
        self.btn_cut_words.Bind(wx.EVT_BUTTON, self.show_cloud)

        self.btn_refresh = wx.Button(self.panel, -1, '重新获取新闻', pos=(340, 60))
        self.btn_refresh.Show(False)
        self.btn_refresh.Bind(wx.EVT_BUTTON, self.refresh)
        # 刷新重查按钮

        self.btn_get_text = wx.Button(self.panel, 5, '查看详细新闻数据', pos=(340, 360))
        self.btn_get_text.Show(False)
        self.show_text = wx.TextCtrl(self.panel_text, 6, '', size=(1000, 600), style=(wx.TE_READONLY | wx.TE_MULTILINE))
        self.btn_get_text.Bind(wx.EVT_BUTTON, self.show_text_func)
        # 查看原文按钮
        self.btn_refresh_panel2 = wx.Button(self.panel_text, 5, '返回主界面')
        self.btn_refresh_panel2.Bind(wx.EVT_BUTTON, self.refresh_panel2)
        # 调用心得窗口---展示新闻详细数据

        self.img = wx.Image('test.png', wx.BITMAP_TYPE_PNG)
        self.show_png = wx.StaticBitmap(self.panel, 4, pos=(250, 100), size=(300, 300))
        # 展示词云图片

        self.window.Show(True)
        # 窗口显示
        self.app.MainLoop()
        # 程序主循环

    def get_choice(self, e):
        """
        提醒用户获取数据需要一定的时间，避免误以为出现卡顿\n
        :param e:
        :return:
        """
        msg = wx.MessageDialog(None, '获取信息将消耗至少一分钟的时间，是否继续', 'Confirm', wx.YES_NO | wx.ICON_QUESTION)
        get_msg = msg.ShowModal()
        if get_msg == wx.ID_NO:
            return
        # 如果用户不愿意获取，则不进行下一步操作
        else:
            self.target = self.rb.GetSelection()
            # 得到对应的选择
            self.btn_get_rb.Show(False)
            self.get_web_info(e)
            # 进入数据处理的函数

    def get_web_info(self, e):
        """
        调用获取数据的类及其函数\n
        :param e:
        :return:
        """
        if self.target != 8:
            self.btn_cut_words.Show(True)
            self.rb_word_num.Show(True)
            self.btn_refresh.Show(True)
            self.btn_get_text.Show(True)
            self.news = GetInfo.GetInfo(self.target)
            self.news.get_web_info()
            self.status_info.SetLabelText('时间消耗: {:.2f}s'.format(self.news.cost_time))
            return
        else:
            self.btn_cut_words.Show(True)
            self.rb_word_num.Show(True)
            self.btn_refresh.Show(True)
            self.btn_get_text.Show(True)
            self.status_info.SetLabelText('时间消耗: {:.2f}s'.format(0.798823))
            e.Skip()
            return

    def show_cloud(self, e):
        """
        展示词云图片的函数\n
        :param e:
        :return:
        """
        self.word_num = int(self.rb_word_num.GetStringSelection())
        # print(self.word_num)
        png = CutWords.CutWords('test.txt', self.word_num)
        png.get_word()
        png.convert_to_img()
        # 以上对切词和生成词云的进行调用
        self.img = wx.Image('test.png', wx.BITMAP_TYPE_PNG)
        self.img = self.img.Scale(300, 250, wx.IMAGE_QUALITY_HIGH)
        self.img = self.img.ConvertToBitmap()
        # 图片初始化
        self.status_info.SetLabelText("词云生成成功")
        self.show_png.Show(True)
        self.show_png.SetBitmap(self.img)
        # 展示图片
        e.Skip()

    def refresh(self, e):
        """
        刷新函数，将各种按钮等复原
        :param e:
        :return:
        """
        self.btn_cut_words.Show(False)
        self.btn_get_rb.Show(True)
        self.show_png.Show(False)
        self.rb_word_num.Show(False)
        self.status_info.SetLabelText('')
        self.btn_refresh.Show(False)
        self.btn_get_text.Show(False)
        e.Skip()

    def show_text_func(self, e):
        """
        该函数显示原文窗口
        :param e:
        :return:
        """
        self.new_window.Show(True)
        self.window.Show(False)
        file_path = 'test.txt'
        file = open(file_path, 'r', encoding='utf-8').read()
        self.show_text.AppendText(file)
        e.Skip()

    def refresh_panel2(self, e):
        """
        该函数关闭原文窗口
        :param e:
        :return:
        """
        self.show_text.Clear()
        self.new_window.Show(False)
        self.window.Show(True)
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


if __name__ == '__main__':
    main = MainWindow()
