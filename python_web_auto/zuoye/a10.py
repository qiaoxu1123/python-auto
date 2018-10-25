from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(6)

try:
    driver.get("https://www.baidu.com/")
    window_list = driver.current_window_handle
    driver.switch_to.window(window_list)
    time.sleep(3)

    driver.execute_script("window.alert('这是一个弹出框!')")
    time.sleep(3)

    driver.switch_to.alert.accept()
    time.sleep(3)
    driver.switch_to.alert.dismiss()
    time.sleep(3)

finally:
    driver.quit()
