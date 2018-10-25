from pageobjects.page_delete import PageDelete
from pageobjects.base_view import BaseView
import time

class HelperDelete(BaseView):

    def helperdelete(self):

        ele_delete= PageDelete(self.driver)

        self.long_press(*ele_delete.page_delete_button_long_loc)
        time.sleep(2)
        self.click(*ele_delete.page_delete_button_delete_loc)
        time.sleep(2)
        self.click(*ele_delete.page_delete_button_enter_loc)
        time.sleep(2)