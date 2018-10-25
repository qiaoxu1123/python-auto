from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("./chromedriver.exe")
# driver.maximize_window()
# driver.implicitly_wait(6)

# try:
#     driver.get("http://bbs.tianya.cn/")
#     # window_list = driver.current_window_handle
#     # driver.switch_to.window(window_list)
#     time.sleep(3)
#
#     driver.execute_script(
#         "document.getElementById('bbs_left_nav').scrollTop=500")
#     time.sleep(3)
#
# finally:
#     driver.quit()
try:
    driver.get("http://www.python.org")
    window_list = driver.current_window_handle
    driver.switch_to.window(window_list)
    time.sleep(5)

    # menu = driver.find_element_by_css_selector(".navigation #downloads")
    # hidden_submenu = driver.find_element_by_css_selector(".navigation #downloads .tier-2:first-child")
    # time.sleep(5)

    menu = driver.find_element_by_link_text('Downloads')
    hidden_submenu = driver.find_element_by_link_text('All releases')

    ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

finally:
    time.sleep(5)
    driver.quit()