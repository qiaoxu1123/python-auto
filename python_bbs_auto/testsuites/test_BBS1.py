from testsuites.base_testcase import BaseTestCase
from pageobjects.BBS_001_homepage import HomePage
from pageobjects.BBS_001_morenpage  import MoRenPage
import unittest
import time


class BBS1Home(BaseTestCase):

    def test_bbs_login(self):
        # 这里一定要test开头  那测试逻辑代码封装到一个test开头的方法里

        # (登陆)声明HomePage类对象
        home_page = HomePage(self.driver)
        home_page.open_url("http://127.0.0.1/upload/forum.php")
        # a = BasePage(self.driver)
        # a.activate()

        # 调用首页搜索能（登陆）
        home_page.login1("admin")
        home_page.login2("admin")

        # (默认板块)
        moren_page = HomePage(self.driver)
        moren_page.moren()

        # (发帖)
        post_page = MoRenPage(self.driver)
        post_page.post1("qiaoxu123")
        post_page.post2("nizhenhao")

        # (回帖)
        replay_page = MoRenPage(self.driver)
        replay_page.replay("duiduiduiduiduiduidui")
        time.sleep(3)
        # self.driver.close()

        # （退出）
        quit_page = HomePage(self.driver)
        time.sleep(2)
        quit_page.quit()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()