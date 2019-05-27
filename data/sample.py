from selenium import webdriver
import unittest
import time, random,string


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.base_url = "https://www.millenniumhotels.com/en/business/account/register/"


    def test_m4bregister(self):
        src_digits = string.digits  # string_数字
        src_uppercase = string.ascii_uppercase  # string_大写字母
        src_lowercase = string.ascii_lowercase  # string_小写字母
        # 随机生成数字、大写字母、小写字母的组成个数（可根据实际需要进行更改）
        digits_nam = random.randint(1, 6)
        digits_cod = random.randint(1,5)
        digits_first_nam = random.randint(1,10)
        digits_last_nam = random.randint(1,10)
        digits_emailadd = random.randint(1,15)
        digits_pass = random.randint(1,10)
        uppercase_num = random.randint(1, 8 - digits_nam - 1)
        lowercase_num = 8 - (digits_nam + uppercase_num)
        # 生成字符串
        com_name = random.sample(src_digits, digits_nam) + random.sample(src_uppercase, uppercase_num) + random.sample(
            src_lowercase, lowercase_num)
        com_code = random.sample(src_digits, digits_cod) + random.sample(src_uppercase, uppercase_num) + random.sample(
            src_lowercase, lowercase_num)
        first_name = random.sample(src_digits, digits_first_nam) + random.sample(src_uppercase, uppercase_num) + random.sample(
            src_lowercase, lowercase_num)
        last_name = random.sample(src_digits, digits_last_nam) + random.sample(src_uppercase, uppercase_num) + random.sample(
            src_lowercase, lowercase_num)
        email_add = random.sample(src_digits, digits_emailadd) + random.sample(src_uppercase, uppercase_num) + random.sample(
            src_lowercase, lowercase_num)
        password = random.sample(src_digits, digits_pass) + random.sample(src_uppercase, uppercase_num) + random.sample(
            src_lowercase, lowercase_num)
        # 打乱字符串
        random.shuffle(com_name)
        random.shuffle(com_code)
        random.shuffle(first_name)
        random.shuffle(last_name)
        random.shuffle(email_add)
        random.shuffle(password)

        # 列表转字符串
        new_com = ''.join(com_name)
        new_cod = ''.join(com_code)
        new_first_name = ''.join(first_name)
        new_last_name = ''.join(last_name)
        new_email_add = ''.join(email_add)
        new_password = ''.join(password)
        print(new_com)
        print(new_cod)
        print(new_first_name)
        print(new_last_name)
        print(new_email_add)
        print(new_password)

        driver = self.driver
        driver.get(self.base_url + "/")
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter your Company Name']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter your Company Name']").send_keys(new_com)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter Company Registration Number']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter Company Registration Number']").send_keys(new_cod)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter your first name']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter your first name']").send_keys(new_first_name)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter your last name']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter your last name']").send_keys(new_last_name)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter personal E-mail address']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter personal E-mail address']").send_keys("%s@mailinator.com"%new_email_add)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter your password']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter your password']").send_keys(new_password)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
