import sys
sys.path.append('/project_baidu')
import unittest
from public.myunit import MyTest
from public import function
from public.base import Page
from test_case.page_obj.clock_in import clock
import time

class loginTest(MyTest, Page):
    def test_login1(self,expected = True):
        po = clock(self.driver)
        po.user_login()

    def test_login3(self, expected= True):
        po = clock(self.driver)
        po.user_login()
        self.take_screenshot('G:\\project_baidu\\report\image\\1.jpg')


if __name__ == "__main__":
    unittest.main()
