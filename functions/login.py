# from page_element import page_element_file
from time import sleep
from elements.ElementsDefine import loginpage

class login_func(object):

    def __init__(self,driver):
        self.driver = driver

    def sign_in_facebook(self,face_email,face_pass):
        """Open login overlay"""
        self.driver.find_element(*loginpage.login_icon).click()
        """Go to sign in by facebook account"""
        self.driver.find_element(*loginpage.facebook_login_button).click()
        self.driver.find_element(*loginpage.facebook_email).send_keys(face_email)
        self.driver.find_element(*loginpage.facebook_password).send_keys(face_pass)
        sleep(3)
        self.driver.find_element(*loginpage.login_button).click()
        sleep(2)

    def sign_out(self):
        """登出"""
        self.driver.find_element(*loginpage.loginuser_logout).click()
        self.driver.find_element(*loginpage.sign_out_homepage).click()


