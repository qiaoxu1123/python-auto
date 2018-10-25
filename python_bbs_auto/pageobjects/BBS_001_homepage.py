from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):

    # 用户名
    home_page_input_username_loc = (By.ID, 'ls_username')
    # 密码
    home_page_input_password_loc = (By.ID, 'ls_password')
    # 点击登陆按钮
    home_page_button_search_loc = (By.CSS_SELECTOR, '.fastlg_l .pn.vm em')
    # 搜索框
    home_page_input_sousuok_loc = (By.ID, 'scbar_txt')
    # 搜索按钮
    home_page_button_sousuoa_loc = (By.ID, 'scbar_btn')
    #点击Discuz!
    home_page_a_discuz_loc = (By.CSS_SELECTOR, '#pt div a:nth-child(5)')
    # 点击默认板块
    home_page_a_moren_loc = (By.CSS_SELECTOR, '#category_1 .fl_tb tbody tr td:nth-child(2) h2 a')
    # 点击退出（001）
    home_page_a_quit_loc = (By.CSS_SELECTOR, '#um p:nth-child(2) a:nth-child(18)')
    # 点击退出（002）
    home_page_a_quit2_loc = (By.CSS_SELECTOR, '#um p:nth-child(2) a:nth-child(13)')
    # 点击管理中心
    hame_page_a_guanli_loc = (By.CSS_SELECTOR, '#um p:nth-child(2) a:nth-child(16)')


    # 输入搜索内容并提交
    # 登陆部分
    def login1(self, username):
        self.sendkeys(username, *self.home_page_input_username_loc)
        time.sleep(2)

    def login2(self, password):
        self.sendkeys(password, *self.home_page_input_password_loc)
        time.sleep(2)
        self.click(*self.home_page_button_search_loc)
        time.sleep(2)

    # 搜索框
    def sousuo(self, ss):
        self.sendkeys(ss, *self.home_page_input_sousuok_loc)
        time.sleep(2)
        self.click(*self.home_page_button_sousuoa_loc)
        time.sleep(2)

    def discuz(self):
        self.click(*self.home_page_a_discuz_loc)

    # 默认板块
    def moren(self):
        self.click(*self.home_page_a_moren_loc)
    # 退出
    def quit(self):
        self.click(*self.home_page_a_quit_loc)
    # 管理中心
    def guanli(self):
        self.click(*self.hame_page_a_guanli_loc)

    def quit2(self):
        self.click(*self.home_page_a_quit2_loc)






