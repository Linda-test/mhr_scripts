import unittest
from selenium import webdriver

from functions.common.log import logger
from functions.enter_global_tab import enter_nav
from functions.venues_fun import meetings_events_func


class MM(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.millenniumhotels.com")
        self.venues_test = enter_nav(self.driver)
        self.venues_filter = meetings_events_func(self.driver)

    def test_Venues(self):
        """测试venues跳转"""
        try:
            self.venues_test.enter_venues_tab()
            self.venues_filter.filter_destination()
            self.venues_filter.filter_event_type()
            self.venues_filter.filter_attendees_type()
            logger.info("Veunues page totally passed")
        except Exception as result:
            self.driver.get_screenshot_as_file("./screenshot/check_venues_page_err.png")
            logger.info("%s unknown error during checking venues page" % result)
            raise

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
