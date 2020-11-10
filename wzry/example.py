# coding=utf-8
"""
@Time    : 2020/11/10 11:02
@Author  : nengdaqin
@File    : example.py
"""
import os
import time

import jsonpath
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
hero_list = requests.get(url)  # 获取英雄列表json文件

hero_list_json = hero_list.json()  # 转化为json格式
hero_name = list(map(lambda x: x['cname'], hero_list.json()))  # 提取英雄的名字
hero_number = list(map(lambda x: x['ename'], hero_list.json()))  # 提取英雄的编号

# hero_name = jsonpath.jsonpath(hero_list_json, "$..cname")
# hero_number = jsonpath.jsonpath(hero_list_json, "$..ename")
print(hero_name)
print(hero_number)


# # 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        # 创建文件夹
        os.mkdir("D:/qnd/Pictures/王者荣耀/" + hero_name[i])
        # 进入创建好的文件夹
        os.chdir("D:/qnd/Pictures/王者荣耀/" + hero_name[i])
        i += 1
        for k in range(10):
            # 拼接url
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            if im.status_code == 200:
                time.sleep(2)
                open(str(k) + '.jpg', 'wb').write(im.content)  # 写入文件


# downloadPic()