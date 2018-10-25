import json

import requests

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL, endpoint])
    # 主要作用是拼接接口请求地址


def better_output(json_str):
    return json.dumps(json.loads(json_str), indent=4)
    # 采用json里面提供方法打印出来，格式更好看


def json_method():
    response = requests.patch(build_uri('user'),
                              auth=(), json={'company': 'haotest',
                                             'email': 'lihanhuan@haotest.com'})
    print(better_output(response.text))


if __name__ == '__main__':
    json_method()
