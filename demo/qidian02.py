import requests
import json

# 7，请使用requests模块编写代码访问 员工管理模块用户资料查询接口，
# 并输出该接口返回响应数据中的url，encoding，cookies，headers，以及响应数据(可以先不做)
#
# - 建议使用requests来实现
session = requests.Session()


# 登录
login_url = "http://ihrm-test.itheima.net/api/sys/login"
headers = {"Content-Type": "application/json"}

# 将python对象解码为json数据(不进行这一步,会以无参的形式进行post请求)
json_data = json.dumps({"mobile": "13800000002", "password": "123456"})

resp = session.post(login_url, json_data, headers=headers)
# print("register response data = ", resp.json())
token_data = resp.json()
# 遍历返回的响应信息
token = [v for k, v in token_data.items()]
# print(token[3])

# 查询
url = "http://ihrm-test.itheima.net/api/sys/profile"
headers = {"Authorization": "Bearer " + token[3]}
print(headers)
response = requests.post(url, headers=headers)
print("register response data = ", response.json())
print(response.cookies)