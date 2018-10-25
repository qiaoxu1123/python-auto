from pageobjects.base_view import BaseView
from selenium.webdriver.common.by import By

class PageRegister(BaseView):

    # 点击立即注册
    page_register_button_register_loc = (By.ID, 'com.tal.kaoyan:id/login_register_text')
    # 输入用户名
    page_register_input_username_loc = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    # 输入邮箱
    page_register_input_email_loc = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    # 输入密码
    page_register_input_password_loc = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
