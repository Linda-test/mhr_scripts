from selenium import webdriver
from time import sleep

class Start_test(object):

    def launch_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url("https://www.millenniumhotels.com")
