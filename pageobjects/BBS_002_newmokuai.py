from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class NewMoPage(BasePage):

    # 点击新建模块
    newmokuai_page_a_new_loc = (By.CSS_SELECTOR, '.fl_tb .fl_row:nth-child(2) td:nth-child(2) a')
    # 回帖
    newmokaui_page_button_replay_loc = (By.CSS_SELECTOR, '.pgs.mbm.cl #post_reply')
    # 回帖内容
    newmokaui_page_input_neirong_loc = (By.CSS_SELECTOR, '#postmessage')
    # 点击参与回复按钮
    newmokaui_page_button_enter_loc = (By.CSS_SELECTOR, '#postsubmit span')

    def newmokaui(self):
        self.click(*self.newmokuai_page_a_new_loc)
    def replay1(self, replay):
        self.click(*self.newmokaui_page_button_replay_loc)
        time.sleep(2)
        self.sendkeys(replay, *self.newmokaui_page_input_neirong_loc)
        time.sleep(2)
        self.click(*self.newmokaui_page_button_enter_loc)
        time.sleep(2)