import unittest
from selenium import webdriver
from functions.MyMillennium_fun import My_Millenium_func
from functions.common.log import logger
from functions.enter_global_tab import enter_nav

class MM(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.millenniumhotels.com")
        self.mm_test = enter_nav(driver=self.driver)
        self.mm_sublink_test = My_Millenium_func(driver=self.driver)

    def test_MyMillennium(self):
        """测试my millennium跳转"""
        try:
            self.mm_test.enter_mm_tab()
            self.mm_sublink_test.click_SLAM()
            self.mm_sublink_test.click_PH()
            self.mm_sublink_test.click_FAQ()
            self.mm_sublink_test.click_TAC()
            logger.info("My Millenium page totally passed")
        except Exception as result:
            self.driver.get_screenshot_as_file("./screenshot/check_mm_page_err.png")
            logger.info("%s unknown error during checking mm page" % result)
            raise

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
