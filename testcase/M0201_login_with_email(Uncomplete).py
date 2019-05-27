import time
import unittest
from functions.BISPages import Pages
from driver.browser import chrome_browser
from ddt import ddt,data
from functions.common.ExcelUtil_tool import ExcelUtil
# import json
# import requests

regions = ['Asia','Europe','MEA','New+Zealand','United+States']
hotels = []
logindata = ExcelUtil.readExcel('../data/acc&env_info.xlsx','Sheet1')

@ddt
class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = chrome_browser()
        self.driver.get("https://www.millenniumhotels.com")
        self.home = Pages(self.driver)

    def tearDown(self):
        self.driver.close()

    @data(*logindata)
    def test_login_email(self,data):
        """linkedin登录"""
        try:
            self.home.login_with_email(data['link_acc'],data['link_pass'])
            self.current_url = self.driver.current_url
            self.assertEqual(self.current_url,"https://www.millenniumhotels.com/","跳转失败")

        except Exception as err:
            self.driver.get_screenshot_as_file("./screenshot/email_err.png")
            raise

    if __name__ == '__main__':
        unittest.main()
#
