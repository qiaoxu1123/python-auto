from pageobjects.page_add import PageAdd
from pageobjects.base_view import BaseView
import time

class HelperAdd(BaseView):

    def helperadd(self, content):

        ele_add = PageAdd(self.driver)

        self.click(*ele_add.page_add_button_plus_loc)
        time.sleep(2)
        self.sendkeys(content, *ele_add.page_add_input_content_loc)
        time.sleep(2)
        self.click(*ele_add.page_add_button_search_loc)
        time.sleep(2)