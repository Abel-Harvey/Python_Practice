import jieba
import wordcloud
import re


class CutWords:
    def __init__(self, path, num):
        self.file_path = path
        # 待分析的文件路径
        self.words_list = []
        # 切分后的词语列表
        self.items = []
        # 切分后的词语--词+次数
        self.show_word_num = num
        # 需要显示的词语数量
        self.img_path = 'test.png'
        # 最后的图片

    def get_word(self):
        """
        该函数旨在将文本文件进行词汇划分\n
        :return:None
        """
        file = open(self.file_path, 'r', encoding='utf-8').read()
        # 打开路径的文件
        file_fixed = re.sub(r'[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\。\@\#\\\&\*\%]',
                            '', file)
        file_fixed = re.sub(r'[视频生产中心|必填项|设置默认码率|视频集|视频页面|文章|文件路径|视频来源|可为空|关键字]',
                            '', file_fixed)
        file_fixed = re.sub(r'[播放器类型|表示普通播放器|播放按钮是否在播放器左下角|表示是|表示播放按钮在播放器中间|是否显示全屏按钮|默认|表示显示]',
                            '', file_fixed)
        file_fixed = re.sub(r'[登录|模式|窗口]',
                            '', file_fixed)
        wd = jieba.lcut(file_fixed)
        # 切分单词
        count = dict()
        # 记录单词出现的次数

        for w in wd:
            if len(w) == 1:
                continue
            else:
                count[w] = count.get(w, 0) + 1
        self.items = list(count.items())
        # 将词汇字典转换为list
        self.items.sort(key=lambda x: x[1], reverse=True)
        # 按次数排序

        for i in range(self.show_word_num):
            wrd, cnt = self.items[i]
            self.words_list.append(wrd)
        # 按照所希望显示的词汇个数，将其存储在self.words_list中

    def convert_to_img(self):
        """
        将词汇转换为图形
        :return:None
        """
        cut_text = ' '.join(self.words_list)
        cloud = wordcloud.WordCloud(width=1000, height=800,
                                    font_path="/System/Library/fonts/PingFang.ttc",
                                    background_color='white')
        img = cloud.generate(cut_text)
        img.to_file('test.png')


if __name__ == '__main__':
    png = CutWords('test.txt', 25)
    png.get_word()
    png.convert_to_img()

