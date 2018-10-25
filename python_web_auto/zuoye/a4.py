from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver.maximize_window()
driver.implicitly_wait(6)
driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://www.hao123.com/")

elem1=driver.find_element_by_link_text("电视剧")
elem1.send_keys(Keys.RETURN)

# elem2=driver.find_element_by_partial_link_text("张勇夫妇")
# elem2.send_keys(Keys.RETURN)



