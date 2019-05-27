"""===========================================================
@TC Name: M0401 - Check m4b booking flow
@Author : TinaZ
@Created Time: 5/7/2019
@Prerequisites:
@Manual Steps + Expect Result:
    Step1 - Login retail account
    Exp1 -  Login successfully
    ----------------------------------------------
    Step2 - Enter booking information in booking widget home page and booking
    Exp2 -  Information entered successfully
    ----------------------------------------------
    Step3 - Proceed to booking the order
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

@Last Update Date + Update by Whom: 5/7/2019 by Tina Zhao
==============================================================="""

import unittest
from functions.common.ExcelUtil_tool import ExcelUtil
from driver.browser import chrome_browser
from ddt import ddt,data

from functions.BISBooking import BookingFlow
from elements.ElementsDefine import ElementsDefine
from functions.BISAccount import Account
from functions.common.Common import Common

LOGIN_DATA = ExcelUtil.readExcel('../data/acc&env_info.xlsx','Sheet1')

@ddt
class TestBookingFlow(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_browser()
        self.common = Common(self.driver)
        self.element = ElementsDefine()
        self.bookflow = BookingFlow(self.driver)
        self.account = Account(self.driver)

        # open UAT3 on chrome browser('0'-Live, '1'-UAT, '2'-UAT2, '3'-UAT3)
        self.common.open_browser(3)

    @data(*LOGIN_DATA)
    def test_m4b_bookingflow(self,data):
        """
        Step1 - Login retail account
        Exp1 -  Login successfully
        """
        self.account.login_with_facebook(data['face_email'],data['face_pw'])
        """
        Step2 - Enter booking information in booking widget home page and booking
        Exp2 -  Information entered successfully
        """
        self.bookflow.enter_booking_info_in_booking_widget()
        self.bookflow.click_checkrr_city_bookflow_page()
        """
        Step3 - Proceed to booking the order
        Exp3 -  Page direct to payment page, no exception
        """
        self.bookflow.click_check_hotel_bookflow_page()
        self.bookflow.close_IG()


        """
        Step4 - Pay with credit card
        Exp4 -  Payment successfully
        """
        self.bookflow.pay_with_creditcard()

        # """
        # Step5 - Check the confirmation page
        # Exp5 -  Confirmation page display normally
        # """
        # self.bookflow.check_info_in_confirmation_page()
        #
        # """
        # Step6 - Record the order number,the hotel name in excel
        # Exp6 -  Record successfully
        # """
        # self.bookflow.record_info_to_excel()


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
