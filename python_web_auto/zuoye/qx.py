from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("http://www.python.org")
assert "Python" in driver.title