from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

class ele_collection(object):
    "首页"
    def __init__(self,driver):
        self.driver = driver
        self.element_business_icon = By.CLASS_NAME,'item item-m4b' #定位For Business按钮
        self.element_language = By.CLASS_NAME,"cl-text"
        self.element_zh_tw = By.XPATH,'//li[text()="简体中文"]'
        self.element_homepage_search = By.CLASS_NAME,"search-text"                    # 首页右上角的搜索框
        self.element_google = By.LINK_TEXT,"Sign in with Google"                      # gmail登录
        self.element_input_gmail = By.ID, "identifierId"                              # 输入gmail账号
        self.element_continue = By.CLASS_NAME, "RveJvd"                                # 点击继续

        self.element_switch_language = By.CLASS_NAME,"cl-text"                         # 定位语言标志
        self.element_select_arabic = By.XPATH,'.//ul[@class = "show-language"]/li[1]' # 选择阿拉伯语
        self.element_select_english = By.XPATH,'.//ul[@class = "show-language"]/li[2]' # 选择英语
        self.element_select_spanish = By.XPATH, './/ul[@class = "show-language"]/li[3]'  # 选择西班牙语
        self.element_select_franch = By.XPATH, './/ul[@class = "show-language"]/li[4]'  # 选择法语
        self.element_select_italian = By.XPATH, './/ul[@class = "show-language"]/li[5]'  # 选择意大利语
        self.element_select_chinese_simple = By.XPATH, './/ul[@class = "show-language"]/li[6]'  # 选择简体中文
        self.element_select_chinese_traditional = By.XPATH, './/ul[@class = "show-language"]/li[7]'  # 选择繁体中文
        self.element_select_japanese = By.XPATH, './/ul[@class = "show-language"]/li[8]'  # 选择日语
        self.element_destination =By.CLASS_NAME, "hotel-title"                          # 定位特色目的地



class HomePage_Fun(ele_collection):
    """存放home界面方法"""

    def click_swictch_language(self):
        """点击语言"""
        self.driver.find_elements(*self.element_switch_language)[1].click()

    def switch_to_chinese(self):
        """点击简体中文"""
        self.driver.find_element(*self.element_select_chinese_simple).click()
        sleep(3)
        destination = self.driver.find_element(*self.element_destination).text
        assert destination == "特色目的地"

    def switch_to_english(self):
        """点击英语"""
        self.driver.find_element(*self.element_select_english).click()
        sleep(3)
        destination = self.driver.find_element(*self.element_destination).text
        assert destination == "FEATURED LOCATIONS"

    def switch_to_Arabic(self):
        """点击阿拉伯语"""
        self.driver.find_element(*self.element_select_arabic).click()
        sleep(3)
        destination = self.driver.find_element(*self.element_destination).text
        assert destination == "مواقع مميزة"

    def switch_to_spanish(self):
        """点击西班牙语"""
        self.driver.find_element(*self.element_select_spanish).click()
        sleep(3)
        destination = self.driver.find_element(*self.element_destination).text
        print(destination)
        assert destination == "DESTINOS DESTACADOS"

    def switch_to_franch(self):
        """点击法语"""
        self.driver.find_element(*self.element_select_franch).click()
        sleep(3)
        destination = self.driver.find_element(*self.element_destination).text
        assert destination == "LIEUX PRÉSENTÉS"

    def switch_to_litalian(self):
        """点击意大利语"""
        self.driver.find_element(*self.element_select_italian).click()
        sleep(3)
        destination = self.driver.find_element(*self.element_destination).text
        assert destination == "LOCALITÀ IN PRIMO PIANO"

    def switch_to_chinese_traditional(self):
        """点击繁体中文"""
        self.driver.find_element(*self.element_select_chinese_traditional).click()
        sleep(3)
        destination = self.driver.find_element(*self.element_destination).text
        assert destination == "精選城市"

    def switch_to_japanese(self):
        """点击日语"""
        self.driver.find_element(*self.element_select_japanese).click()
        sleep(3)
        destination = self.driver.find_element(*self.element_destination).text
        assert  destination == "注目のロケーション"

    # def sign_in_facebooks(self,face_email,face_pass):
    #     """facebook登录"""
    #     self.login_homepage()
    #     self.driver.find_element(*self.element_facebook).click()
    #     self.driver.find_element(*self.element_facebook_email).send_keys(self.face_email)
    #     self.driver.find_element(*self.element_facebook_password).send_keys(self.face_pass)
    #     sleep(3)
    #     self.driver.find_element(*self.element_login_button).click()
    #     sleep(2)
    #     self.sign_out_homepage()
    #     sleep(5)

    # def sign_in_linkedin(self,link_acc,link_pass):
    #     """linkedin登录"""
    #     self.link_acc = link_acc
    #     self.link_pass = link_pass
    #     self.login_homepae()
    #     self.driver.find_element(*self.element_LinkedIn).click()
    #     self.driver.find_element(*self.element_linkedin_email).send_keys(self.link_acc)
    #     self.driver.find_element(*self.element_linkedin_pwd).send_keys(self.link_pass)
    #     self.driver.find_element(*self.element_click_linkedin_signin).click()
    #
    # def sign_in_google(self):
    #     """gmail登录"""
    #     self.login_homepae()
    #     self.driver.find_element(*self.element_google).click()
    #     self.driver.find_element(*self.element_input_gmail).send_keys("liuyan061061@gmail.com")
    #     self.driver.find_elements(*self.element_continue)[0].click()
    #     self.driver.find_element(By.NAME, "password").send_keys("ly605402932")
    #     self.driver.find_elements(*self.element_continue)[0].click()
    #     sleep(3)
    #     self.sign_out_homepage()
    #     sleep(3)


    def enter_m4b_registerpage(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.millenniumhotels.com")
        self.driver.find_element(*self.element_business_icon).click()
        sleep(3)
        for i in range(10):
            try:
                el = self.driver.find_element_by_xpath("//*[@class='icon-icon_mhr_m4b-logo-white']")
                if el.is_displayed():
                    break
            except: pass
            sleep(1)
        else:
            print("time out")
        return

    def enter_mm_registerpage(self):
        pass

    # if __name__ == '__main__':

# home = HomePage_Fun()
# home.enter_m4b_registerpage()




