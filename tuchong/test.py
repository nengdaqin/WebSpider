# coding=utf-8
"""
@Time    : 2020/11/5 12:56
@Author  : nengdaqin
@File    : test.py
"""
import urllib.parse
from urllib import parse
city = "城市"
a = urllib.parse.quote(city)
print(a)  # %E5%9F%8E%E5%B8%82
#
scenery = "风光"
a1 = parse.quote(scenery)
print(a1)  # %E9%A3%8E%E5%85%89

url = 'http://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E6%A2%A6'
print(parse.unquote(url))  # http://www.baidu.com/s?wd=中国梦