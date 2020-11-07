import re
import requests
import time
# import os
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"

}


# 请求网页
# url = 'https://tuchong.com/17687886/72295189/' # 1
# url = 'https://zhaojie.tuchong.com/71137025/'  # 2
# url = "https://zhaojie.tuchong.com/68624068/"  # 3
# url = "https://tuchong.com/282981/72379241/"  # 4
# url = "https://tuchong.com/1317488/70540893/"  # 5
# url = "https://tuchong.com/1317488/71322713/"  # 6
# url = "https://tuchong.com/445323/69687747/"  # 7
# url = "https://tuchong.com/16430236/70204465/"  # 8
# url = "https://tuchong.com/16958101/73429515/"  # 9
# url = "https://tuchong.com/438502/13619306/"  # 10
# url = "https://tuchong.com/18111840/72686026/"  # 11
url = "https://wgvutj1.tuchong.com/73558844/"  # 12

res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
html = res.text
# print(html)


# 解析网页
# urls = re.findall('<img id=".+?" class=".+?" src="(.+?)" alt="">', html)
urls = re.findall('<img id=".*?" class=".*?".*?src="(.*?)" alt="">', html)
# print(urls)

# # 保存图片
for url in urls:
    # 图片名字
    time.sleep(1)
    file_name = url.split('/')[-1]
    res = requests.get(url, headers=headers)
    with open(r"E:\project\web_spider\girl\imgs\meinv" + file_name, "wb")as f:
        f.write(res.content)