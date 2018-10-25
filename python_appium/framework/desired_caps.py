from configparser import ConfigParser
# from framework.logger import Logger
# from appium import webdriver
# import os
#
# # 获取初始化好的logger对象
# logger = Logger(logger="DesiredCaps").getlog()
#
# # 自动化安装apk包到手机
# apk_path = os.path.dirname(os.path.abspath('.'))
#
# class DesiredCaps(object):
#
#     def appium_desired(self):
#
#         desired_caps = {}
#         # 设备系统
#         desired_caps['platformName'] = 'Android'
#         # 设备系统版本
#         desired_caps['platformVersion'] = '6.0.1'
#         # 设备名称
#         desired_caps['deviceName'] = '127.0.0.1:21503'
#         # 手机e382ee26 夜神127.0.0.1:62001   逍遥127.0.0.1:21503
#
#         # 每次运行新建session
#         desired_caps['sessionOverride'] = True
#         # 不需要每次都安装apk
#         desired_caps['noReset'] = True
#
#         # 应用程序的包名
#         # desired_caps['appPackage'] = 'com.tal.kaoyan'
#         # desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
#         desired_caps['appPackage'] = 'com.example.todolist'
#         desired_caps['appActivity'] = 'com.example.todolist.LoginActivity'
#         # 测试apk包的路径
#         desired_caps['app'] = apk_path + '/app/todolist.apk'
#         # desired_caps['app'] = apk_path + '/app/kaoyanbang_42.apk'
#         # 启动app
#         driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
#         return driver

from configparser import ConfigParser
from framework.logger import Logger
from appium import webdriver
import os

#获取初始化好的logger对象
logger = Logger(logger='AppiumDedired').getlog()

class DesiredCaps(object):

    def appium_desired(self):

        # 选择路径，读取ini文件
        config=ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path, encoding='utf-8')

        # 配置
        desired_caps={}

        # 设备系统
        desired_caps['platformName'] = config.get('deviceType', 'platformName')
        logger.info('设备系统platformName:%s', desired_caps['platformName'])

        # 设备系统版本
        desired_caps['platformVersion'] = config.get('platformName', 'platformVersion')
        logger.info('设备系统版本platformVersion:%s', desired_caps['platformName'])

        # 设备名称
        desired_caps['deviceName'] = config.get('platformName', 'deviceName')
        logger.info('设备名称deviceName:%s', desired_caps['deviceName'])

        # app_apk
        desired_caps['appPackage'] = config.get('appType', 'appPackage')
        logger.info('应用程序包名:%s', desired_caps['appPackage'])

        # app路径
        desired_caps['appname'] = config.get('appName', 'appname')
        dir = os.path.dirname(os.path.abspath('.'))
        desired_caps['apk_path'] = dir+'/app/'+desired_caps['appname']
        logger.info('app路径:%s',desired_caps['apk_path'])

        # 启动app
        desired_caps['noReset'] = config.get('appName', 'noReset')
        logger.info('不需要每次都安装apk, noReset:%s', desired_caps['noReset'])

        desired_caps['appActivity'] = config.get('appType', 'appActivity')
        logger.info('启动：%s', desired_caps['appActivity'])

        desired_caps['sessionOverride'] = config.get('appName', 'sessionOverride')
        logger.info('每次运行新建session:%s', desired_caps['sessionOverride'])

        # 配置实体：driver
        desired_caps['ip'] = config.get('appType', 'ip')
        desired_caps['port'] = config.get('appType', 'port')
        self.driver = webdriver.Remote('http://'+str(desired_caps['ip'])+':'+str(desired_caps['port'])+'/wd/hub', desired_caps)
        logger.info('实例化driver成功')


        self.driver.implicitly_wait(3)
        logger.info('隐式等待3秒')

        return self.driver
