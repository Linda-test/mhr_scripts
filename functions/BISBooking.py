""" ================================================================================================================
@Description: This module defines the business functions about retail booking flow.Use these function and update if
              necessary.
@Last Update Date + Update by Whom: 5/7/2019 by TinaZ
====================================================================================================================="""

import time
from selenium import webdriver
from elements.ElementsDefine import ElementsDefine
from functions.common.log import logger


class BookingFlow(object):
    def __init__(self,driver):
        self.driver = driver
        self.element = ElementsDefine()

    def enter_booking_info_in_booking_widget(self, des_name):
        '''选择一个酒店，订房间'''
        try:
            self.driver.find_element(*self.element.destination).click()
            time.sleep(3)
            self.driver.find_element(*self.element.element_destination).send_keys(des_name)
            self.driver.find_element(*self.element.click_checkin).click()
            time.sleep(2)
            self.driver.find_element(*self.element.next_month).click()
            self.driver.find_element(*self.element.next_month).click()
            self.driver.find_element(*self.element.next_month).click()
            time.sleep(2)
            self.driver.find_element(*self.element.select_date).click()
            time.sleep(2)
            self.driver.find_element(*self.element.element_book).click()

        except Exception as result:
            self.driver.get_screenshot_as_file("../screenshot/ bookingpage.png")
            print("%s error happened" % result)

    def click_checkrr_city_bookflow_page(self):
        try:
            self.driver.find_element(*self.element.btn_checkrmsrts_citybfpage).click()
        except Exception as result:
            self.driver.get_screenshot_as_file("../screenshot/ bookingpage.png")
            print("%s error happened" % result)

    def click_check_hotel_bookflow_page(self):
        try:
            self.driver.find_element(*self.driver.btn_checkout_hotelbfpage).click()
            time.sleep(5)
        except Exception as result:
            self.driver.get_screenshot_as_file("../screenshot/ bookingpage.png")
            print("%s error happened" % result)

    def proceed_to_booking(self):
        pass

    def pay_with_creditcard(self):
        self.current_url = self.driver.current_url
        print(self.driver.title)
        # self.assertIn("Guest Information & Checkout", self.driver.title)
        try:
            self.driver.find_element(*self.driver.item_wallet_paymentpage).click()
            self.driver.find_element(*self.driver.txt_card_name).send_keys("test")
            self.driver.find_element(*self.driver.txt_card_num).send_keys("1111111111111111")
            self.driver.find_element(*self.driver.txt_card_code).send_keys("123")
            self.driver.find_element(*self.driver.txt_card_expiry_month).send_keys("01")
            self.driver.find_element(*self.driver.txt_card_expiry_year).send_keys("2020")

        except Exception as result:
            print("%s error happen during click wallet list" % result)



    def pay_with_3D_creditcard(self):
        pass

    def pay_with_paypal(self):
        pass

    def pay_with_ali(self):
        pass

    def pay_with_union(self):
        pass

    def enter_info_in_booking_widget(self):
        pass

    def check_info_in_bookingflow_page(self):
        pass


    def check_info_in_confirmation_page(self):
        pass

    def record_info_to_excel(self):
        pass

    def close_IG(self):
        pass

    def book_currentdate(self, des_name):
        self.driver.find_element(*self.element.destination).click()
        logger.info("click destination field")
        time.sleep(3)
        # des_name = 'London'
        self.driver.find_element(*self.element.destination).send_keys(des_name)
        logger.info("input destination name")
        time.sleep(2)
        self.driver.find_element(*self.element.city_select).click()
        logger.info("select the hotel/city in search result list")
        time.sleep(2)
        self.driver.find_element(*self.element.book_btn).click()
        logger.info("click the Book Now button")
        time.sleep(2)

    def check_city_page(self,des_name):
        try:
            assert u"Hotels in %s" % des_name in self.driver.title
            logger.info("City page redirected link is right")
        except Exception as e:
            logger.info("City page redirected link is wrong", format(e))
        self.driver.find_element(*self.element.explore_city).click()
        time.sleep(2)
        try:
            assert u"Hotels In London UK" in self.driver.title
            logger.info("Explore City page redirected link is right")
        except Exception as e:
            logger.info("Explore City page redirected link is wrong", format(e))










