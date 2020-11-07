# coding=utf-8
"""
@Time    : 2020/10/26 19:59
@Author  : nengdaqin
@File    : top250.py
"""
import re
import os
import time
import csv
import requests
from lxml import etree


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",

    "Cookie": 'bid=v_gyYgETdBM; douban-fav-remind=1; ll="108306"; __yadk_uid=MVXl9igO0pmOAeZQi1JlwXRJQfNxDXcg; '
              '_vwo_uuid_v2=D6CB99A5F2F1A5F41A6D3FA69826A5148|9f09d038d709014def87947733ea20b7; '
              '__utmz=223695111.1603713298.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; __utmc=30149280; '
              '__utmc=223695111; __utmz=30149280.1603768772.11.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; '
              '__gads=ID=ad949aa1d5262dba-226aa0b466c4004a:T=1603777909:RT=1603777909:S'
              '=ALNI_MZJXJltcQtFIatyIRNG_FIGlOuIJA; '
              '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1603782122%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl'
              '%3D3G5JnKf8WTAiMFI6XhC7pyhfZ64pkaXFb0zkIKLr3i46-NRBIouKkHA5HPdPM1TL%26wd%3D%26eqid'
              '%3Dab2e9c5f00068340000000065f96b908%22%5D; _pk_ses.100001.4cf6=*; '
              '__utma=30149280.298890239.1592358726.1603776664.1603782122.13; __utmb=223695111.0.10.1603782122; '
              '__utma=223695111.366213804.1601179165.1603776664.1603782122.9; dbcl2="205598878:Yy1ZyeRv4RI"; ck=UAdf; '
              '__utmt_douban=1; __utmb=30149280.10.10.1603782122; '
              '_pk_id.100001.4cf6=114024a2359c92d6.1601179165.9.1603784315.1603777912.; push_noty_num=0; '
              'push_doumail_num=0 '



}


# 第1步：https://movie.douban.com/top250?start=0&filter=
# 第2步：https://movie.douban.com/subject/1292052/

# 1.获取详情页面的url
def get_detail_url(url):
    resp = requests.get(url, headers=headers).content.decode("utf-8")
    html_text = etree.HTML(resp)
    lis = html_text.xpath('//ol[@class="grid_view"]/li/div/div[@class="pic"]/a/@href')
    return lis


# 2.解析详情页面并获取数据
def parse_detail_url(url):
    res = requests.get(url, headers=headers).content.decode("utf-8")
    html_text = etree.HTML(res)
    # 电影名
    title = html_text.xpath("//h1/span/text()")[0]
    # 评分
    score = re.findall('<strong class="ll rating_num" property="v:average">(.+?)</strong>', res)
    # 年代
    years = "".join(html_text.xpath("//h1/span/text()")[1]).strip("()")
    # 导演
    director = html_text.xpath('//div[@class="subject clearfix"]//span/a/text()')[0]
    # 编剧
    screenwriter = html_text.xpath('//div[@class="subject clearfix"]//span/a/text()')[1:3]
    # 主演
    actor = html_text.xpath('//div[@class="subject clearfix"]//span/a/text()')[3:]
    # 类型
    types = html_text.xpath('//*[@id="info"]/span/text()')[4:6]
    # 制片地区
    region = re.findall(' <span class="pl">制片国家/地区:</span>(.+?)<br/>', res)
    # 语言
    language = re.findall('<span class="pl">语言:</span>(.+?)<br/>', res)
    # 上映时间
    releaseTime = html_text.xpath('//*[@id="info"]/span/text()')[10]
    # 片长
    filmLength = re.findall('<span class="pl">片长:</span> <span property="v:runtime".*?>(.+?)</span>', res)

    # 将上述结果存储到字典中
    dict_data = {
        "title": title, "score": score, "years": years, "director": director, "screenwriter": screenwriter,
        "actor": actor, "types": types, "region": region, "language": language, "releaseTime": releaseTime,
        "filmLength": filmLength
    }

    return dict_data


# 3.保存数据 -- 以csv文件格式进行保存
def save_data(data):
    # 保存的路径
    download_path = r"E:\project\web_spider\douban\data"
    # 如果目录文件不存在就创建
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    # 保存的文件名
    file_name = download_path + "/" + "top250.csv"
    # 表头
    header = ["title", "score", "years", "filmLength", "region", "types", "language", "director", "screenwriter",
          "releaseTime", "actor"]

    with open(file_name, "a", encoding="utf-8")as fp:
        write = csv.DictWriter(fp, header)

        # 以读的方式打开文件，reader判断一下表头是否存在
        with open("./data/top250.csv", "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            # 如果表头为空则写入，不为空就直接写入内容
            if not [row for row in reader]:
                write.writeheader()
            else:
                write.writerow(data)

    print("抓取完成！！")

def main():
    # 初始的url
    base_url = "https://movie.douban.com/top250?start=0&filter="
    lis_url = get_detail_url(base_url)
    print(lis_url)
    # for li_url in lis_url:
    #     data = parse_detail_url(li_url)
    #
    #     # 每次请求等待1s
    #     time.sleep(3)
    #     # 保存数据
    #     save_data(data)


    # for i in range(0, 251, 25):
    #     url = base_url.format(i)
    #     # 获取详情页面url
    #     lis_url = get_detail_url(url)
    #     # 请求详情页面并提取数据
    #     for li_url in lis_url:
    #         data = parse_detail_url(li_url)
    #         # print(data)
    #         # 每次请求等待1s
    #         time.sleep(1)
    #         # 保存数据
    #         save_data(data)

if __name__ == '__main__':
    main()
