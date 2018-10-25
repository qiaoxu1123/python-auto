# from selenium import webdriver
# import re
#
# driver = webdriver.Chrome("./chromedriver.exe")
# .
#
# try:
#     driver.get("http://home.baidu.com/home/index/contact_us")
#     print("百度首页已打开：", driver.title)
#
#     elem = driver.find_elements_by_class_name("mail-content-text")
#     for i in elem:
#       print(i.text)

    # doc=driver.page_source
    # emails = re.findall(r'[\w]+@[\w\.-]+',doc)
    # for i in emails:
    #    print(i)

# finally:
#    driver.quit()
#
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com")
elements = driver.find_elements_by_tag_name("a")

print('共找到a标签%d个'%len(elements))

for ele in elements:
    print(ele.text)

driver.quit()
