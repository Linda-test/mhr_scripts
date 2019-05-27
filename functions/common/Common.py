""" ================================================================================================================
@Description: This module defines the business functions about register,login and update account management.
              Use these function and update if necessary.
@Last Update Date + Update by Whom: 5/25/2019 by TinaZ
====================================================================================================================="""
from elements.ElementsDefine import ElementsDefine
from functions.common.ExcelUtil_tool import ExcelUtil
from functions.common.global_variable import GlobalVariable
from functions.common.log import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

# ENV = ExcelUtil.readExcel('../data/acc&env_info.xlsx','Sheet1')
ENV = ExcelUtil.readExcel('C:\\MLP\\Automation\\Project\data\\acc&env_info.xlsx','Sheet1')

class Common(object):
    def __init__(self,driver):      # Initial for the elements
        self.driver = driver
        self.element = ElementsDefine()
        self.glovar = GlobalVariable()

    def open_browser(self):
        """
            open browser with environment link
        :return:
        """
        i = 0
        while i <= 3:
            try:
                self.driver.get(self.glovar.ENV_LINK)
                WebDriverWait(self.driver,1).until(EC.presence_of_element_located((self.element.element_login_icon)))
                print('-' * 20 + '%s %s page successfully opened.'% (self.glovar.ENV,self.glovar.ENV_LINK) + '-' * 20)
                break
            except Exception as error:
                i += 1
                print('-'*20+'Failed during open homepage, try %s times' % i + '-'*20+'%s' % error)
                self.driver.refresh()

    def check_result(self):
        pass

    def is_element_visible(self, element):
        try:
            the_element = EC.visibility_of_element_located((element))
            assert the_element(self.driver)
            logger.info("%s is displayed" % the_element)
            return True
        except Exception as err:
            print(err)
            logger.info("element is not displayed")
            return False

