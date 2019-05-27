import time
from elements.ElementsDefine import ElementsDefine
from functions.common.log import logger


class meetings_events_func(object):

    def __init__(self, driver):
        self.driver = driver
        self.element = ElementsDefine()

    def filter_destination(self):
        self.driver.find_element(*self.element.destination_filter).click()
        time.sleep(3)
        self.driver.find_element(*self.element.select_destination_singapore).click()
        time.sleep(3)
        des_type_selection = self.driver.find_element(*self.element.destination_type).text
        logger.info(des_type_selection)
        assert des_type_selection == 'Singapore'
        logger.info("destination filter works right")

    def filter_event_type(self):

        self.driver.find_element(*self.element.event_type_filter).click()
        time.sleep(3)
        self.driver.find_element(*self.element.select_event_type_Conference).click()
        time.sleep(3)
        event_type_selection = self.driver.find_element(*self.element.event_type_txt).text
        logger.info(event_type_selection)
        assert event_type_selection == 'Conference'
        logger.info("event filter works right")

    def filter_attendees_type(self):
        self.driver.find_element(*self.element.attendees_filter).click()
        time.sleep(3)
        self.driver.find_element(*self.element.select_attendees_21).click()
        time.sleep(3)
        attendees_type_selection = self.driver.find_element(*self.element.attendees_type_txt).text
        logger.info(attendees_type_selection)
        assert attendees_type_selection == '21 - 50'
        logger.info("attendees filter works right")