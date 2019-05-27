import unittest
from selenium import webdriver

from functions.common.log import logger
from functions.enter_global_tab import enter_nav
from functions.offers_func import explore_offers_func

class MM(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.millenniumhotels.com")
        self.offers_test = enter_nav(self.driver)
        self.explore_offer_test = explore_offers_func(self.driver)

    def test_Offers(self):
        """测试offers跳转"""
        try:
            self.offers_test.enter_offers_tab()
            self.explore_offer_test.click_explore()
            self.explore_offer_test.filter_offers()
            self.explore_offer_test.book_offer()
            logger.info("Offers page totally passed")
        except Exception as result:
            self.driver.get_screenshot_as_file("./screenshot/check_offers_page_err.png")
            logger.info("%s unknown error during checking offers page" % result)
            raise

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
