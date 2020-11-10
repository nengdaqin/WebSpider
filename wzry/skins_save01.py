# coding=utf-8
"""
@Time    : 2020/11/10 14:12
@Author  : nengdaqin
@File    : skins_save.py
"""
import requests
import jsonpath
import time
import os

headers = {
    "User_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 "
                  "Safari/537.36"}
# 获取英雄的json数据
def get_json_data(json_url):
    hero_json = requests.get(json_url, headers=headers).json()
    return hero_json


def download(heroData):
    # 通过jsonpath语法找到json数据中英雄的的名称和编号
    hero_name = jsonpath.jsonpath(heroData, "$..cname")
    hero_number = jsonpath.jsonpath(heroData, "$..ename")

    num = 0  # 英雄名称的索引
    for i in hero_number:  # 遍历英雄的编号

        # 以英雄的名称创建文件夹
        download_path = "D:/qnd/Pictures/王者荣耀/" + hero_name[num]
        if not os.path.exists(download_path):
            os.mkdir(download_path)
        # 进入创建好的文件夹
        os.chdir(download_path)
        num += 1

        for j in range(10):  # 遍历输出图片的序号
            # 拼接url
            img_url = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" + str(i) + "/" + str(
                i) + "-bigskin-" + str(j) + ".jpg"

            # 使用拼接好的url发送请求
            img = requests.get(img_url, headers=headers)  # 使用拼接的url发送请求

            if img.status_code == 200:  # 如果请求的url返回状态码为200，则继续下一步操
                time.sleep(2)
                print(img.url)
                file_name = str(j) + ".jpg"  # 文件名
                if not os.path.exists(file_name):  # 如果文件不存在就下载
                    with open(file_name, "wb") as f:
                        f.write(img.content)


def main():
    base_url = "https://pvp.qq.com/web201605/js/herolist.json"
    json_data = get_json_data(base_url)
    download(json_data)


if __name__ == '__main__':
    main()