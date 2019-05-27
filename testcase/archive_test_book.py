import unittest
from selenium import webdriver
from time import sleep
from functions.BookingPage import Bookflow
hotelname = "M Social Singapore"

class Test_Book(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.millenniumhotels.com")
        self.booktest = Bookflow(driver=self.driver)

    def tearDown(self):
        self.driver.close()

    def test_booking(self):
        self.booktest.book_room(hotelname)


    if __name__ == "__main__":
        unittest.main()
