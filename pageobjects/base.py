from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from framework.logger import Logger
from selenium import webdriver
import time
import os.path

logger = Logger(logger="BasePage").getlog()


class BasePage(object):

    def __init__(self, driver):
        # 初始化driver
        self.driver = driver

    def back(self):
        # 浏览器后退按钮
        self.driver.back()
        logger.info("Click back on current page")

    def forward(self):
        # 浏览器前进按钮
        self.driver.forward()
        logger.info("Click forward on current page.")

    def open_url(self, url):
        # 打开url站点
        self.driver.get(url)

    def quit_browser(self):
        # 关闭并停止浏览器服务
        self.driver.quit()

    def close(self):
        # 点击关闭当前窗口
        try:
            self.driver.close()
            logger.info("Closing adn quit the browser.")
        except Exception as e:
            logger.error("Failed to quit the browser with ")

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素-->", loc)
        except:
            logger.error("%s 页面中未能找到%s元素" % (self, loc))

        # 保存图片

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
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s" % e)

        # 输入

    def sendkeys(self, text, *loc):
        elem = self.find_element(*loc)
        elem.clear()
        try:
            elem.send_keys(text)
            logger.info("Input success")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s" % e)

        # 清除文本框
    def clear(self, *loc):
        elem = self.find_element(*loc)
        try:
            elem.clear()
        except Exception as e:
            self.get_windows_img()
            # logger.error("Failed to take screenshot! %s" % e)

    # 点击元素
    def click(self, *loc):
        elem = self.find_element(*loc)
        try:
            logger.info("The element %s was clicked." % elem.text)
            elem.click()
            # print("The element %s was clicked." % elem.text)
        except Exception as e:
            logger.error("Faild to click the element with %s" % e)
            # print("Faild to click the element with %s" % e)

    # 激活窗口
    def activate(self):
        try:
            self.driver.switch_to.window(self.driver.current_window_handle)
            logger.info("The current window to activate success")
        except:
            logger.error("The current window to activate faild")

    # def move(self, *loc):
    #     elem = self.find_element(*loc)
    #     try:
    #         elem.move()
    #         print("The mouse moved to the element")
    #     except Exception as e:
    #         print("Faild to click the element with %s" % e)

    def print1(self, *loc):
        elem = self.find_element(*loc)
        try:
            logger.info("The element %s was print." % elem.text)
        except Exception as e:
            logger.error("Faild")