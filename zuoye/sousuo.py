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

    p_name = driver.find_element_by_name('username')
    p_name.send_keys('qiaoxu')
    time.sleep(2)

    p_pwd = driver.find_element_by_name('password')
    p_pwd.send_keys('haotest' + Keys.RETURN)
    time.sleep(2)

    sou = driver.find_element_by_id('scbar_txt')
    sou.send_keys('qiaoxu11' + Keys.RETURN)
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)

    # dian = driver.find_element_by_css_selector('ul .pbw strong font')
    # dian.click()
    # time.sleep(5)

    # driver.close()
    # driver.switch_to_window(window_list)
    #driver.switch_to.window(driver.window_handles[2])

    aa = driver.find_element_by_css_selector('.tl .sttl.mbn em span')
    if aa.text == 'qiaoxu11':
        print("结果: 找到 ", aa.text, "相关内容 6 个")
    else:
        print("未找到")

    driver.close()
    driver.switch_to_window(window_list)
    driver.switch_to.window(driver.window_handles[0])

    n_quit = driver.find_element_by_css_selector('#um p:nth-child(2) a:nth-child(12)')
    time.sleep(2)
    n_quit.click()

finally:
    driver.quit()