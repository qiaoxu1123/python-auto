from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

try:
    driver.get("http://127.0.0.1/upload/forum.php")
    window_list = driver.current_window_handle
    driver.switch_to.window(window_list)
    time.sleep(3)



    p_name = driver.find_element_by_name('username')
    p_name.send_keys('qiaoxu')
    time.sleep(2)

    p_pwd = driver.find_element_by_name('password')
    p_pwd.send_keys('haotest' + Keys.RETURN)
    time.sleep(2)

    dis = driver.find_element_by_css_selector('.fl_row td:nth-child(2) h2 a')
    time.sleep(2)
    dis.click()

    menu = driver.find_element_by_id('newspecial')
    hidden_submenu = driver.find_element_by_css_selector('.p_pop .poll a')
    time.sleep(2)

    ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

    sub = driver.find_element_by_name('subject')
    sub.send_keys('谁最美？')
    time.sleep(2)

    #driver.switch_to.frame('attachframe')
    a = driver.find_element_by_css_selector('#pollm_c_1 p:nth-child(1) .px.vm')
    a.send_keys('花花')
    time.sleep(2)

    b = driver.find_element_by_css_selector('#pollm_c_1 p:nth-child(2) .px.vm')
    b.send_keys('莉莉')
    time.sleep(2)

    c = driver.find_element_by_css_selector('#pollm_c_1 p:nth-child(3) .px.vm')
    c.send_keys('艳艳')
    time.sleep(2)

    look = driver.find_element_by_name('visibilitypoll')
    look.click()
    time.sleep(2)

    fq = driver.find_element_by_id('postsubmit')
    fq.click()
    time.sleep(2)

    xz = driver.find_element_by_id('option_3')
    xz.click()
    time.sleep(5)

    tj = driver.find_element_by_id('pollsubmit')
    tj.click()
    time.sleep(5)

    a1 = driver.find_element_by_css_selector('.pvt label')
    a2 = driver.find_element_by_css_selector('.pcht table tbody tr:nth-child(2) td:nth-child(2)')
    print("选项名称：",a1.text,"投票比例：",a2.text)

    b1 = driver.find_element_by_css_selector('.pcht table tbody tr:nth-child(3) .pvt label')
    b2 = driver.find_element_by_css_selector('.pcht table tbody tr:nth-child(4) td:nth-child(2)')
    print("选项名称：", b1.text, "投票比例：", b2.text)

    c1 = driver.find_element_by_css_selector('.pcht table tbody tr:nth-child(5) .pvt label')
    c2 = driver.find_element_by_css_selector('.pcht table tbody tr:nth-child(6) td:nth-child(2)')
    print("选项名称：", c1.text, "投票比例：", c2.text)

    bt = driver.find_element_by_id('thread_subject')
    print("主题名称：",bt.text)

    driver.close()
    driver.switch_to_window(window_list)

finally:
    driver.quit()