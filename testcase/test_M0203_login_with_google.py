import unittest
from functions.BISAccount import Account
from driver.browser import chrome_browser
from ddt import ddt,data
from functions.common.Common import Common
from functions.common.ExcelUtil_tool import ExcelUtil
from functions.common.log import logger
logindata = ExcelUtil.readExcel('C:\\MLP\\Automation\\Project\data\\acc&env_info.xlsx','Sheet1')
# logindata = ExcelUtil.readExcel('../data/acc&env_info.xlsx','Sheet1')

@ddt
class GoogleLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_browser()
        self.account = Account(self.driver)
        self.common = Common(self.driver)
        self.common.open_browser()

    @data(*logindata)
    def test_login_google(self,data):
        """测试google登录"""
        try:
            self.account.login_with_google(data['google_acc'],data['google_pw'])
            logger.info("Result Success Rate Is 100%")
        except Exception as result:
            self.driver.get_screenshot_as_file("./screenshot/google_err.png")
            logger.info("%s unknown error during login with google" % result)
            raise

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()
#
