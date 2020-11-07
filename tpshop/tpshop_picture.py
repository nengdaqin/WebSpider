import requests
from lxml import etree

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"

}

# 获取每个首页标题里的商品分类信息

url_list = []
# 获取第一个详情页面的title
def detail_url(url):
    resp = requests.get(url, headers=headers).content.decode("utf-8")
    html = etree.HTML(resp)
    li_url = html.xpath('//ul[@class="navitems clearfix"]/li/a/@href')

    # 遍历li标签
    for li in li_url:
        details_url = "http://shop.qyw2017.com" + li
        url_list.append(details_url)
        # print(details_url)
    print(url_list)

# 解析详情页面内容
# def parse_detail_page(details_url):
#     resp = requests.get(details_url, headers=headers).content.decode("utf-8")
#     html = etree.HTML(resp)
#     title = html.xpath('//div[@class="opt-list"]//dl/dt/text()')
#     text = html.xpath('//div[@class="opt-list"]//dl/dd//div/a/span/text()')
#     print(title)
#     print(text)
#
base_url = "http://shop.qyw2017.com/index.php/"
detail_url(base_url)

