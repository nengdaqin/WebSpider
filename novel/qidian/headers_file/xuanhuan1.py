# coding=utf-8
"""
@Time    : 2020/10/26 19:39
@Author  : nengdaqin
@File    : xuanhuan1.py
"""
import requests
import re

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",

        "Cookie": "_csrfToken=8xS14ovSEUGka0KZk2PODGycaqGJSPb4lPpLDZ3V; newstatisticUUID=1603069046_1288729293; "
                  "qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; "
                  "lrbc=1023708557%7C571660236%7C0%2C1023718967%7C571767942%7C0%2C1023438690%7C565189988%7C0; "
                  "rcr=1023708557%2C1023718967%2C1023438690%2C1021668703; topGame=1; "
                  "e1=%7B%22pid%22%3A%22qd_P_mycenter%22%2C%22eid%22%3A%22qd_M11%22%2C%22l1%22%3A1%7D; "
                  "e2=%7B%22pid%22%3A%22qd_P_mycenter%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A2%7D; "
                  "newstatisticSID=1603713057_568330432 "

    }

url = "https://www.qidian.com/"
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
print(resp.text)

# print(resp.text)