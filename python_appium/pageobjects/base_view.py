from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from framework.logger import Logger
import time
import os.path

logger = Logger(logger="BaseView").getlog()

class BaseView(object):

    def __init__(self, driver):
        # 初始化driver
        self.driver = driver

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            # logger.info("找到页面元素-->", loc)
        except:
            logger.error("%s 页面中未能找到%s元素" % (self, loc))

        # 点击元素
    def click(self, *loc):
        elem = self.find_element(*loc)
        try:
            logger.info("The element %s was clicked." % elem.text)
            elem.click()
        except Exception as e:
            logger.error("Faild to click the element with %s" % e)

    # 输入
    def sendkeys(self, text, *loc):
        elem = self.find_element(*loc)
        # elem.clear()
        try:
            elem.send_keys(text)
            logger.info("Input success")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s" % e)

    # 点击元素
    def click(self, *loc):
        elem = self.find_element(*loc)
        try:
            logger.info("The element %s was clicked." % elem.text)
            elem.click()
        except Exception as e:
            logger.error("Faild to click the element with %s" % e)

    # 长按
    def long_press(self, *loc):
        elem = self.find_element(*loc)
        try:
            TouchAction(self.driver).long_press(elem).wait(10000).perform()
            logger.info("长按成功")
        except:
            logger.error("Faild")

    def get_windows_img(self):
        """
        在这里把file_path这个参数写死 直接保存到项目根目录的一个文件夹/screenshots/下
        :return:
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except Exception as e:
            logger.error("Failed to take screenshot! %s" % e)

    def back(self):
        # 浏览器后退按钮
        self.driver.back()
        logger.info("Click back on current page")

    def forward(self):
        # 浏览器前进按钮
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 清除文本框
    def clear(self, *loc):
        elem = self.find_element(*loc)
        try:
            elem.clear()
            logger.info("Cleanup succeeded")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s" % e)

    # 激活窗口
    def activate(self):
        try:
            self.driver.switch_to.window(self.driver.current_window_handle)
            logger.info("The current window to activate success")
        except:
            logger.error("The current window to activate faild")

    # def find_elements(self, *loc):
    #     return self.driver.find_elements(*loc)
    #
    # def get_window_size(self):
    #     return self.driver.get_window_size()
    #
    # def swipe(self, start_x, start_y, end_x, end_y, duration):
    #     return self.driver.swipe(start_x, start_y, end_x, end_y, duration)