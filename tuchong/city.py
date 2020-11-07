# coding=utf-8
"""
@Time    : 2020/10/28 19:07
@Author  : nengdaqin
@File    : city.py
"""
import requests
import os
import csv
import time
from lxml import etree


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.111 Safari/537.36 "
}


# 需求：爬取图虫网的城市类
# url
# 步骤1.https://tuchong.com/explore/  # 首页
#         '//div[@class="page-content"]//ul/li/a/@href'  # 城市页url_list

# 步骤2.https://tuchong.com/tags/%E5%9F%8E%E5%B8%82/  # 城市页
#         '//ul[@class="pagelist-wrapper"]/li//div/@href'  # 详情页面url
#           '//div[@class="scene-container-next"]/div/img/@src'  详情页面图片

# 获取类的url
def get_class_url(url):
    resp = requests.get(url, headers=headers).content.decode("utf-8")
    html_text = etree.HTML(resp)
    lis = html_text.xpath('//div[@class="page-content"]//ul/li/a/@href')
    # 返回所有种类的url
    return lis


# 获取每个详情页面
def get_detail_url(lis_url):
    resp = requests.get(lis_url, headers=headers).content.decode("utf-8")
    html_text = etree.HTML(resp)
    details = html_text.xpath('//ul[@class="pagelist-wrapper"]/li//div/@href')
    return details


# 解析详情页面并获取数据
def parse_detail_url(details_url):
    resp = requests.get(details_url, headers=headers).content.decode("utf-8")
    html_text = etree.HTML(resp)
    picture = html_text.xpath('//ul[@class="pagelist-wrapper"]/li//div/@href')
    return picture


def save_picture(data_picture):
    # 下载的路径
    download_path = r"E:\project\web_spider\girl\imgs\tuchong"
    # 如果目录文件不存在就创建
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    # 保存的文件名
    file_name = download_path
    with open(file_name, "wb")as f:
        f.write(data_picture)


def main():
    base_url = 'https://tuchong.com/explore/'
    lis_url = get_class_url(base_url)
    # print(lis_url)
    li_url = [li_url for li_url in lis_url]
    time.sleep(2)
    # print(len(li_url))  # 66
    print(li_url)
    details_url = get_detail_url(li_url[0])
    print(details_url)


if __name__ == '__main__':
    main()
