# coding=utf-8
"""
@Time    : 2020/11/10 12:21
@Author  : nengdaqin
@File    : skins_save.py
"""
import requests
import jsonpath
import time
import os

headers = {"User_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"}
url = "https://pvp.qq.com/web201605/js/herolist.json"

hero_json = requests.get(url, headers=headers).json()
hero_name = jsonpath.jsonpath(hero_json, "$..cname")
hero_number = jsonpath.jsonpath(hero_json, "$..ename")


# 图片url-- 106：表示英雄编号，bigskin：表示高清大图，7：表示图片序号
# picture_url = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/106/106-bigskin-7.jpg"

# 遍历英雄的编号
num = 0  # 文件夹
for i in hero_number:
    # 创建文件夹
    os.mkdir("D:/qnd/Pictures/王者荣耀/" + hero_name[num])
    # 进入创建好的文件夹
    os.chdir("D:/qnd/Pictures/王者荣耀/" + hero_name[num])
    num += 1
    for j in range(10):  # 遍历输出图片的序号
        # 拼接url
        img_url = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" + str(i) + "/" + str(
            i) + "-bigskin-" + str(j) + ".jpg"

        img = requests.get(img_url, headers=headers)  # 使用拼接的url发送请求
        if img.status_code == 200:  # 如果请求的url返回状态码为200，则继续下一步操
            time.sleep(2)
            with open(str(j) + ".jpg", "wb") as f:
                f.write(img.content)

