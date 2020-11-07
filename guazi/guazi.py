import requests
from lxml import etree
import time
import os
import csv


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.111 Safari/537.36",

    "Cookie": "uuid=44c74231-3a05-43d8-fdef-642b17ac2f79; ganji_uuid=3126244650101135279950; lg=1; cityDomain=sz; "
              "track_id=135408883602464768; antipas=89936B0y52l85952709281308Y; clueSourceCode=%2A%2300; "
              "user_city_id=17; preTime=%7B%22last%22%3A1603805975%2C%22this%22%3A1601221141%2C%22pre%22%3A1601221141"
              "%7D; sessionid=3d5c6872-3ab4-4841-8863-a916a1852f60; "
              "cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A"
              "%22pcbiaoti%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C"
              "%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C"
              "%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A"
              "%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%22135408883602464768%22%2C%22display_finance_flag%22"
              "%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2244c74231-3a05-43d8-fdef-642b17ac2f79%22%2C"
              "%22ca_city%22%3A%22sz%22%2C%22sessionid%22%3A%223d5c6872-3ab4-4841-8863-a916a1852f60%22%7D; "
              "lng_lat=113.89792_22.56617; gps_type=1; close_finance_popup=2020-10-27 "




}

# 获取瓜子二手车宝马类

# url层级关系
# 第一层:"https://www.guazi.com/sz/"
# 第二层:https://www.guazi.com/sz/bmw/
# 第三层:"https://www.guazi.com/sz/a51c5d632699f10ex.htm#fr_page=list&fr_pos=city&fr_no=0"


url = "https://www.guazi.com/sz/"
# 1.发起请求
resp = requests.get(url, headers=headers).content.decode("utf-8")
html = etree.HTML(resp)

# 提取汽车url
cars_url = html.xpath('//div[@class="buycar-brand clearfix marginTop13"]/a/@href')

# 第二层url

for car_url in cars_url:
    list_url = "https://www.guazi.com" + car_url
    # print(list_url)


# # 第二次发送请求
    car_resp = requests.get(list_url, headers=headers).content.decode("utf-8")
    car_html = etree.HTML(car_resp)
    lis_url = car_html.xpath('//ul[@class="carlist clearfix js-top"]/li/a/@href')  # 详情汽车页
    # print(details_url)

    for li in lis_url:
        detail_url = "https://www.guazi.com" + li

        # 第三次发送请求
        detail_resp = requests.get(detail_url, headers=headers).content.decode("utf-8")
        detail_html = etree.HTML(detail_resp)

        # 汽车标题
        title = "".join(detail_html.xpath('//div[@class="center js-center detail"]/div/div/h2/text()'))
        # title = (detail_html.xpath('//div[@class="center js-center detail"]/div/div/h2/text()'))
        titles = [x.strip() for x in title if x.strip() != '']
        # print(title)
        # 公里数、排量、变速箱
        car_info = (detail_html.xpath('//ul[@class="basic-eleven clearfix"]/li/div/text()'))
        lis_info = [x.strip() for x in car_info if x.strip() != '']

        km = lis_info[0]
        displacement = lis_info[3]
        gearbox = lis_info[2]
        index = lis_info[1]
        register_num = lis_info[4]
        mode = lis_info[5]
        use = lis_info[6]
        property_right = lis_info[7]

        cars_info = {
            "km": km, "displacement": displacement, "gearbox": gearbox, "index": index, "register_num": register_num,
            "mode": mode, "use": use, "property_right": property_right}
        # print(cars_info)

        # 4.保存数据
        download_path = r"E:\project\web_spider\guazi\data"
        if not os.path.exists(download_path):
            os.mkdir(download_path)
        name = download_path + "/" + "guazi.csv"

        header = ["km", "displacement", "gearbox", "index", "register_num", "mode", "use", "property_right"]

        time.sleep(3)
        with open(name, "a", encoding="utf-8", newline="") as fp:
            write = csv.DictWriter(fp, header)

            # 已读的方式打开文件，reader判断一下标题是否存在
            with open("./data/guazi.csv", "r", encoding="utf-8", newline="") as f:
                reader = csv.reader(f)
                # 如果表头为空则打印，不为空就不打印
                if not [row for row in reader]:
                    write.writeheader()
                    write.writerow(cars_info)

                else:
                    write.writerow(cars_info)

            print("{}抓取完成".format(title))