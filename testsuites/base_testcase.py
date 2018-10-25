from framework.desired_caps import DesiredCaps
import unittest
import time

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # selfUp()的代码，主要是测试的前提准备工作
        desired = DesiredCaps()
        self.driver = desired.appium_desired()

    def tearDown(self):
        # tearDown()的代码，主要是测试结束后要做的工作  基本上都是关闭浏览器
        time.sleep(3)
        self.driver.quit()