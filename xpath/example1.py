import requests
from lxml import etree




def send_request(url):
    resp = requests.get(url).content.decode("utf-8")
    return resp

# 2.获取内容
def get_content(resp):
    html = resp.text
    return html


def main():
    url = "https://www.baidu.com"
    resp = send_request(url)
    print(resp)

if __name__ == '__main__':
    main()