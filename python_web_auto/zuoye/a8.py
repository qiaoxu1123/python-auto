from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(6)

try:
    driver.get("https://www.baidu.com/")
    window_list = driver.current_window_handle
    driver.switch_to.window(window_list)

    em=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'.mnav'))
    )
    em.click()
    print("当前页面是：",driver.title)

finally:
    time.sleep(5)
    driver.quit()