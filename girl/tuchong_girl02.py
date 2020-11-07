# coding=utf-8
import re
import requests

# 1.发送请求
def send_request(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    return response

# 2.获取内容
def get_content(response):
    html = response.text
    return html

# 3.解析数据

def get_data(html):

    urls = re.findall("", html)
    return urls

# 4.保存数据