from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger
import time

logger = Logger(logger="SouSuo").getlog()

class SouSuo(BasePage):

    # 验证信息定位
    sousuo_page_a_yanzheng_loc = (By.CSS_SELECTOR, '.pbw .xs3 a')
    sousuo_page_text_yanzheng_loc = (By.ID, 'thread_subject')

    sousuo_page_button_quit_loc = (By.CSS_SELECTOR, '#um p:nth-child(2) a:nth-child(13)')

    def yanzheng1(self):
        self.click(*self.sousuo_page_a_yanzheng_loc)

    def yanzheng2(self):
        text = self.sousuo_page_text_yanzheng_loc
        try:
            assert 'qiaoxu111' in self.driver.title
            logger.info("success")
        except:
            logger.error("Filed")

    def quit(self):
        self.click(*self.sousuo_page_button_quit_loc)
