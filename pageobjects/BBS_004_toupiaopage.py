from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger
import time

logger = Logger(logger="SouSuo").getlog()

class TouPiao(BasePage):

    # 发起投票内容
    toupiao_page_input_title_loc = (By.NAME, 'subject')
    toupiao_page_input_neirong1_loc = (By.CSS_SELECTOR, '#pollm_c_1 p:nth-child(1) .px.vm')
    toupiao_page_input_neirong2_loc = (By.CSS_SELECTOR, '#pollm_c_1 p:nth-child(2) .px.vm')
    toupiao_page_input_neirong3_loc = (By.CSS_SELECTOR, '#pollm_c_1 p:nth-child(3) .px.vm')
    # 选项框（所有人可见)
    toupiao_page_input_all_loc = (By.ID, 'visibilitypoll')
    # 点击发起投票
    toupiao_page_button_faqi_loc = (By.ID, 'postsubmit')
    # 选择
    toupiao_page_input_xuanze_loc = (By.ID, 'option_3')
    # 投票
    toupiao_page_button_toupiao1_loc = (By.ID, 'pollsubmit')

    def toupiaopage1(self, title, n1, n2, n3):
        self.sendkeys(title, *self.toupiao_page_input_title_loc)
        time.sleep(1)
        self.sendkeys(n1, *self.toupiao_page_input_neirong1_loc)
        time.sleep(1)
        self.sendkeys(n2, *self.toupiao_page_input_neirong2_loc)
        time.sleep(1)
        self.sendkeys(n3, *self.toupiao_page_input_neirong3_loc)
        time.sleep(3)

    def toupiaopage2(self):
        self.click(*self.toupiao_page_input_all_loc)
        time.sleep(2)
        self.click(*self.toupiao_page_button_faqi_loc)
        time.sleep(2)
        self.click(*self.toupiao_page_input_xuanze_loc)
        time.sleep(2)
        self.click(*self.toupiao_page_button_toupiao1_loc)

    # 取出投票各个选项的名称以及投票比例
    # 取出投票的主题名称

    toupioa_page_text_a1_loc = (By.CSS_SELECTOR, '.pvt label')
    toupioa_page_text_a2_loc = (By.CSS_SELECTOR, '.pcht table tbody tr:nth-child(2) td:nth-child(2)')
    toupioa_page_text_b1_loc = (By.CSS_SELECTOR, '.pcht table tbody tr:nth-child(3) .pvt label')
    toupioa_page_text_b2_loc = (By.CSS_SELECTOR, '.pcht table tbody tr:nth-child(4) td:nth-child(2)')
    toupioa_page_text_c1_loc = (By.CSS_SELECTOR, '.pcht table tbody tr:nth-child(5) .pvt label')
    toupioa_page_text_c2_loc = (By.CSS_SELECTOR, '.pcht table tbody tr:nth-child(6) td:nth-child(2)')
    toupiao_page_text_title_loc = (By.ID, 'thread_subject')

    def toupiaopage3(self):
        self.print1(*self.toupioa_page_text_a1_loc)
        self.print1(*self.toupioa_page_text_a2_loc)
        self.print1(*self.toupioa_page_text_b1_loc)
        self.print1(*self.toupioa_page_text_b2_loc)
        self.print1(*self.toupioa_page_text_c1_loc)
        self.print1(*self.toupioa_page_text_c2_loc)

        # print("选项名称：", self.a1.text, "投票比例：", self.a2.text)
        # print("选项名称：", self.b1.text, "投票比例：", self.b2.text)
        # print("选项名称：", self.c1.text, "投票比例：", self.c2.text)
        # print("主题名称：", self.bt.text)




