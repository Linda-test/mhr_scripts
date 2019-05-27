from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from functions.Homepage import HomePage_Fun

class Register(HomePage_Fun):

    def M4B_register(self):
        self.enter_m4b_registerpage()

    def MM_register(self):
        self.enter_mm_registerpage()


