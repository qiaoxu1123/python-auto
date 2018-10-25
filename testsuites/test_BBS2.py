from testsuites.base_testcase import BaseTestCase
from pageobjects.BBS_001_homepage import HomePage
from pageobjects.BBS_001_morenpage import MoRenPage
from pageobjects.BBS_002_guanlipage import GuanLiPage
from pageobjects.BBS_002_newmokuai import NewMoPage
import unittest
import time


class BBS2Home(BaseTestCase):

    def test_bbs_fabiao(self):
        # 这里一定要test开头  那测试逻辑代码封装到一个test开头的方法里

        # (登陆)声明HomePage类对象
        home_page = HomePage(self.driver)
        home_page.open_url("http://127.0.0.1/upload/forum.php")

        # 调用首页搜索能
        home_page.login1("admin")
        home_page.login2("admin")

        # （默认板块)
        moren_page = HomePage(self.driver)
        moren_page.moren()

        # (删帖)
        delete_page = MoRenPage(self.driver)
        delete_page.delete()

        # 点击管理中心
        guanli_center = HomePage(self.driver)
        guanli_center.guanli()
        self.driver.switch_to.window(self.driver.window_handles[1])

        # 进入管理页面
        guanli_page1 = GuanLiPage(self.driver)
        guanli_page1.guanli1("admin")
        time.sleep(2)

        # 添加新板块
        guanli_page2 = GuanLiPage(self.driver)
        guanli_page2.guanli2('qiaoqiao')
        # self.driver.switch_to.frame('main')


        # 管理员退出
        self.driver.switch_to.window(self.driver.window_handles[0])
        quit1 = HomePage(self.driver)
        quit1.quit()
        time.sleep(2)

        # 普通用户登陆
        home_page1 = HomePage(self.driver)
        home_page1.login1("qiaoxu")
        home_page1.login2("haotest")
        time.sleep(2)

        # 点击Discuz
        discuz_page = HomePage(self.driver)
        discuz_page.discuz()
        time.sleep(2)

        # 点击新模块
        new_page = NewMoPage(self.driver)
        new_page.newmokaui()

        # 新模块里发帖
        post_page = MoRenPage(self.driver)
        post_page.post1("qiaoxu111")
        post_page.post2("nizhenhaonizhenhaonizhenhao")

        # 新模块里回帖
        replay_page = NewMoPage(self.driver)
        replay_page.replay1("duiduiduiduiduiduidui")
        time.sleep(3)

        # 普通用户退出
        quit_page = HomePage(self.driver)
        quit_page.quit2()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()