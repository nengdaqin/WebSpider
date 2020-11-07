import requests
import os
import time
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}


# 1.发送请求
url = "http://www.xbiquge.la/15/15003/6795760.html"
res = requests.get(url, headers=headers)
res.encoding = "utf-8"
html = res.text
# print(html)


# 2.获取响应内容
title = re.findall(' <a href="/">(.*?)</a> &gt; <a href="/fenlei/7_1.html">.*?</a> &gt; <a href=".*?</a>', html)
print(title)


# 3.解析内容




# 4.保存数据