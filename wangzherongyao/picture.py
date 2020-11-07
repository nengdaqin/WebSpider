# coding=utf-8
"""
@Time    : 2020/11/6 20:27
@Author  : nengdaqin
@File    : picture.py
"""
import requests
url = "https://pvp.qq.com/web201605/js/herolist.json"

headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 "
                         "Safari/537.36"}

jsonData = requests.get(url, headers=headers).json()
print(jsonData)