from pageobjects.base_view import BaseView
from selenium.webdriver.common.by import By
# import time

class PageLogin(BaseView):

    # 用户名/密码
    page_login_input_username_loc = (By.ID, 'com.example.todolist:id/nameET')
    page_login_input_password_loc = (By.XPATH, '//android.widget.EditText[2]')
    # 点击登陆按钮
    page_login_button_search_loc = (By.ID, 'com.example.todolist:id/loginBtn')

    # def pagelogin(self, username, password):
    #
    #     self.sendkeys(username, *self.page_login_input_username_loc)
    #     time.sleep(2)
    #     self.sendkeys(password, *self.page_login_input_password_loc)
    #     time.sleep(2)
    #     self.click(*self.page_login_button_search_loc)
    #     time.sleep(2)