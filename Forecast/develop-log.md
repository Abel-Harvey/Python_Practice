# Forecast项目开发日志
## Author: Abel-Harvey
## Created Date: 12-01-2020

开发详情：
### version: v0.1
1. 当获取到相关结果后，如果成功，则将有*desc*反馈的是:**OK**，状态码为1000
2. 反之，则*desc*为: **invilad-citykey**,且状态码为1002
3. 定义exit退出码：3，表示遇到城市查询问题，可能以后需要将其状态返回，供GUI处理
##### 2020-12-2
- 由于查询后一个空格依旧存在，且无法进行锁定，故计划进行Show(False)
- 由于相关数据的缺失，故应当进行布局的重新调整
- 考虑减小初始的屏幕大小，当点击不同的btn，按照实际将显示数据的大小重新调整大小，当点击刷新按钮后，回到初始大小
- 按钮位置也需要调整
##### 2020-12-4
- 天气图标不对劲，对于那么多的图片，如何一次配置，简单调用呢？
- 假设使用一个列表，到时候直接进行调用？这样会造成大量的空间浪费！
- 查询昨天的天气不能对图标进行刷新，需要进行订正，可以预见的是，对于未来天气也有这个问题
##### 2020-12-5
- 设置好了未来天气的四个显示区域
##### 2020-12-6
- 今日天气虽然点击查询后就出现了，但是好歹得再给一个按钮，不然想看今天得天气怎么办?