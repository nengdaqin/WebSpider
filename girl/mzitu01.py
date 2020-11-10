# coding=utf-8
"""
@Time    : 2020/11/9 22:36
@Author  : nengdaqin
@File    : mzitu.py
"""
import time

import requests
import re
from lxml import etree
import socket
socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒
url = "https://www.mzitu.com/"
Host_referer = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    'Referer': url}

resp = requests.get(url, headers=Host_referer).content.decode("utf-8")
html_text = etree.HTML(resp)


url_list = html_text.xpath('//div[@class="postlist"]/ul/li/a/@href')
time.sleep(2)
# print(url_list)
# print(len(url_list))
urls = [urls for urls in url_list]
print(urls)
# 解析详情页面并提取内容
# for urls in url_list:
#     time.sleep(2)
#     print(urls)

detail = requests.get(urls[0], headers=Host_referer)

de_html = etree.HTML(detail)

img = de_html.xpath('//div[@class="main-image"]//img/@src')
print(img)
#
#     with open("file_name.jpg", "wb")as f:
#         f.write(img)

