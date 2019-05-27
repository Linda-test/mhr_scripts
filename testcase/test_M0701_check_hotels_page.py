import unittest
from selenium import webdriver

from functions.common.log import logger
from functions.enter_global_tab import enter_nav
from functions.hotels_func import hotels_destinations_func
class MM(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.millenniumhotels.com")
        self.hotels_test = enter_nav(self.driver)
        self.hotels_check = hotels_destinations_func(self.driver)

    def test_Hotels(self):
        """测试hotels跳转"""
        try:
            self.hotels_test.enter_hotels_tab()
            self.hotels_check.All_region()
            self.hotels_check.Asia_region()
            self.hotels_check.Europe_region()
            self.hotels_check.MiddleEast_region()
            self.hotels_check.NewZealand_region()
            self.hotels_check.UniteStates_region()
            logger.info("Hotels page totally passed")
        except Exception as result:
            self.driver.get_screenshot_as_file("./screenshot/check_hotels_page_err.png")
            logger.info("%s unknown error during checking hotels page" % result)
            raise

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
