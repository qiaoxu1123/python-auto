from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

try:
    driver.get("http://127.0.0.1/upload/forum.php")
    window_list = driver.current_window_handle
    driver.switch_to.window(window_list)
    time.sleep(3)

    #driver.switch_to.frame('x-URS-iframe')

    name = driver.find_element_by_name('username')
    name.send_keys('admin')
    time.sleep(2)

    pwd = driver.find_element_by_name('password')
    pwd.send_keys('admin' + Keys.RETURN)
    time.sleep(2)

    in_m = driver.find_element_by_css_selector('#category_1 .fl_tb tbody tr td:nth-child(2) h2 a')
    in_m.click()
    time.sleep(2)

    title = driver.find_element_by_name('subject')
    title.send_keys('qiaoxu1')
    time.sleep(2)

    wz = driver.find_element_by_name('message')
    wz.send_keys('qiaoxuhaomei')
    time.sleep(2)

    fb = driver.find_element_by_id('fastpostsubmit')
    time.sleep(2)
    fb.click()

    hf = driver.find_element_by_id('post_reply')
    time.sleep(2)
    hf.click()

    hf1 = driver.find_element_by_id('postmessage')
    hf1.send_keys('duiduidui')
    time.sleep(2)

    ff = driver.find_element_by_id('postsubmit')
    time.sleep(2)
    ff.click()

    quit = driver.find_element_by_css_selector('#um p:nth-child(2) a:nth-child(18)')
    time.sleep(2)
    quit.click()

finally:
    driver.quit()