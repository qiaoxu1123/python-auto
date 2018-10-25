from testsuites.base_testcase import BaseTestCase
from pagehelper.helper_login import HelperLogin
from pagehelper.helper_delete import HelperDelete
import unittest

class Delete(BaseTestCase):

    def test_delete(self):
        # 这里一定要test开头  那测试逻辑代码封装到一个test开头的方法里

        page_login = HelperLogin(self.driver)
        page_login.helperlogin('1', '1')

        page_delete = HelperDelete(self.driver)
        page_delete.helperdelete()

if __name__=='__main__':
    unittest.main()