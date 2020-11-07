from urllib.parse import urlencode
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'
"https://tuchong.com/rest/tags/%E5%9F%8E%E5%B8%82/posts?page=1&count=20&order=weekly&before_timestamp="


headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page
    }

    url = base_url + urlencode(params)

    try:
        response = requests.get(url, heafers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)
