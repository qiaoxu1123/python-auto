import requests
import json
URL = 'https://api.github.com'

def build_url(endpoint):
    # 主要作用拼接接口请求地址
    return '/'.join([URL, endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def request_method():
    response = requests.patch(build_url('users'), auth=('qiaoxu1123', 'haotest123456789haotest'), json={'company': 'haotest', 'emil': '544990162@qq.com'})
    print(better_output(response.text))

if __name__  == "__main__" :
    request_method()



