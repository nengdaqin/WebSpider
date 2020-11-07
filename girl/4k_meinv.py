import requests
from lxml import etree
import os

if __name__ == "__main__":
    # URL地址
    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    # 创建文件夹保存图片数据
    if not os.path.exists(r'E:\\project\web_spider\girl\imgs'):
        os.mkdir(r'E:\\project\web_spider\girl\imgs')

    # 爬取页面源数据
    response = requests.get(url=url, headers=headers)
    # response.encoding = 'gbk'
    page_text = response.text

    # 数据解析：src属性值、alt属性值
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    for li in li_list:
        # 获取图片的src属性值
        img_src = 'http://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
        # 获取图片的alt属性值
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')

        print(img_name,img_src)

        # 访问图片地址
        img_data = requests.get(url=img_src, headers=headers).content
        # 持久化存储图片数据
        img_path = r'E:\\project\web_spider\girl\imgs'+img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '打印成功！！！')

