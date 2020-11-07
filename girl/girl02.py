import re
import requests
import time
import os
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"

}


# 请求网页
# url = 'https://www.mmonly.cc/mmtp/xgmn/299922.html' # 1
url = 'https://www.tupianzj.com/meinv/20190923/195613.html'  # 2

res = requests.get(url, headers=headers)
res.encoding = 'gb2312'
html = res.text
# print(html)


# 解析网页
# dir_name = re.findall('<a href=.+?alt="(.+?)" src=.+?</a>', html)[0]
# urls = re.findall('<a href=.+?><img alt=.+?src="(.+?)".+?</a>', html)  # 1
urls = re.findall("<div.*?href=.*?href='.*?src=(.*?).*?</a></a></div>", html)  # 2

# print(urls)
# print(dir_name)







# 保存图片
# for url in urls:
#     # 图片名字
#     file_name = url.split('/')[-1]
#     res = requests.get(url, headers=headers)
#     with open(file_name, "wb")as f:
#         f.write(res.content)