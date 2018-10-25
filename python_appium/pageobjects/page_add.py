from pageobjects.base_view import BaseView
from selenium.webdriver.common.by import By
# import time

class PageAdd(BaseView):

    # 点击加号
    page_add_button_plus_loc = (By.ID, 'com.example.todolist:id/action_new')
    # 输入待办事项内容
    page_add_input_content_loc = (By.ID, 'com.example.todolist:id/toDoItemDetailET')
    # 点击保存按钮
    page_add_button_search_loc = (By.ID, 'com.example.todolist:id/saveBtn')