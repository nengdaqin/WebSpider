# -*- coding:utf-8 -*-
"""
微信公众号：学编程的金融客
作者：小笨聪
"""
import time

import requests
import re
import urllib.parse  # quote()可以将中文转换为URL编码格式
import json
import traceback
import os


# 下载网页
def Download(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/69.0.3497.100 Safari/537.36",
    }
    try:
        return requests.get(url, headers=head, timeout=60)

    except (Exception, AttributeError) as a:
        print(a)


# 获取开始的标签链接
def Thelabel():
    url = "https://tuchong.com/explore/"
    html = Download(url).text
    return re.findall('<span class="tag-title">([\u4e00-\u9fa5]+)</span>', html)


# 获取第X页的列表
def Picturegroup(name, num):
    url = "https://tuchong.com/rest/tags/%(name)s/posts?page=%(num)s&count=20&order=weekly" % {'name': name,
                                                                                               "num": str(num)}
    print(url)
    html = Download(url)
    if html:
        return json.loads(html.text)  # 用json模块解析并且返回一个解析好的json模块


# 下载保存
def Save(url_list, title, page):
    title_naem = os.path.join("picture", title)  # 要将图片保存到那个文件夹
    if not os.path.exists(title_naem):
        try:
            os.makedirs(title_naem)
            num = 0
            countfile = 0
            countdir = 0
            for url in url_list:
                num += 1
                path_name_split = url.split("/")
                suffix = ".%s" % path_name_split[-1].split(".")[-1]
                path_name = os.path.join("picture", os.path.join(title, "%s(%d)%s" % (title, num, suffix)))
                # print(path_name)
                # path_name = os.path.join("图虫网爬虫",path_name)
                if not os.path.exists(path_name.encode()):
                    response = Download(url)
                    if requests:
                        if not os.path.exists(path_name):
                            with open(path_name, "wb") as f:
                                f.write(response.content)
                                f.close()
                                countfile += 1
                                print("正在下载：%s 标题：%s   共%d张/现%d张" % (page, title, num, len(url_list)),
                                  "当前进度文件夹进度{0:.2f}%".format(countfile * 100 / len(url_list)))
            print("%s下载完毕！" % title)
        except:  # 输出错误的类型
            print(traceback.print_exc())


# 用正则匹配图片链接
def Picturenoe(title, url, page, type):
    """
    title: 后续获取到的图片集的名称，用做创建文件夹的名字
    url:   传入图片集的地址
    page:  直观输出的现在正在爬取第几页
    type:  判断我们究竟该用那种方式进行匹配
    """
    if type == 1:
        html = Download(url).text
        path = list(
            set(re.findall(r'<img id="image\d+" class="multi-photo-image" src="([a-zA-z]+://[^\s]*)" alt="">', html)))
    elif type == 2:
        html = Download(url).text
        path = list(set(re.findall(r'<img src="([a-zA-z]+://[^\s]*)" alt="\d+.[a-z]+" />', html)))
    Save(path, title, page)
    # print("开始下载：%s共：%d个" % (title, len(path)))


def DownloadIf(url, title, page):
    if url.find("/t/") != -1:
        Picturenoe(title, url, page, 2)
    else:
        Picturenoe(title, url, page, 1)


# 删除Windows文件创建时不允许出现的字符
def strip(path):
    return re.sub(r'[? .\\*|"<>，:/]', "", str(path))


# 总程序
def initial(name, num):
    for i in range(1, num + 1):
        print(i)
        img_info = Picturegroup(name, i)
        number = 0
        print("开始下载第%d页共：%d套" % (i, len(img_info['postList'])))
        for img_info_temp in img_info['postList']:
            img_info_url = img_info_temp['url']
            img_info_post_id = img_info_temp['post_id']
            img_info_title = strip(img_info_temp['title']).strip()
            if img_info_title == "":
                img_info_title = img_info_post_id
            number += 1
            DownloadIf(img_info_url, img_info_title, "下载第%d页共：共%d套/现%d套" % (i, len(img_info['postList']), number))
    print("全部下载完毕共：%d页,%d套！" % (number, len(img_info['postList'])))


if __name__ == '__main__':
    if not os.path.exists("picture"):
        os.makedirs("picture")
        print("偷偷创建了：picture 文件夹")
    label = Thelabel()  # 获取动态标签
    print("标签：", label, "更多标签请前往https://tuchong.com/explore/查询")
    name = urllib.parse.quote(input("请输入标签名字："))
    number = int(input("请输入要爬取的页数："))
    time.sleep(3)
    initial(name, number)
