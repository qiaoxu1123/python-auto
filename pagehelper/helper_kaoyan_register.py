from pageobjects.page_kaoyan_register import PageRegister
from pageobjects.base_view import BaseView
import time

class HelperRegister(BaseView):

    def helperregister(self, username, email, password):

        ele_register= PageRegister(self.driver)

        self.click(*ele_register.page_register_button_register_loc)
        time.sleep(2)
        self.sendkeys(username, *ele_register.page_register_input_username_loc)
        time.sleep(2)
        self.sendkeys(email, *ele_register.page_register_input_email_loc)
        time.sleep(2)
        self.sendkeys(password, *ele_register.page_register_input_password_loc)
        time.sleep(2)