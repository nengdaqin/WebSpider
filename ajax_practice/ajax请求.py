# coding=utf-8
"""
@Time    : 2020/11/1 10:23
@Author  : nengdaqin
@File    : ajax请求.py
"""
import requests
import json

"豆瓣电影--https://movie.douban.com/(切换电影页码时，使用ajax异步请求)"
url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20" \
      "&page_start=0 "

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) "
                  "Version/5.1 Safari/534.50 "
}

json_data = requests.get(url, headers=headers)
data = json_data.text
# 将字符串的内容反序列化成Python对象
json_data = json.loads(data)
# print(json_data)
subjects = json_data['subjects']
# print(subjects)
result = []
for movie in subjects:
    row = {
        'movie_rate': movie['rate'],
        'movie_name': movie['title'],
        'movie_url': movie['url']
    }
    result.append(row)
print(result)