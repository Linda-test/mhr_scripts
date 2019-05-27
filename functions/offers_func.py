import time
from elements.ElementsDefine import ElementsDefine
from functions.common.log import logger


class explore_offers_func(object):

    def __init__(self, driver):
        self.driver = driver
        self.element = ElementsDefine()

    def click_explore(self):
        self.driver.find_element(*self.element.explore_offers).click()
        try:
            assert u"Asia Hotels Special Offers" in self.driver.title
            logger.info("Explore offers is right")
        except Exception as e:
            logger.info("Explore offers is wrong",format(e))

    def filter_offers(self):
        self.driver.find_element(*self.element.offer_type).click()
        time.sleep(3)
        self.driver.find_element(*self.element.type_select).click()
        time.sleep(2)
        offer_type_text = self.driver.find_element(*self.element.offer_type_txt).text
        logger.info(offer_type_text)
        assert offer_type_text == 'PAY NOW AND SAVE'

    def book_offer(self):
        self.driver.find_element(*self.element.booknow_offer_btn).click()
        time.sleep(2)
        offer_book_btn = self.driver.find_element(*self.element.offer_book).text
        logger.info(offer_book_btn)
        assert offer_book_btn == 'BOOK'
