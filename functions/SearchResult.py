from elements.ElementsDefine import bookingflow
from selenium import webdriver
from selenium.webdriver.common.by import By

class homepage(object):
    def __init__(self,driver):
        self.driver = driver

class Result_list(homepage):
    def check_hotel_name(self):
        pass

    def is_result_found(self):
        return "No result found." not in self.driver.page_source
