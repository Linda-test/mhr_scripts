
from elements.ElementsDefine import ElementsDefine
from functions.common.log import logger


class enter_nav(object):

    def __init__(self,driver):
        self.driver = driver
        self.element = ElementsDefine()

    def enter_mm_tab(self):
        self.driver.find_element(*self.element.Mymillennium_tab).click()
        try:
            assert u"My Millennium" in self.driver.title
            logger.info("My Millennium redirected link is right")
        except Exception as e:
            logger.info("My Millennium redirected link is wrong",format(e))

    def enter_hotels_tab(self):
        self.driver.find_element(*self.element.Hotels_tab).click()
        try:
            assert u"Hotels" in self.driver.title
            logger.info("Hotels redirected link is right")
        except Exception as e:
            logger.info("Hotels redirected link is wrong",format(e))

    def enter_venues_tab(self):
        self.driver.find_element(*self.element.Venues_tab).click()
        try:
            assert u"Meetings & Events" in self.driver.title
            logger.info("Venues redirected link is right")
        except Exception as e:
            logger.info("Venues redirected link is wrong",format(e))


    def enter_offers_tab(self):
        self.driver.find_element(*self.element.Offers_tab).click()
        try:
            assert u"Offers" in self.driver.title
            logger.info("Offers redirected link is right")
        except Exception as e:
            logger.info("Offers redirected link is wrong",format(e))





