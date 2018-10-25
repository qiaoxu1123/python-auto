from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("http://www.yahoo.com/")
assert "Yahoo" in driver.title




elem = driver.find_element_by_name("p")
elem.send_keys('hhhhhhhhhh' + Keys.RETURN)
time.sleep(10)

driver.quit()


