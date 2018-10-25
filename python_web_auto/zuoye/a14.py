from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver.exe")
#driver.maximize_window()
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

    #删除
    # in_m = driver.find_element_by_css_selector('#category_1 .fl_tb tbody tr td:nth-child(2) h2 a')
    # in_m.click()
    # time.sleep(2)
    #
    # title = driver.find_element_by_css_selector('#normalthread_6 tr th a:nth-child(2)')
    # title.click()
    # time.sleep(2)
    #
    # delete = driver.find_element_by_css_selector('.wp .xi2 a')
    # delete.click()
    # time.sleep(2)
    #
    # yes = driver.find_element_by_id('modsubmit')
    # yes.click()
    # time.sleep(2)

    guanli = driver.find_element_by_css_selector('#um p:nth-child(2) a:nth-child(16)')
    guanli.click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[1])

    ap = driver.find_element_by_name('admin_password')
    ap.send_keys('admin' + Keys.RETURN)
    time.sleep(2)

    luntan = driver.find_element_by_id('header_forum')
    luntan.click()
    time.sleep(2)

    driver.switch_to.frame('main')
    bank = driver.find_element_by_css_selector('.lastboard a')
    bank.click()
    time.sleep(2)

    c = driver.find_element_by_css_selector('.tb tbody:nth-child(3) td:nth-child(3) .txt')
    c.clear()
    c.send_keys('qiaoqiaoqiao')
    time.sleep(2)

    btn = driver.find_element_by_css_selector('.fixsel .btn')
    btn.click()
    time.sleep(2)

    driver.close()
    driver.switch_to_window(window_list)

    quit = driver.find_element_by_css_selector('#um p:nth-child(2) a:nth-child(18)')
    time.sleep(2)
    quit.click()

    #driver.switch_to.window(driver.window_handles[0])

    p_name = driver.find_element_by_name('username')
    p_name.send_keys('qiaoxu')
    time.sleep(2)

    p_pwd = driver.find_element_by_name('password')
    p_pwd.send_keys('haotest' + Keys.RETURN)
    time.sleep(2)

    dis = driver.find_element_by_css_selector('.fl_row td:nth-child(2) h2 a')
    time.sleep(2)
    dis.click()

    n_title = driver.find_element_by_name('subject')
    n_title.send_keys('qiaoxu11')
    time.sleep(2)

    n_wz = driver.find_element_by_name('message')
    n_wz.send_keys('qiaoxuhaomei')
    time.sleep(2)

    n_fb = driver.find_element_by_id('fastpostsubmit')
    time.sleep(2)
    n_fb.click()

    n_hf = driver.find_element_by_id('post_reply')
    time.sleep(2)
    n_hf.click()

    n_hf1 = driver.find_element_by_id('postmessage')
    n_hf1.send_keys('duiduiduiduiduiduiduiduiduiduiduiduidui')
    time.sleep(2)

    n_ff = driver.find_element_by_id('postsubmit')
    time.sleep(2)
    n_ff.click()

    n_quit = driver.find_element_by_css_selector('#um > p:nth-child(2) > a:nth-child(12)')
    time.sleep(2)
    n_quit.click()

finally:
    driver.quit()