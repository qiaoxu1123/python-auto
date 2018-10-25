from testsuites.base_testcase import BaseTestCase
from pageobjects.BBS_001_homepage import HomePage
from pageobjects.BBS_001_morenpage import MoRenPage
from pageobjects.BBS_004_toupiaopage import TouPiao
from pageobjects.BBS_002_newmokuai import NewMoPage

import time

class BBS4Home(BaseTestCase):

    def test_bbs_toupiao(self):
        # 这里一定要test开头  那测试逻辑代码封装到一个test开头的方法里

        # (登陆)声明HomePage类对象
        home_page2 = HomePage(self.driver)
        home_page2.open_url("http://127.0.0.1/upload/forum.php")

        # 调用首页搜索能
        home_page2.login1("qiaoxu")
        home_page2.login2("haotest")

        # 进入默认板块
        moren_page = HomePage(self.driver)
        moren_page.moren()

        # 点击发帖
        moren_page1 = MoRenPage(self.driver)
        moren_page1.toupiaopage()

        # 发起投票
        toupiao_page1 = TouPiao(self.driver)
        toupiao_page1.toupiaopage1("谁最美？", "刘亦菲", "范冰冰", "谢娜")

        toupiao_page2 = TouPiao(self.driver)
        toupiao_page2.toupiaopage2()

        toupiao_page3 = TouPiao(self.driver)
        toupiao_page3.toupiaopage3()

        # 退出
        quit_page = HomePage(self.driver)
        quit_page.quit2()
        self.driver.close()