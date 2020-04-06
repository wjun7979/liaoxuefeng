# -*- conding: utf-8 -*-
# 访问https://www.python.org/events/python-events/，用浏览器查看源码并复制，
# 然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

from urllib import request
from html.parser import HTMLParser
import re


class MyHTMLParser(HTMLParser):
    '''HTML解析器的类'''

    def __init__(self):
        super().__init__()
        self.__parsedata = None  # 设置一个空的标志位
        self.info = []  # 最终输出的信息

    def handle_starttag(self, tag, attrs):
        '''这个方法在标签开始的时候被调用，tag是小写的标记名，attrs是一个(name,value)形式的列表'''
        if tag == 'h3' and ('class', 'event-title') in attrs:
            self.__parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
        if tag == 'time':
            self.__parsedata = 'time'
        if tag == 'span' and ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
        if tag == 'span' and ('class', 'event-location') in attrs:
            self.__parsedata = 'location'

    def handle_data(self, data):
        '''这个方法用来处理任意数据'''
        if self.__parsedata == 'name':
            self.info.append('会议名称: %s' % data)
        if self.__parsedata == 'time':
            self.info.append('会议时间: %s' % data)
        if self.__parsedata == 'year':
            # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
            if re.match(r'^\d{4}$', data.strip()):
                self.info.append('会议年份: %s' % data)
        if self.__parsedata == 'location':
            self.info.append('会议地点: %s\n' % data)

    def handle_endtag(self, data):
        '''此方法用来处理元素的结束标记'''
        self.__parsedata = None  # 在HTML 标签结束时，把标志位清空


def get_html(url):
    '''访问指定的url并返回HTML源代码'''
    with request.urlopen(url, timeout=10) as f:
        return f.read().decode('utf-8')


url = 'https://www.python.org/events/python-events/'
html = get_html(url)
parser = MyHTMLParser()  # 实例化HTML解析器类
parser.feed(html)  # 解析HTML源码
for s in parser.info:  # 输出解析后的内容
    print(s)
