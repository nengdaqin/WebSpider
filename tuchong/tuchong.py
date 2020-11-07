# coding=utf-8
"""
@Time    : 2020/11/5 12:41
@Author  : nengdaqin
@File    : tuchong.py
"""
import re
import requests
import json
import os


def Download(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/69.0.3497.100 Safari/537.36",
    }
    try:
        return requests.get(url, headers=head, timeout=60)

    except (Exception, AttributeError) as a:
        print(a)

def Picture_group(name, num):
    url = "https://tuchong.com/rest/tags/%(name)s/posts?page=%(num)s&count=20&order=weekly" % {'name': name,
                                                                                               "num": str(num)}
    print(url)
    html = Download(url)
    if html:
        return json.loads(html.text)  # 用json模块解析并且返回一个解析好的json模块

def save_picture(data_picture):
    # 下载的路径
    download_path = r".\tuchong"
    # 如果目录文件不存在就创建
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    # 保存的文件名
    file_name = download_path
    with open(file_name, "wb")as f:
        f.write(data_picture)



def main():
    base_url = "https://tuchong.com/tags/%E5%9F%8E%E5%B8%82/"
    Download(base_url)
    a = Picture_group("%E5%9F%8E%E5%B8%82", 1)
    print(a)

if __name__ == '__main__':
    main()

