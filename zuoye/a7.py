from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(6)

try:
    driver.get("https://mail.163.com/")
    window_list = driver.current_window_handle
    driver.switch_to.window(window_list)
    time.sleep(3)

    driver.switch_to.frame('x-URS-iframe')

    elem = driver.find_element_by_name('email')
    elem.send_keys('hhhhhhhhhh')
    time.sleep(5)

    elem = driver.find_element_by_name('password')
    elem.send_keys('hhhhhhhhhh' + Keys.RETURN)
    time.sleep(5)

finally:
    driver.quit()
