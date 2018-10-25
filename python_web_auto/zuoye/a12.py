from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
import time


driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(6)

try:
    driver.get("https://movie.douban.com/top250")

    window_list = driver.current_window_handle
    driver.switch_to.window(window_list)

    #while True:
    movies = driver.find_elements_by_css_selector('.article .grid_view li')
    length=movies.__len__()

    for movie in range(0,length):
        movie_link = driver.find_elements_by_css_selector('.article .grid_view li .hd a')

        link=movie_link[movie]
        link.click()



        movie_no = driver.find_element_by_css_selector('.top250-no')
        movie_name = driver.find_element_by_css_selector('#content h1 span:nth-child(1)')
        movie_type = driver.find_element_by_css_selector('#info > span:nth-child(8)')
        #movie_time = driver.find_element_by_css_selector('#info > span:nth-child(18)')
        movie_score = driver.find_element_by_css_selector('.rating_wrap .rating_num')

        print("排名：",movie_no.text,
                "影片名称：",movie_name.text,
                "类型：",movie_type.text,
                #"上映日期：",movie_time.text,
                "豆瓣评分：",movie_score.text)
        time.sleep(3)
        driver.back()
        driver.refresh()


        # content > div > div.article > ol > li:nth-child(1) > div > div.info > div.bd > p.quote > span


finally:
    time.sleep(10)
    driver.quit()