from appium import webdriver
import os

# 自动化安装apk包到手机
apk_path = os.path.dirname(os.path.abspath('.'))

desired_caps = {}
# 设备系统
desired_caps['platformName'] = 'Android'
# 设备系统版本
desired_caps['platformVersion'] = '6.0.1'
# 设备名称
desired_caps['deviceName'] = '127.0.0.1:21503'
# 手机28PNW17C29024401 夜神127.0.0.1:62001   逍遥127.0.0.1:21503
# 每次运行新建session
desired_caps['sessionOverride'] = True
# 不需要每次都安装apk
desired_caps['noReset'] = True
# 应用程序的包名
# desired_caps['appPackage'] = 'com.tal.kaoyan'
# desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

desired_caps['appPackage'] = 'com.example.todolist'
desired_caps['appActivity'] = 'com.example.todolist.LoginActivity'
# 测试apk包的路径
desired_caps['app'] = apk_path + '/app/todolist.apk'
# desired_caps['app'] = apk_path + '/app/kaoyanbang_42.apk'
# 启动app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.find_element_by_xpath('//driver.find_element_by_xpath[16]').click()


# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(ComplexAndroidTests)
#     unittest.TextTestRunner(verbosity=2).run(suite)
