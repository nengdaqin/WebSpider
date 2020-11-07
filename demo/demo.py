import requests
from lxml import etree

header = {
    'User-Agent': '',

    'cookie': ''

}



detail_urls = []
# 获取详情页面url
def get_detail_urls(url):
    # 获取详情url
    resp = requests.get(url, headers=header)
    text = resp.content.decode('utf-8')
    html = etree.HTML(text)
    ul = html.xpath('//ul[@class="carlist clearfix js-top"]')[0]
    # print(ul)
    lis = ul.xpath('./li')
    for li in lis:
        detail_url = li.xpath('./a/@href')
        detail_url = 'https://www.guazi.com'+detail_url[0]
        detail_urls.append(detail_url)
    return detail_urls

# 解析详情页面内容
def parse_detail_page(url):
    resp = requests.get(url, headers=header)
    text = resp.content.decode('utf-8')
    html = etree.HTML(text)
    title = html.xpath('//div[@class="product-textbox"]/h2/text()')[0]
    title = title.replace(r'\r\n', '').strip()
    # print(title)
    info = html.xpath('//div[@class="product-textbox"]/ul/li/span/text()')
    # print(len(info))
    infos = {}
    km = info[2]
    displacement = info[3]
    speed_box = info[4]

    infos['title'] = title
    infos['km'] = km
    infos['displacement'] = displacement
    infos['speedbox'] = speed_box
    return infos

# 保存数据
def save_info(infos,f):
    f.write('{},{},{},{}\n'.format(infos['title'],infos['km'],infos['displacement'],infos['speedbox']))
def main():
    # 第一个url
    base_url = 'https://www.guazi.com/cs/buy/o{}/'
    with open('guazi_cs.csv', 'a', encoding='utf-8') as f:
        for x in range(1, 6):
            url = base_url.format(x)
            # 获取详情页面url
            car_urls = get_detail_urls(url)
            # 解析详情页面内容
            for detail_url in car_urls:
                infos = parse_detail_page(detail_url)
                save_info(infos, f)

if __name__ == '__main__':
    main()


