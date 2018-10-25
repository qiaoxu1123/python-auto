from selenium.webdriver.common.keys import Keys
from testsuite.basetestcase import BaseTestCase
from pageobjects.baidu_homepage import HomePage
import unittest
import time


class BaiduSearch(BaseTestCase):

    def test_baidu_search(self):
        # 这里一定要test开头  那测试逻辑代码封装到一个test开头的方法里

        # 声明HomePage类对象
        home_page = HomePage(self.driver)
        home_page.open_url("https://www.baidu.com")

        # 调用首页搜索功能
        home_page.search('selenium')
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()