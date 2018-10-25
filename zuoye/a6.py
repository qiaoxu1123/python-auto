from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(6)

try:
    driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")

    window_list = driver.current_window_handle
    driver.switch_to.window(window_list)

    while True:
        jobs = driver.find_elements_by_css_selector('.item_con_list li')
    #job_link = driver.find_element_by_css_selector('.item_con_list li:first-child .p_top a span')

        for job in jobs:
            job_link = job.find_element_by_css_selector('.p_top a span')
            job_link.click()

            driver.switch_to_window(driver.window_handles[1])

            job_company = driver.find_element_by_css_selector('.company')
            job_name = driver.find_element_by_css_selector('.name')
            job_salary = driver.find_element_by_css_selector('.salary')
            job_request = driver.find_element_by_css_selector('.job_request span:nth-child(3)')

            print("公司：",job_company.text,
                  "职位：",job_name.text,
                  "工资范围：",job_salary.text,
                  "工作经验：",job_request.text)
            driver.close()
            driver.switch_to_window(window_list)

        next_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.item_con_pager .pager_container a:last-child'))
        )
        next_page_class = next_page.get_attribute('class')

        if 'page_next_disabled' in next_page_class:
            break
        else:
            next_page.click()
            time.sleep(3)

finally:
    time.sleep(10)
    driver.quit()

    ##content > div > div.article > div.paginator > span.next > a

    # next_page = WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div > div.article > div.paginator > span.next > a'))
    # )
    # next_page_class = next_page.get_attribute('class')
    #
    # if 'page_next_disabled' in next_page_class:
    #     break
    # else:
    #     next_page.click()
    #     time.sleep(3)

    # page = driver.find_element_by_css_selector('.next')
    # a = driver.find_element_by_css_selector('.next a')
    # b = a.get_attribute('href')
    # print(b)
    # c = driver.page_source
    # if b in c:
    #     break
    # else:
    #     page.click()
    #     time.sleep(3)
