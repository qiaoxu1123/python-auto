from selenium import webdriver
from configparser import ConfigParser
from framework.logger import Logger
import os.path

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_dirver_path = dir + '/tools/IEDriverServer.exe'

    def open_browser(self):
        config = ConfigParser()

        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Chrome(self.ie_driver_path)
            logger.info("Starting IE browser.")
        # elif browser == "Firefox":
        #     启动firefox
        #     logger.info("Starting Firefox browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implictily wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now Close and quit the browser.")
        self.driver.quit()