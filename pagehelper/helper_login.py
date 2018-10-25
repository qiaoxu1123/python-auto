from pageobjects.page_login import PageLogin
from pageobjects.base_view import BaseView
import time

class HelperLogin(BaseView):
    def helperlogin(self, username, password):

        ele_login = PageLogin(self.driver)

        self.sendkeys(username, *ele_login.page_login_input_username_loc)
        time.sleep(2)
        self.sendkeys(password, *ele_login.page_login_input_password_loc)
        time.sleep(2)
        self.click(*ele_login.page_login_button_search_loc)
        time.sleep(2)