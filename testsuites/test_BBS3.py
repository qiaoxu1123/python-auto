from testsuites.base_testcase import BaseTestCase
from pageobjects.BBS_001_homepage import HomePage
from pageobjects.BBS_003_sousuopage import SouSuo

import time

class BBS3Home(BaseTestCase):

    def test_bbs_sousuo(self):
        # 这里一定要test开头  那测试逻辑代码封装到一个test开头的方法里

        # (登陆)声明HomePage类对象
        home_page2 = HomePage(self.driver)
        home_page2.open_url("http://127.0.0.1/upload/forum.php")

        # 调用首页搜索能
        home_page2.login1("qiaoxu")
        home_page2.login2("haotest")

        # 搜索haotest
        sousuo_page = HomePage(self.driver)
        sousuo_page.sousuo("qiaoxu111")

        # 切换到搜索页面
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        yanzheng1_page = SouSuo(self.driver)
        yanzheng1_page.yanzheng1()
        time.sleep(2)

        # 验证信息
        self.driver.switch_to.window(self.driver.window_handles[2])
        yanzheng_page = SouSuo(self.driver)
        yanzheng_page.yanzheng2()

        # 退出
        quit = SouSuo(self.driver)
        quit.quit()
        self.driver.close()

