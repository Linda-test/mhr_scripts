""" ================================================================================================================
@Description: This module defines the business functions about create and login.Use these function and update if
              necessary.
@Last Update Date + Update by Whom: 5/25/2019 by TinaZ
====================================================================================================================="""

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.ElementsDefine import ElementsDefine


class Pages(object):
    def __init__(self, driver):      # Initial for the elements
        self.driver = driver
        self.element = ElementsDefine()

    """-----------------------------------------------------------
    Description:  A series of function about homepage
    Author: Yan Liu
    Date: 
    Update By:
    Update Date：
    -------------------------------------------------------------"""
    def click_swictch_language(self):
        """点击语言"""
        self.driver.find_elements(*self.element.element_switch_language)[1].click()

    def switch_to_chinese(self):
        """点击简体中文"""
        self.driver.find_element(*self.element.element_select_chinese_simple).click()
        sleep(3)
        destination = self.driver.find_element(*self.element.element_destination).text
        assert destination == "特色目的地"

    def switch_to_emglish(self):
        """点击英语"""
        self.driver.find_element(*self.element.element_select_english).click()
        sleep(3)
        destination = self.driver.find_element(*self.element.element_destination).text
        assert destination == "FEATURED LOCATIONS"

    def switch_to_Arabic(self):
        """点击阿拉伯语"""
        self.driver.find_element(*self.element.element_select_arabic).click()
        sleep(3)
        destination = self.driver.find_element(*self.element.element_destination).text
        assert destination == "مواقع مميزة"

    def switch_to_spanish(self):
        """点击西班牙语"""
        self.driver.find_element(*self.element.element_select_spanish).click()
        sleep(3)
        destination = self.driver.find_element(*self.element.element_destination).text
        print(destination)
        assert destination == "DESTINOS DESTACADOS"

    def switch_to_franch(self):
        """点击法语"""
        self.driver.find_element(*self.element.element_select_franch).click()
        sleep(3)
        destination = self.driver.find_element(*self.element.element_destination).text
        assert destination == "LIEUX PRÉSENTÉS"

    def switch_to_litalian(self):
        """点击意大利语"""
        self.driver.find_element(*self.element.element_select_italian).click()
        sleep(3)
        destination = self.driver.find_element(*self.element.element_destination).text
        assert destination == "LOCALITÀ IN PRIMO PIANO"

    def switch_to_chinese_traditional(self):
        """点击繁体中文"""
        self.driver.find_element(*self.element.element_select_chinese_traditional).click()
        sleep(3)
        destination = self.driver.find_element(*self.element.element_destination).text
        assert destination == "精選城市"

    def switch_to_japanese(self):
        """点击日语"""
        self.driver.find_element(*self.element.element_select_japanese).click()
        sleep(3)
        destination = self.driver.find_element(*self.element.element_destination).text
        assert destination == "注目のロケーション"


    """ ------------------------------------------------------------------------
    Description:  A series of function about property page
    Author: Tina Zhao
    Date: 
    Update By:
    Update Date:
    ----------------------------------------------------------------------------"""

    def proceed_to_property_page(self):

        # 1.Find ‘Hotels’ link then click
        self.driver.find_element(*self.element.link_hotels_xpath).click()
        print('-' * 20 + self.driver.title + '-' * 20)

        is_homepage_opened = "Millennium Hotels and Resorts" in self.driver.title
        # assert is_homepage_opened

        if is_homepage_opened is True:
            print('Home page property page is opened')
        else:
            print('Failed open home page')

        # 2.Find specific hotel name then click
        self.driver.find_element(*self.element.link_hotel_name_xpath).click()

        print('-' * 20 + self.driver.title + '-' * 20)
        is_hotelpage_opened = "Grand Copthorne Waterfront" in self.driver.title
        # assert is_hotelpage_opened

        if is_hotelpage_opened is True:
            print('Hotel property page is opened')
        else:
            print('Failed open hotel property page')


    def check_rooms_section(self):
        self.driver.find_element_by_link_text(self.element.link_room_section_text).click()


    def check_other_section(self):
        self.driver.find_element_by_link_text(self.element.link_room_section_text).click()
