import unittest
from functions.BISProfile import Profile
from functions.BISAccount import Account
from driver.browser import chrome_browser
from functions.common import log
from functions.common.Common import Common
from functions.common.ExcelUtil_tool import ExcelUtil
from ddt import ddt,data
logger = log.createlogger("MAIN")
logindata = ExcelUtil.readExcel('C:\\MLP\\Automation\\Project\data\\acc&env_info.xlsx','Sheet1')
# logindata = ExcelUtil.readExcel('../data/acc&env_info.xlsx','Sheet1')
@ddt
class ProfileTest(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_browser()
        self.account = Account(self.driver)
        self.profile = Profile(self.driver)
        self.common = Common(self.driver)
        self.common.open_browser()

    @data(*logindata)
    def test_MyLifestyle(self,data):
        """测试profile-my life style界面的检查"""
        try:
            self.account.login_with_facebook(data['face_email'], data['face_pw'])
            self.profile.enter_profile()
            self.profile.enter_my_lifestyle()
            self.profile.my_stay_preference()
            self.profile.my_favourite_destination()
            self.profile.my_interests()
            logger.info("Result Success Rate Is 100%")
        except Exception as result:
            self.driver.get_screenshot_as_file("./screenshot/check_hotels_page_err.png")
            logger.info("%s unknown error during checking profile-my lifestyle page" % result)
            raise

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

