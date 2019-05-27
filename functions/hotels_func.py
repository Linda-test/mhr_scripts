import time
from elements.ElementsDefine import ElementsDefine
from functions.common.log import logger


class hotels_destinations_func(object):

    def __init__(self, driver):
        self.element = ElementsDefine()
        self.driver = driver

    def All_region(self):
        try:
            self.driver.find_element(*self.element.All_region).click()
            time.sleep(2)
            self.driver.find_element(*self.element.last_All_hotels).click()
            time.sleep(2)
            logger.info(self.driver.current_url)
            self.driver.back()
            js = "var action=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
            time.sleep(3)
            return True
        except:
            logger.info("can't display all region")
            return False

    def Asia_region(self):
        try:
            self.driver.find_element(*self.element.Asia_region).click()
            time.sleep(2)
            self.driver.find_element(*self.element.last_Asia_hotels).click()
            time.sleep(2)
            logger.info(self.driver.current_url)
            self.driver.back()
            js = "var action=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
            time.sleep(2)
            return True
        except:
            logger.info("can't display Asia region")
            return False

    def Europe_region(self):
        try:
            self.driver.find_element(*self.element.Europe_region).click()
            time.sleep(2)
            self.driver.find_element(*self.element.last_Europe_hotels).click()
            time.sleep(2)
            logger.info(self.driver.current_url)
            self.driver.back()
            js = "var action=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
            time.sleep(2)
            return True
        except:
            logger.info("can't display Europe region")
            return False

    def MiddleEast_region(self):
        try:
            self.driver.find_element(*self.element.MiddleEast_region).click()
            time.sleep(2)
            self.driver.find_element(*self.element.last_MiddleEast_hotels).click()
            time.sleep(2)
            logger.info(self.driver.current_url)
            self.driver.back()
            js = "var action=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
            time.sleep(2)
            return True
        except:
            logger.info("can't display Middle East region")
            return False

    def NewZealand_region(self):
        try:
            self.driver.find_element(*self.element.NewZealand_region).click()
            time.sleep(2)
            self.driver.find_element(*self.element.last_NewZealand_hotel).click()
            time.sleep(2)
            logger.info(self.driver.current_url)
            self.driver.back()
            js = "var action=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
            time.sleep(2)
            return True
        except:
            logger.info("can't display New Zealand region")

    def UniteStates_region(self):
        try:
            self.driver.find_element(*self.element.UnitedStates_region).click()
            time.sleep(2)
            self.driver.find_element(*self.element.last_UniteStates_hotel).click()
            time.sleep(2)
            logger.info(self.driver.current_url)
            time.sleep(2)
            self.driver.back()
            js = "var action=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
            time.sleep(2)
            return True
        except:
            logger.info("can't display Unite States region")
            return False


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://www.millenniumhotels.com")
# driver.find_element(*global_tab.Hotels_tab).click()
# driver.find_element_by_link_text('Asia').click()
# time.sleep(2)
# driver.find_element_by_link_text('Millennium Resort Patong Phuket').click()
# time.sleep(2)
# print(driver.current_url)
# driver.back()
# js="var action=document.documentElement.scrollTop=0"
# driver.execute_script(js)
# time.sleep(3)
# driver.find_element_by_link_text('Europe').click()
# time.sleep(2)
# driver.find_element_by_link_text('Copthorne Hotel Slough-Windsor').click()
# time.sleep(2)
# print(driver.current_url)
# driver.back()
# driver.refresh()
# time.sleep(3)


