# coding=utf-8
"""
@Time    : 2020/11/1 12:38
@Author  : nengdaqin
@File    : headers.py
"""
from lxml import etree

import requests
import random

header_list = [
    # Chrome
    {"User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, "
                   "like Gecko) Version/5.1 Safari/534.50"},
#     {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 "
#                    "Safari/535.1"},
#     {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                    "Chrome/86.0.4240.111 Safari/537.36 "},
#
#     {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                    "Chrome/73.0.3683.103 Safari/537.36"},
#     # MAC
#     {"User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, "
#                    "like Gecko) Version/5.1 Safari/534.50"},
#
#     # Firefox
#     {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0Firefox 4.0.1 – MAC"},
#     {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
#
]
#
headers = [header for header in header_list]
header = random.choice(headers)
print(header)
url = "https://www.guazi.com/sz/"
# 1.发起请求
resp = requests.get(url, header).content.decode("utf-8")
html = etree.HTML(resp)
print(resp)


# def random_header():
#     headers = [header for header in header_list]
#     header = random.choice(headers)
#     # print(header)
#     return header


# def main():
#     base_url = "https://movie.douban.com"
#     header = random_header()
#     resp = requests.get(base_url, header)
#     resp.encoding = "utf-8"
#     print(resp.content)
#
# if __name__ == '__main__':
#     main()
# url = "https://www.guazi.com/sz/"
# # 1.发起请求
# resp = requests.get(url, headers=headers).content.decode("utf-8")
# html = etree.HTML(resp)