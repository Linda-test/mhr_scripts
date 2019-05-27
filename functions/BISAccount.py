""" ================================================================================================================
@Description: This module defines the business functions about register,login and update account management.
              Use these function and update if necessary.
@Last Update Date + Update by Whom: 5/25/2019 by TinaZ
====================================================================================================================="""
import datetime
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from elements.ElementsDefine import ElementsDefine
from functions.common.Common import Common
from functions.common.log import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Account(object):
    def __init__(self, driver):      # Initial for the elements
        self.driver = driver
        self.element = ElementsDefine()
        self.common = Common(driver)

    """-----------------------------------------------------------
    @Description:  A series of function about login
    @Author: Yan Liu
    @Parameter: ()
                - 
                -
    @Output: True/False/Empty
             1)
             2）
             3）
    @Example:
    @Prerequisites: 1) not login
    @Business Steps: 
    @Last Update Date + Update by Whom: 5/25/2019 by TinaZ
    -------------------------------------------------------------"""

    def login_homepage(self):
        """点击登录按钮"""
        try:
            self.driver.find_elements(*self.element.element_login_icon)[1].click()
            logger.info("Login overlay open successfully")
        except Exception as result:
            logger.warning("%s unknown error happened" % result)

    """-----------------------------------------------------------
    @Description:  A series of function about login
    @Author: Yan Liu
    @Parameter: ()
                - 
                -
    @Output: True/False/Empty
             1)
             2）
             3）
    @Example:
    @Prerequisites: 1) not login
    @Business Steps: 
    @Last Update Date + Update by Whom: 5/25/2019 by TinaZ
    -----------------------------------------------------------"""
    def logout_homepage(self):
        """登出"""
        self.driver.find_element(*self.element.element_loginuser_logout).click()
        self.driver.find_element(*self.element.element_sign_out_homepage).click()

    def login_with_facebook(self, face_email, face_pw):
        """facebook登录"""
        self.face_email = face_email
        self.face_pw = face_pw
        self.login_homepage()
        try:
            self.driver.find_element(*self.element.element_facebook).click()
            logger.info("click the facebook login button")
            print('-'*20+'click faecbook sign in'+'-' * 20)
            self.driver.find_element(*self.element.element_facebook_email).send_keys(self.face_email)
            logger.info("input facebook acccount")
            print('-' * 20 + 'input facebook email' + '-' * 20)
            self.driver.find_element(*self.element.element_facebook_password).send_keys(self.face_pw)
            logger.info("input facebook password")
            print('-' * 20 + 'input facebook password' + '-' * 20)
            self.driver.find_element(*self.element.element_login_button).click()
            logger.info("click facebbook login button")
            print('-' * 20 + 'click sign in' + '-' * 20)
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((self.element.login_status)))
            logger.info("login successfully")
            print('-' * 20 + 'facebook login successfully' + '-' * 20)
        except Exception as result:
            logger.warning("%s error happened" % result)
        finally:
            logger.info(self.driver.current_url)


    def login_with_linkedin(self, link_acc, link_pw):
        """linkedin登录"""
        self.linkedin_acc = link_acc
        self.linkedin_pw = link_pw
        self.login_homepage()
        try:
            self.driver.find_element(*self.element.element_LinkedIn).click()
            logger.info("click linkedin login button")
            print('-'*20+'click linkedin sign in'+'-' * 20)
            self.driver.find_element(*self.element.element_linkedin_email).send_keys(self.linkedin_acc)
            logger.info("input linkedin account")
            print('-' * 20 + 'input linkedin account' + '-' * 20)
            self.driver.find_element(*self.element.element_linkedin_pwd).send_keys(self.linkedin_pw)
            logger.info("input linkedin password")
            print('-' * 20 + 'input linkedin password' + '-' * 20)
            self.driver.find_element(*self.element.element_click_linkedin_signin).click()
            logger.info("click linkedin sign in button")
            print('-' * 20 + 'click sign in' + '-' * 20)
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((self.element.login_status)))
            logger.info("login successfully")
            print('-' * 20 + 'linkedin login successfully' + '-' * 20)
        except Exception as result:
            logger.warning("%s error happened" % result)
        finally:
            logger.info(self.driver.current_url)
            time.sleep(2)

    def login_with_google(self,google_acc,google_pw):
        """gmail登录"""
        self.google_acc = google_acc
        self.google_pw = google_pw
        self.login_homepage()
        self.driver.find_element(*self.element.element_google).click()
        logger.info("click google login button")
        print('-' * 20 + 'click google sign in' + '-' * 20)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((self.element.element_input_gooogleacc)))
        self.driver.find_element(*self.element.element_input_gooogleacc).send_keys(google_acc)
        print('-' * 20 + 'input google account' + '-' * 20)
        self.driver.find_elements(*self.element.element_continue)[0].click()
        print('-' * 20 + 'click next step' + '-' * 20)
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.element.element_input_googlepw)))
        except Exception as error:
            print('-' * 20 + "Failed redirect to google pass word page" + '-' * 20 + '%s' % error)
        self.driver.find_element(*self.element.element_input_googlepw).send_keys(google_pw)
        print('-' * 20 + 'input google password' + '-' * 20)
        self.driver.find_elements(*self.element.element_continue)[0].click()
        print('-' * 20 + 'click next step' + '-' * 20)
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((self.element.login_status)))
            logger.info("login successfully")
            print('-' * 20 + 'google login successfully' + '-' * 20)
        except Exception as result:
            logger.warning("%s error happened" % result)
        finally:
            logger.info(self.driver.current_url)

    def login_with_email(self,email_acc,email_pw):
        pass

    def login_m4b_with_facebook(self):
        pass

    def login_m4b_with_google(self):
        pass

    def login_m4b_with_linkedin(self):
        pass

    def login_m4b_with_email(self):
        pass




















