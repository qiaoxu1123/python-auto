from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from testsuite.basetestcase import BaseTestCase
import unittest
import time


class BaiduSearch(BaseTestCase):

    def test_baidu_search(self):
        # 测试方法必须要以test开头
        self.driver.find_element_by_id('kw').send_keys('selenium' +Keys.RETURN)
        time.sleep(2)
        assert "selenium" in self.driver.title

if __name__ == "__main__":
    unittest.main()