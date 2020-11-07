import requests
from lxml import etree


# 发送请求获取需要的url
def get_url(url):
    response = requests.get(url).content.decode("utf-8")

