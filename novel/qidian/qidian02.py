# 起点中文网 (从吞噬星空崛起)
import time

import requests
from lxml import etree
import os

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"

}

# 1.获取url
#      第(1)步:https://www.qidian.com/free/all?chanId=21
#      第(2)步:https://book.qidian.com/info/1023708557#Catalog
#      第(3)步:https://read.qidian.com/chapter/i6RYcHPknkTZ6ZDT--NUMw2/hOhbnT8PkQPM5j8_3RRvhw2

url = "https://www.qidian.com/free/all?chanId=21"
# 2.发送请求
resp = requests.get(url, headers=headers).content.decode("utf-8")
# 转换数据
html = etree.HTML(resp)
novel_url_list = html.xpath('//div/ul[@class="all-img-list cf"]/li/div/a/@href')

# 定义一个列表接收url
new_urls = []
# 3.第(2)步url
for novel_url in novel_url_list:
    new_url = "https:" + novel_url + "#Catalog"
    new_urls.append(new_url)

# 第2次发送请求
resp = requests.get(new_urls[7], headers=headers).content.decode("utf-8")
# 转换数据
page_html = etree.HTML(resp)

# 小说名
novel_name = page_html.xpath('//div[@class="book-information cf"]/div/h1/em/text()')


# 章节url
catalog_url_list = page_html.xpath('//div[@class="volume-wrap"]/div/ul/li/a/@href')
for catalog_url in catalog_url_list:
    # 第(3)步url  (pass)
    detail_url = "https:" + catalog_url

    # 第3次发送请求
    resp = requests.get(detail_url, headers=headers).content.decode("utf-8")
    detail_html = etree.HTML(resp)

    # 章节名
    title_list = "".join(detail_html.xpath('//head/title/text()')).split('_')[1]  # .split("_")[1]

    # 章节正文
    novel_text = "\n".join(detail_html.xpath('//div[@class="read-content j_readContent"]//p//text()'.strip("\u3000")))

    file_name = "".join(novel_name) + ".txt"

# 4.保存数据
    download_path = r"/web_spider/novel/novel_data"
    if not os.path.exists(download_path):
        os.mkdir(download_path)

    # "a+":以追加的形式写入
    name = download_path + "/" + file_name
    # 等待3s
    time.sleep(3)
    with open(name, "a+", encoding="utf-8") as f:
        f.write("------" + "".join(title_list) + "------" + "\n")
        f.write(novel_text + "\n")  # 换行
        print("".join(title_list + '-----抓取完成'))
print("抓取完成")





