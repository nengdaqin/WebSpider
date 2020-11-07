from lxml import etree
import requests

# headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
#                      'application/signed-exchange;v=b3',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Cache-Control': 'max-age=0',
# 'Connection': 'keep-alive',
# 'Cookie': 'fikker-spEH-SVuL=SKuZGHo8IKJMQDideJaIQVcfyHkFLb9H; fikker-spEH-SVuL=SKuZGHo8IKJMQDideJaIQVcfyHkFLb9H; '
#           'Hm_lvt_e73fd8f9f7e092a67d6a312a933f5525=1586390925,1586398042,1586418821,1586431465; '
#           'Hm_lpvt_e73fd8f9f7e092a67d6a312a933f5525=1586431465; jieqiVisitId=article_articleviews%3D1',
# 'Host': 'www.biqooge.com',
# 'Sec-Fetch-Mode': 'navigate',
# 'Sec-Fetch-Site': 'none',
# 'Sec-Fetch-User': '?1',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 '
#               'Safari/537.36 '
# }


# 获取第一个详情页面的title
def get_detail_url(url):
    response = requests.get(url)
    text = response.content.decode("utf-8")
    html = etree.HTML(text)
    ul = html.xpath("//div[@class='nav w1224 clearfix']/ul")[0]
    # print(ul)
    lis = ul.xpath("./li")  # /a/@href
    # 创建一个列表来接收返回的urls
    detail_urls = []
    for li in lis:
        detail_url = li.xpath("./a/@href")
        detail_url = "http://shop.qyw2017.com/" + detail_url[0]
        detail_urls.append(detail_url)
        # print(detail_urls)
    return detail_urls

url = "http://shop.qyw2017.com/"
detail_urls = get_detail_url(url)

# 解析详情页面内容
def parse_detail_page(url):
    response = requests.get(url)
    text = response.content.decode("utf-8")
    html = etree.HTML(text)
    title = html.xpath("//div[@class='opt-list']/dl/dt/text()")
    title = html.xpath('//div[@class="opt-list"]/dl/dd/div/div/div/a/span/text()')
    print(title)


# detail_urls = get_detail_urls(url)

def main():
    # url = "http://shop.qyw2017.com/"
    url = "http://shop.qyw2017.com/index.php/Home/Goods/goodsList/id/32"

    # get_detail_url(url)
    parse_detail_page(url)


if __name__ == '__main__':
    main()

# def save_data(infoS):
# #     with open("shopInfo.txt", "w", encoding="utf-8") as f:
# #
# #         f.write(json.dumps(infoS, ensure_ascii=True))
