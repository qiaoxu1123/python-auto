from framework.browser_engine import BrowserEngine
import unittest
import time

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # selfUp()的代码，主要是测试的前提准备工作
        browser = BrowserEngine()
        self.driver = browser.open_browser()

    def tearDown(self):
        # tearDown()的代码，主要是测试结束后要做的工作  基本上都是关闭浏览器
        time.sleep(3)
