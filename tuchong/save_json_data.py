# coding=utf-8
"""
@Time    : 2020/11/9 9:06
@Author  : nengdaqin
@File    : save_json_data.py
"""
import requests
import json

url = "https://tuchong.com/rest/tags/%E5%B1%B1/posts?page=1&count=20&order=weekly"
headers = {
    "User_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/41.0.2227.0 Safari/537.36"
}

resp = requests.get(url, headers=headers).json()
print(resp)

with open("mountain.json", "w", encoding="utf-8") as f:
    json.dump(resp, f, ensure_ascii=False)

