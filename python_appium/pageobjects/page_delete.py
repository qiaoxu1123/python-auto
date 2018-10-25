from pageobjects.base_view import BaseView
from selenium.webdriver.common.by import By

class PageDelete(BaseView):

    # 长按
    page_delete_button_long_loc = (By.XPATH, '//android.widget.ListView/android.widget.RelativeLayout')
    # 点击删除
    page_delete_button_delete_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout')
    # 点击确定
    page_delete_button_enter_loc = (By.ID, 'android:id/button1')