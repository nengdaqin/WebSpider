# coding=utf-8
"""
@Time    : 2020/11/1 12:36
@Author  : nengdaqin
@File    : tuchong.py
"""
import requests
import json

"图虫图片类https://tuchong.com/tags/%E5%9F%8E%E5%B8%82/采用ajax请求呈现数据"

url = "https://tuchong.com/rest/tags/%E5%9F%8E%E5%B8%82/posts?page=1&count=20&order=weekly&before_timestamp="

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) "
                  "Version/5.1 Safari/534.50 "
}
