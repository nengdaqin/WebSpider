import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'

}

# url = "https://www.qidian.com/free/all?chanId=21"
url = "https://read.qidian.com/chapter/i6RYcHPknkTZ6ZDT--NUMw2/hOhbnT8PkQPM5j8_3RRvhw2"

# 2.发送请求
resp = requests.get(url, headers=headers).content.decode("utf-8")
# 转换数据
html = etree.HTML(resp)

text = html.xpath('/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/p')
print(resp)
