# coding=utf-8
"""
@Time    : 2020/11/10 15:56
@Author  : nengdaqin
@File    : picture.py
"""
import os

import requests
import re
import time
import jsonpath
import socket
socket.setdefaulttimeout(20)

headers = {
    "User_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 "
                  "Safari/537.36"}
def get_json_data(json_url):

    hero_json = requests.get(json_url, headers=headers).json()
    return hero_json




def download(hero_json):
    # 使用jsonpath语法匹配英雄的名称和ID
    hero_name = jsonpath.jsonpath(hero_json, "$..name")
    heroId = jsonpath.jsonpath(hero_json, "$..heroId")
    # 遍历英雄的编号
    num = 0  # 文件夹
    for i in heroId:
        # 创建文件夹
        download_path = "D:/qnd/Pictures/lol_pic/" + hero_name[num]
        if not os.path.exists(download_path):
            # 创建文件夹
            os.mkdir(download_path)
            # 进入创建好的文件夹
        os.chdir(download_path)

        num += 1
        # 拼接url
        for j in range(4):
            for k in range(10):
                img_url = "https://game.gtimg.cn/images/lol/act/img/skin/" + 'big' + str(i) + str(0) + str(j) + str(
                    k) + ".jpg"

                img = requests.get(img_url, headers=headers)  # 使用拼接的url发送请求
                if img.status_code == 200:  # 如果请求的url返回状态码为200，则继续下一步操

                    # for name in hero_name:
                    #     time.sleep(2)
                    #     print("正在下载:", name)

                    file_name = str(k) + ".jpg"  # 文件名
                    if not os.path.exists(file_name):  # 如果文件不存在就下载
                        with open(file_name, "wb") as f:
                            f.write(img.content)




def main():
    base_url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
    jsonData = get_json_data(base_url)
    download(jsonData)

if __name__ == '__main__':
    main()