import unittest
import ddt
from selenium import webdriver
from data.read_excel import ExcelUtil
from functions.login import login_func

Exc = ExcelUtil()
logindata = Exc.readExcel('C:/Users/linda.li2/Desktop/millenniumhotels/data/email&password.xlsx','facebook')

@ddt.ddt
class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.millenniumhotels.com")

    def tearDown(self):
        self.driver.close()

    @ddt.data(*logindata)
    def test_login_facebook(self,data):
        """测试facebook登录"""
        login_func.sign_in_facebook(data['face_email'], data['face_pass'])


    if __name__ == '__main__':
        unittest.main()
#
