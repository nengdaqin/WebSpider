import requests
import json

session = requests.Session()

# 登录
def login():
    login_url = "http://ihrm-test.itheima.net/api/sys/login"
    headers = {"Content-Type": "application/json"}

    # 将python对象解码为json数据(不进行这一步,会以无参的形式进行post请求)
    json_data = json.dumps({"mobile": "13800000002", "password": "123456"})

    resp = session.post(login_url, json_data, headers=headers)
    token_data = resp.json()
    # 遍历返回的响应信息
    token = [v for k, v in token_data.items()]
    return token[3]  # 取 data的值

def search(token):
    url = "http://ihrm-test.itheima.net/api/sys/profile"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    response = requests.post(url, headers=headers)
    return response

def main():
    token = login()
    response = search(token)
    print(response.url)  # 响应url
    print(response.encoding)  # 响应的编码
    print(response.cookies)  # 响应的cookies
    print(response.headers)  # 响应头
    print("search response data = ", response.json())  # 响应的json数据

if __name__ == '__main__':
    main()