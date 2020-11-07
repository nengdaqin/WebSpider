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
html = etree.HTML(resp)
# print(resp)

# 3.解析需要的数据
novel_url_list = html.xpath('//div/ul[@class="all-img-list cf"]/li/div/a/@href')
novel_url_list = "https:" + novel_url_list[7]
print(novel_url_list)

# novel_title = html.xpath("")

# 请求解析的第二页url
detail_url = requests.get(novel_url_list, headers=headers).content.decode("utf-8")
detail_html = etree.HTML(detail_url)
# 解析li标签中的url
lis_url = detail_html.xpath('//div[@class="volume-wrap"]/div/ul/li/a/@href')
# print(lis_url)
# 小说名
# novel_name = detail_html.xpath('//div[@class="book-info"]/h1/em/text()')
# print(novel_name)

details_page = []
# print(details_url)
for detail in lis_url:
    details = "https:" + detail
    details_page.append(details)

page_resp = requests.get(details_page, headers=headers).content.decode("utf-8")
page_html = etree.HTML(page_resp)
# 章节标题
page_title = etree.HTML('//h3[@class="j_chapterName"]/span/text()')[0]
# 文本内容
page_text = page_html.xpath('//div[@class="read-content j_readContent"]/p/span/text()')
print(page_text)



# 请求每个章节的url


# details = []






# 4.保存数据
