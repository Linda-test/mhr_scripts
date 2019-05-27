"""===========================================================
TC Name: M0401 - Check m4b booking flow
Author : TinaZ
Created Time: 5/6/2019
Manual Steps + Expect Result:
    Step1 - Login m4b account
    Exp1 -  Login successfully
    ----------------------------------------------
    Step2 - Enter booking information in dashboard page and booking
    Exp2 -  Information entered successfully
    ----------------------------------------------
    Step3 - Proceed to booking the order in step3,4,5
    Exp3 -  Page direct to payment page, no exception
    ----------------------------------------------
    Step4 - Pay with credit card
    Exp4 -  Payment successfully
    ----------------------------------------------
    Step5 - Check the confirmation page
    Exp5 -  Confirmation page display normally
    ----------------------------------------------
    Step6 - Record the order number,the hotel name in excel
    Exp6 -  Record successfully
    ----------------------------------------------

Last Update Date + Update by Whom: 5/6/2019 by Tina Zhao
==============================================================="""
import unittest
from driver.browser import chrome_browser
from functions.BISBookingM4B import M4BBookingFlow
from time import *


class TestM4BBookingFlow(unittest.TestCase):
    def __init__(self):
        self.driver = chrome_browser()
        self.driver.get("https://www.millenniumhotels.com")
        time.sleep(5)
        self.m4b_booking = M4BBookingFlow()

    def test_m4b_bookingflow(self):
        """
        Step1 - Login m4b account
        Exp1 -  Login successfully
        """
        self.m4b_booking.login_m4b_with_facebook()







