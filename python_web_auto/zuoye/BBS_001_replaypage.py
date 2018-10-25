from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class ReplayPage(BasePage):

    # 点击回复按钮
    replay_page_button_replay_loc = (By.CSS_SELECTOR, '.wp.cl .pgs.mbm.cl.pbm.bbs #post_reply')
    # 输入回复内容
    replay_page_input_message_loc = (By.CSS_SELECTOR, '.area #postmessage')
    # 点击参与/回复 按钮
    replay_page_button_submit_loc = (By.ID, 'postsubmit')
    # # 点击退出
    replay_page_button_quit_loc = (By.CSS_SELECTOR, '#um p:nth-child(2) a:nth-child(18)')


    # 输入搜索内容并提交
    # 回帖部分
    def replay(self, replay):
        self.click(*self.replay_page_button_replay_loc)
        time.sleep(2)
        self.sendkeys(replay, *self.replay_page_input_message_loc)
        time.sleep(2)
        self.click(*self.replay_page_button_submit_loc)
        time.sleep(2)
        self.click(*self.replay_page_button_quit_loc)
