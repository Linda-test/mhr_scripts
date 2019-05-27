import unittest
from selenium import webdriver
from functions.BISBooking import BookingFlow
from functions.common.log import logger


class MM(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.millenniumhotels.com")
        self.city_test = BookingFlow(self.driver)

    def test_City(self):
        """测试city page"""
        des_name = 'London'
        try:
            self.city_test.book_currentdate(des_name)
            self.city_test.check_city_page(des_name)
            logger.info("Result Success Rate Is 100%")
        except Exception as result:
            self.driver.get_screenshot_as_file("./screenshot/check_city_page_err.png")
            logger.info("%s unknown error during checking city page" % result)
            raise

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
