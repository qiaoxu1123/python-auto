from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class PostPage(BasePage):
# 帖子标题
    post_page_input_title_loc = (By.NAME, 'subject')
    # 帖子内容
    post_page_input_neirong_loc = (By.ID, 'fastpostmessage')
    # 点击发表帖子
    post_page_button_fabiao_loc = (By.CSS_SELECTOR, '#fastpostsubmit strong')

# 发帖部分
    def post1(self, title):
        self.sendkeys(title, *self.post_page_input_title_loc)
        time.sleep(2)

    def post2(self, neirong):
        self.sendkeys(neirong, *self.post_page_input_neirong_loc)
        time.sleep(2)
        self.click(*self.post_page_button_fabiao_loc)
        time.sleep(2)