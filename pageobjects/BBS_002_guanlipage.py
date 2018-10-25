from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from selenium import  webdriver
import time

class GuanLiPage(BasePage):

    # 输入密码
    guanli_page_input_pwd_loc = (By.NAME, 'admin_password')
    # 点击提交按钮
    guanli_page_button_submit_loc = (By.NAME, 'submit')
    # 点击论坛
    guanli_page_a_luntan_loc = (By.ID, 'header_forum')
    # 添加新的模块
    guanli_page_button_mokuai_loc = (By.CSS_SELECTOR, '#cpform table tbody:nth-child(3) tr td:nth-child(2) div a')
    # 清楚文本内容
    guanli_page_input_clear_loc = (By.CSS_SELECTOR, 'tbody:nth-child(3) tr:nth-child(1) td:nth-child(3) div input')
    # 点击提交按钮
    guanli_page_button_tijiao_loc = (By.ID, 'submit_editsubmit')
    # 退出
    # self.driver.switch_to.default_content()#跳出iframe模块
    # guanli_page_button_quit_loc = (By.CSS_SELECTOR, '#frameuinfo p:nth-child(1) a')


    def guanli1(self, pwd):
        self.sendkeys(pwd, *self.guanli_page_input_pwd_loc)
        time.sleep(2)
        self.click(*self.guanli_page_button_submit_loc)
        time.sleep(2)

    def guanli2(self, newbankuai):
        self.click(*self.guanli_page_a_luntan_loc)
        time.sleep(2)
        self.driver.switch_to.frame('main')
        self.click(*self.guanli_page_button_mokuai_loc)
        time.sleep(2)
        self.sendkeys(newbankuai, *self.guanli_page_input_clear_loc)
        time.sleep(2)
        self.click(*self.guanli_page_button_tijiao_loc)
        # self.click(*self.guanli_page_button_quit_loc)
        self.driver.close()
        time.sleep(2)

