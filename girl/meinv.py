# coding=utf-8
"""
@Time    : 2020/11/3 22:37
@Author  : nengdaqin
@File    : meinv.py
"""
import time

import requests
# from lxml import etree
import re
# 第一步：https://www.tupianzj.com/meinv/
# 第二步：https://www.tupianzj.com/meinv/20201020/218939.html
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
           "Chrome/86.0.4240.111 Safari/537.36"}


def get_detail_url(base_url):
    resp = requests.get(base_url, headers=headers).content.decode('gb2312')

    # html_text = etree.HTML(resp)
    detail_urls = re.findall('<li><a href="(.*?)" title=".+?">', resp)
    # print(detail_urls)
    # 获取详情页面
    url_list = ["https://www.tupianzj.com" + detail_url for detail_url in detail_urls]
    # print(url_list)
    # print(len(url_list))
    return url_list

# 请求详情页面,解析提取数据
def parse_detail_url(li_url):
    res = requests.get(li_url[0], headers=headers)
    res.encoding = "gb2312"
    html = res.text
    time.sleep(1)
    # print(html)

    li = re.findall('<img src="(.*?)".*?</a>', html)
    return li

def main():
    base_url = "https://www.tupianzj.com/meinv/"
    li_url = get_detail_url(base_url)
    print(li_url)
    li = parse_detail_url(li_url)
    print(li)


if __name__ == '__main__':
    main()
