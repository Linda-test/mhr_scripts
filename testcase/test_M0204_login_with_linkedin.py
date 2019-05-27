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
class LinkedInLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_browser()
        self.account = Account(self.driver)
        self.common = Common(self.driver)
        self.common.open_browser()

    @data(*logindata)
    def test_login_linkedin(self,data):
        """测试linkedin登录"""
        try:
            self.account.login_with_linkedin(data['linkedin_acc'],data['linkedin_pw'])
            logger.info("Result Success Rate Is 100%")
        except Exception as result:
            self.driver.get_screenshot_as_file("./screenshot/linkedin_err.png")
            logger.info("%s unknown error during login with linkedin" % result)
            raise

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
#
