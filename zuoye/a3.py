from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("http://baidu.com")
assert "百度" in driver.title

elem=driver.find_elements_by_tag_name("a")

for link in elem:
    print(link.get_attribute("href"))
    print(link.get_attribute("text"))

driver.quit()
