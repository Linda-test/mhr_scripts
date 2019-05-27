"""===========================================================
@TC Name: M0100 Create retail account - normal
@Author : TinaZ
@Created Time: 4/25/2019
@Manual Steps + Expect Result:
    Step1 - Open hotel property page
    Exp1 -  Property page opened
    ----------------------------------------------
    Step2 - Check rooms section
    Exp2 -  Property page opened
    ----------------------------------------------
    Step3 - Check other section
    Exp3 -  Each item works well
    ----------------------------------------------
@Last Update Date + Update by Whom: 5/25/2019 by Tina Zhao
==============================================================="""

import unittest
from driver.browser import *
import time
from functions.BISPages import Pages


class TestPropertyElements(unittest.TestCase):

    def setUp(self):
        self.driver = chrome_browser()
        self.driver.get("https://www.millenniumhotels.com")
        time.sleep(5)
        self.property_page = Pages(self.driver)

    def test_property_page(self):
        """Step1 - Open hotel property page
        Exp1 -  Property page opened """
        self.property_page.proceed_to_property_page()

        """Step2 - Check rooms section
        Exp2 -  Property page opened """
        self.property_page.check_rooms_section()

        """Step3 - Check other section
        Exp3 -  Each item works well """
        self.property_page.check_other_section()

    @unittest.skip("I don't want to run this testcase.")  # skip one testcase to keep excuting others
    def test_property_elements(self):
        # Test proceed to hotel property page
        pass

    def tearDown(self):
        self.driver.quit()  # close broswer

    if __name__ == "__main__":
        unittest.main()
