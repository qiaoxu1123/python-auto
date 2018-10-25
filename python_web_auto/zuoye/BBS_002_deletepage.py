from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class DeletePage(BasePage):

    # 点击title前面的选项框
    delete_page_input_xuanze_loc = (By.CSS_SELECTOR, '.o input')
    # 删除按钮
    delete_page_a_delete_loc = (By.CSS_SELECTOR, '#mdly p strong')
    # 点击确定按钮
    detele_page_button_enter_loc = (By.ID, 'modsubmit')


    # 删帖部分
    def delete(self):
        self.click(*self.delete_page_input_xuanze_loc)
        time.sleep(2)
        self.click(*self.delete_page_a_delete_loc)
        time.sleep(2)
        self.click(*self.detele_page_button_enter_loc)

