import re
import requests
import time
import os
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"

}

# 获取详情页面的url
def get_detail_urls(url):
    res = requests.get(url, headers=headers)
    res.encoding = 'gb2312'
    html = res.text
    urls_list = re.findall('<a href="(.+?)" target=".+?src=".+?" alt=".+?".+?</a>', html)
    data_urls = []
    for website in urls_list:
        data_url = "https://www.tupianzj.com/" + website

        data_urls.append(data_url)
    return data_urls
    # print(data_urls)

url = 'https://www.tupianzj.com/meinv/mm/xqxmn/'


detail_urls = get_detail_urls(url)

# 解析详情页内容
# def parse_detail_page(url):
#     response = requests.get(detail_url, headers=headers)
#     response.encoding = 'gb2312'
#     html_text = response.text
#     pictures_url = re.findall("<a href='.+?'><a href='.+?'>.+?src=(.+?) id=.+? alt=.+?</a>", html_text)
#     # print(pictures_url)
#     return pictures_url

# 解析详情页内容
for detail_url in detail_urls:
    response = requests.get(detail_url, headers=headers)
    response.encoding = 'gb2312'
    html_text = response.text
    pictures_url = re.findall("<a href='.+?'><a href='.+?'>.+?src=(.+?) id=.+? alt=.+?</a>", html_text)
    # print(pictures_url)
    # picture_name = re.findall('<li>.+?title="(.+?)".+?src=".+?".+?</i>', html_text)
    # print(picture_name)
    # print(type(pictures_url))

# 保存图片
# for picture_url in pictures_url:
#     file_name = picture_url.split("/")[-1]
#     responses = requests.get(picture_url, headers=headers)
#     with open("file_name", "wb")as f:
#         f.write(responses.content)