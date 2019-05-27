import unittest
from selenium import webdriver
import time


class Test_Register_M4B(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.millenniumhotels.com")

    def test_register(self):
        """测试M4B注册"""
        # self.enter_m4b_registerpage()
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        # self.driver.get("https://www.millenniumhotels.com")
        self.driver.find_element_by_xpath("//li[@class='item item-m4b']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='cookie-policy-close']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@id='hero-gradient']//following-sibling::div/div/div/div[2]/*[@class='m4b-homepage-hero-bar-link']").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()


