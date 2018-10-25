import os
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

# 自动化安装apk包到手机
apk_path = os.path.dirname(os.path.abspath('.'))

class AddAndroidTests(unittest.TestCase):
    # @classmethod
    def setUp(self):

        desired_caps = {}
        # 设备系统
        desired_caps['platformName'] = 'Android'
        # 设备系统版本
        desired_caps['platformVersion'] = '6.0.1'
        # 设备名称
        desired_caps['deviceName'] = '127.0.0.1:21503'

        # 每次运行新建session
        desired_caps['sessionOverride'] = True
        # 不需要每次都安装apk
        desired_caps['noReset'] = True
        # 应用程序的包名
        desired_caps['appPackage'] = 'com.example.todolist'
        desired_caps['appActivity'] = 'com.example.todolist.LoginActivity'
        # 测试apk包的路径
        desired_caps['app'] = apk_path + '/app/todolist.apk'
        # 启动app
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_elements(self):
        # pause a moment, so xml generation can occur
        sleep(2)

        self.driver.find_element_by_id('com.example.todolist:id/nameET').send_keys('1')
        # self.driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys('1')
        # driver.find_element_by_class_name('android.widget.EditText').send_keys('1')
        # driver.find_element_by_class_name('android.widget.EditText').send_keys('1')
        self.driver.find_element_by_xpath('//android.widget.EditText[2]').send_keys('1')
        self.driver.find_element_by_id('com.example.todolist:id/loginBtn').click()

        sleep(2)
        self.driver.find_element_by_id('com.example.todolist:id/action_new').click()
        # self.driver.find_element_by_xpath('//android.widget.TextView').click()
        self.driver.find_element_by_id('com.example.todolist:id/toDoItemDetailET').send_keys('1111')
        sleep(2)
        self.driver.find_element_by_id('com.example.todolist:id/saveBtn').click()

        sleep(2)
        action1 = TouchAction(self.driver)
        el = self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.RelativeLayout')
        action1.long_press(el).wait(10000).perform()

        sleep(2)
        self.driver.find_element_by_xpath(
            '//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout').click()

        self.driver.find_element_by_id('android:id/button1').click()




