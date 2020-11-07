# 起点中文网 (从吞噬星空崛起)
import requests
from lxml import etree

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

# 3.第(2)步url
for novel_url in novel_url_list:
    new_url = "https:" + novel_url + "#Catalog"
    print(new_url)

    # 第2次发送请求
    resp = requests.get(new_url, headers=headers).content.decode("utf-8")
    # 转换数据
    page_html = etree.HTML(resp)
    # print(page_html)
    # 小说名
    novel_name = page_html.xpath('//div[@class="book-info"]/h1/em/text()')
    # print(novel_name)

# 章节url
#     catalog_url_list = page_html.xpath('//div[@class="volume-wrap"]/div/ul/li/a/@href')
#     for catalog_url in catalog_url_list:
#         # 第(3)步url  (pass)
#         detail_url = "https:" + catalog_url
#
#         print(detail_url)

        # 第3次发送请求
        # resp = requests.get(detail_url, headers=headers).content.decode("utf-8")
        # detail_html = etree.HTML(resp)
        # # 章节名
        # title_list = etree.HTML('//div[@class="volume"]/ul/li/a/text()')
        # # 章节正文
        # novel_text = "\n".join(detail_html('//div[@class="read-content j_readContent"]/p/span/text()'))
        # file_name = "".join(novel_name) + ".txt"

        # 4.保存数据
        # "a+":以追加的形式写入
    #     with open(file_name, "a+", encoding="utf-8") as f:
    #         f.write("------" + "".join(title_list)[-1] + "------" + "\n")
    #         f.write(novel_text + "\n")  # 换行
    #         print("".join(title_list[-1] + '-----抓取完成'))
    # print("抓取完成")





