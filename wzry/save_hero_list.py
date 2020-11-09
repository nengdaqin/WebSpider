# coding=utf-8
"""
@Time    : 2020/11/6 20:27
@Author  : nengdaqin
@File    : save_hero_list.py
"""
import requests
import json
url = "https://pvp.qq.com/web201605/js/herolist.json"

headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 "
                         "Safari/537.36"}

hero_list = requests.get(url, headers=headers).json()
print(hero_list)
with open("../json_file/wzry.json", "w", encoding="utf-8") as f:
    json.dump(hero_list, f, ensure_ascii=False)