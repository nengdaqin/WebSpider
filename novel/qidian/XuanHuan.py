# coding=utf-8
"""
@Time    : 2020/10/26 18:50
@Author  : nengdaqin
@File    : XuanHuan.py
"""
# 爬取起点网玄幻类小说
import time
import requests
from lxml import etree
# from headers_file import header


"""
步骤：
# 第1步：https://www.qidian.com/
# 第2步：https://www.qidian.com/xuanhuan
# 第3步：https://www.qidian.com/free/all?chanId=21
# 第4步：https://book.qidian.com/info/1024088056#Catalog
"""

# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                       "(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
#
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
#                   "application/signed-exchange;v=b3;q=0.9",
#
#         "Cookie": "csrfToken=8xS14ovSEUGka0KZk2PODGycaqGJSPb4lPpLDZ3V; newstatisticUUID=1603069046_1288729293; "
#                   "qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; "
#                   "lrbc=1023708557%7C571660236%7C0%2C1023718967%7C571767942%7C0%2C1023438690%7C565189988%7C0; "
#                   "rcr=1023708557%2C1023718967%2C1023438690%2C1021668703; topGame=1; ywguid=854022805626; "
#                   "ywkey=yw4lVVcUh48q; ywopenid=FAD63986096F5678D8FD201340AB0F9F; "
#                   "e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A08%22%2C%22l1%22%3A1%7D; "
#                   "e2=%7B%22pid%22%3A%22qd_P_xuanhuan%22%2C%22eid%22%3A%22qd_F122%22%2C%22l1%22%3A3%7D ",
#
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
#
#     }

proxies = "183.166.6.70:27943"

# 1.发送请求

def send_request(url):
    resp = requests.get(url, proxies=proxies).content.decode("utf-8")
    html = etree.HTML(resp)
    print(resp)
    # print()

urls = "https://www.qidian.com/"
send_request(urls)
# 2.获取响应内容


# 3.解析提取数据


# 4.保存数据


# def main():
#     base_url = "https://www.qidian.com/"
#     send_request(base_url)
