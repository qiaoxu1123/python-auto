from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class MoRenPage(BasePage):

    # 发帖部分

    # 帖子标题
    post_page_input_title_loc = (By.NAME, 'subject')
    # 帖子内容
    post_page_input_neirong_loc = (By.ID, 'fastpostmessage')
    # 点击发表帖子
    post_page_button_fabiao_loc = (By.CSS_SELECTOR, '#fastpostsubmit strong')

    def post1(self, title):
        self.sendkeys(title, *self.post_page_input_title_loc)
        time.sleep(2)

    def post2(self, neirong):
        self.sendkeys(neirong, *self.post_page_input_neirong_loc)
        time.sleep(2)
        self.click(*self.post_page_button_fabiao_loc)
        time.sleep(2)

    # 回帖部分

    # 点击回复按钮
    replay_page_button_replay_loc = (By.CSS_SELECTOR, '.wp.cl .pgs.mbm.cl.pbm.bbs #post_reply')
    # 输入回复内容
    replay_page_input_message_loc = (By.CSS_SELECTOR, '.area #postmessage')
    # 点击参与/回复 按钮
    replay_page_button_submit_loc = (By.ID, 'postsubmit')
    # # 点击退出
    replay_page_button_quit_loc = (By.CSS_SELECTOR, '#um p:nth-child(2) a:nth-child(18)')

    def replay(self, replay):
        self.click(*self.replay_page_button_replay_loc)
        time.sleep(2)
        self.sendkeys(replay, *self.replay_page_input_message_loc)
        time.sleep(2)
        self.click(*self.replay_page_button_submit_loc)
        time.sleep(2)
        self.click(*self.replay_page_button_quit_loc)
        time.sleep(2)

    # 删帖部分

    # 点击title前面的选项框
    delete_page_input_xuanze_loc = (By.CSS_SELECTOR, '.o input')
    # 删除按钮
    delete_page_a_delete_loc = (By.CSS_SELECTOR, '#mdly p strong')
    # 点击确定按钮
    detele_page_button_enter_loc = (By.ID, 'modsubmit')

    def delete(self):
        self.click(*self.delete_page_input_xuanze_loc)
        time.sleep(2)
        self.click(*self.delete_page_a_delete_loc)
        time.sleep(2)
        self.click(*self.detele_page_button_enter_loc)

    # 点击发帖
    toupiao_page_button_toupiao_loc = (By.CSS_SELECTOR, '#newspecial')
    # 发起投票
    toupiao_page_a_faqi_loc = (By.CSS_SELECTOR, '#editorbox ul li:nth-child(2) a')

    def toupiaopage(self):
        self.click(*self.toupiao_page_button_toupiao_loc)
        time.sleep(2)
        self.click(*self.toupiao_page_a_faqi_loc)


