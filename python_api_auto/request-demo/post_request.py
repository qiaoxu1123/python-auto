import requests
import unittest

class Test_login(unittest.TestCase):
    url = 'https://passport.womai.com/login/login.do'

    headers = {'Accept': 'application/json, text/javascript, */*',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Content-Length': '177',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Host': 'passport.womai.com',
               'Origin': 'https: // passport.womai.com',
               'Referer': 'https: // passport.womai.com / redirect / redirect.do?mid = 0 & returnUrl = http % 3',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400',
               'X-Requested-With': 'XMLHttpRequest'}

    payload = {'serverPath': 'http://www.womai.com/',
               'loginId': 'qiaoxu1123',
               'password': 'haotest2018',
               'validateCode': '',
               'tempcode': '',
               'mid': '0',
               'returnUrl': 'http://www.womai.com/index-31000-0.htm'}

    def test_login(self):
        response = requests.post(self.url, headers=self.headers, data=self.payload)
        json_data = response.json()
        print(json_data)

        # 断言：测试结果与期望结果对比
        self.assertEqual('2', json_data['msg'])

if __name__ == '__main__':
    unittest.main()