from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver.exe")

try:
    driver.implicitly_wait(5) #操作等待超时时间，10秒，默认等待  0.5miao
    driver.get("http://baidu.com")

    #激活当前窗口
    driver.switch_to.window(driver.current_window_handle)

    #控制台输出信息
    print("百度首页已打开：", driver.title)

    #搜索文本框   id=kw
    search_input = driver.find_element_by_id('kw')

    #找到后，键入 java 并提交搜索
    search_input.send_keys('java')
    search_input.submit()

    #获取页面zho“报读为您找到相关结果约”52,200,000个“ 相关文字的元素
    nums = driver.find_element_by_class_name('nums_text')

    #控制台打印信息
    print(nums.text)

    #再次激活窗口
    driver.switch_to.window(driver.current_window_handle)

    #执行脚本，显示一个框提示用户
    wait_seconds = 10
    #driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(nums.text.replace("\n","\t"),wait_seconds))
    driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(nums.text.replace("\n", "$"), wait_seconds))
    time.sleep(wait_seconds)
finally:
    driver.quit()



