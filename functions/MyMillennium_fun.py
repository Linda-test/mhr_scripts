from elements.ElementsDefine import ElementsDefine
from functions.common.log import logger


class My_Millenium_func(object):

    def __init__(self, driver):
        self.driver = driver
        self.element = ElementsDefine()

    def click_MM(self):
        self.driver.find_element(*self.element.My_Millennium_link).click()

    def click_SLAM(self):
        self.driver.find_element(*self.element.Stay_Like_A_Millionaire_link).click()
        try:
            assert u"Stay Like" in self.driver.title
            logger.info("Stay Like redirected link is right")
        except Exception as e:
            logger.info("Stay Like redirected link is wrong",format(e))

    def click_PH(self):
        self.driver.find_element(*self.element.Participating_Hotels_link).click()
        try:
            assert u"Participating Hotels" in self.driver.title
            logger.info("Participating Hotels redirected link is right")
        except Exception as e:
            logger.info("Participating Hotels redirected link is wrong",format(e))

    def click_FAQ(self):
        self.driver.find_element(*self.element.Frequently_Asked_Questions_link).click()
        try:
            assert u"Frequently Asked Questions" in self.driver.title
            logger.info("Frequently Asked Questions redirected link is right")
        except Exception as e:
            logger.info("Frequently Asked Questions redirected link is wrong",format(e))

    def click_TAC(self):
        self.driver.find_element(*self.element.Terms_and_Conditions_link).click()
        try:
            assert u"Terms and Conditions" in self.driver.title
            logger.info("Terms and Conditions redirected link is right")
        except Exception as e:
            logger.info("Terms and Conditions redirected link is wrong",format(e))


