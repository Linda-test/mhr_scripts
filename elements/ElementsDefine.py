from selenium.webdriver.common.by import By

class ElementsDefine(object):

    def __init__(self):

        #Homepage elements
        self.element_login_icon = By.ID, 'opt-login'  # 定位登录按钮
        self.element_facebook = By.CLASS_NAME,'wgt-sqbutton-facebook' # 定位facebook登录
        self.element_facebook_email = By.ID, "email"  # facebook界面的输入邮箱和密码
        self.element_facebook_password = By.ID, "pass"
        self.element_login_button = By.ID, "loginbutton"  # facebook登录按钮

        self.element_language = By.CLASS_NAME, "cl-text"
        self.element_zh_tw = By.XPATH, '//li[text()="简体中文"]'
        self.element_homepage_search = By.CLASS_NAME, "search-text"  # 首页右上角的搜索框

        self.element_google = By.CLASS_NAME, 'wgt-sqbutton-google'  # gmail登录
        self.element_input_gooogleacc = By.ID, "identifierId"  # 输入google账号
        self.element_input_googlepw = By.NAME,'password' #输入google账号密码
        self.element_continue = By.CLASS_NAME, "RveJvd"  # 点击继续
        # self.element_pw_continue = By.CSS_SELECTOR,'#passwordNext > content:nth-child(3) > span:nth-child(1)' #点击密码继续

        self.login_status = By.CSS_SELECTOR,'body > div.global-wrapper.index-wrapper > div.navbar > div.menu-wrapper > div.user-module-desktop > div > div > div > div.nav > div.logged-in > div.login-in.show-user > div' #登录状态
        self.expand_profile = By.CSS_SELECTOR,'div.nav:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)' #定位展开profile
        self.view_profile = By.CSS_SELECTOR,'div.pc-new-user:nth-child(1) > span:nth-child(2) > a:nth-child(1)' #定位 view profile

        #profile page
        self.profile_img = By.CSS_SELECTOR,'.mm2-board-header-desktop > div:nth-child(1) > img:nth-child(1)' #定位用户图标
        self.profile_welcome = By.CSS_SELECTOR,'.mm2-board-avater-container-welcome > span:nth-child(1)' #定位welcome文字
        self.profile_name = By.CSS_SELECTOR,'.mm2-board-avater-container-name'
        self.profile_member_since = By.CSS_SELECTOR,'.mm2-board-header-desktop > div:nth-child(2) > div:nth-child(1)' #定位membersince
        self.profile_member_num = By.CSS_SELECTOR,'div.mm2-board-member-block:nth-child(3) > div:nth-child(1)' #定位member number
        self.print_member_card = By.CLASS_NAME,'mm2-board-member-block-link' #定位print member card
        self.point_available = By.XPATH,"//*[@class='mm2-board-points-num-big active']" #定位available point
        self.redeem_disable_status = By.CSS_SELECTOR,'div.swiper-slide:nth-child(4) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)'
        self.redeem_active_status = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-vouchers-container > div.mm2-board-vouchers-desktop > div.mm2-board-vouchers-content-swiper.mm2-board-vouchers-content-swiper-has-fixed-item > div.swiper-container > div > div.swiper-slide.swiper-slide-visible.swiper-slide-active > div > div.mm2-vouchers-item-bottom-container > span.mm2-gold-button'
        self.point_progress = By.CSS_SELECTOR,'.mm2-board-points-progress' #定位point progress bar
        self.point_expired = By.CSS_SELECTOR,'.mm2-board-points-num-small' #定位 point expiring in next 3 months
        self.transfer_points = By.LINK_TEXT,'Transfer Points' #定位 transfer point
        self.View_Points_History = By.LINK_TEXT,'View Points History' #定位view point history
        self.discover_rewards = By.CSS_SELECTOR,'.mm2-board-points-bottom-block-button > a:nth-child(1)' #定位discover rewards
        self.task_icon = By.CSS_SELECTOR,'div.mm2-board-earn-detail-container:nth-child(2) > div:nth-child(1)' #定位task icon
        self.task_thumbnail_icon = By.CSS_SELECTOR,'div.mm2-board-earn-bottom-container:nth-child(3) > div:nth-child(1) > div:nth-child(1)' #定位task thumdnail icon
        self.task_status = By.CSS_SELECTOR,'div.mm2-board-earn-bottom-container:nth-child(3) > div:nth-child(1) > div:nth-child(2)' #定位task status
        self.task_des = By.CSS_SELECTOR,'div.mm2-board-earn-detail-container:nth-child(2) > p:nth-child(2)' #定位task 描述
        self.redeem_now = By.CSS_SELECTOR,'h3.active'
        self.my_vouchers = By.CSS_SELECTOR, '.mm2-multiple-header > h3:nth-child(2)'
        self.reward_list_first = By.XPATH,"//*[@class='swiper-slide swiper-slide-visible swiper-slide-active']"
        self.more_rewards = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-vouchers-container > div.mm2-board-vouchers-desktop > div.mm2-board-vouchers-header.mm2-multiple-header > a'
        self.catalogue_available = By.CLASS_NAME,'tip-title'
        self.close_catalogue = By.XPATH,"//*[@class='wgt-sqbutton-black tip-button']"
        self.reward_img = By.CSS_SELECTOR,'div.swiper-slide:nth-child(4) > div:nth-child(1) > div:nth-child(1)'
        self.reward_points = By.CSS_SELECTOR,'div.swiper-slide:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'
        self.reward_points_overlay = By.CSS_SELECTOR,'.mm2-board-popup-voucher-points'
        self.reward_name = By.CSS_SELECTOR,'div.swiper-slide:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1)'
        self.redeem_des = By.CSS_SELECTOR,'div.swiper-slide:nth-child(4) > div:nth-child(1) > div:nth-child(2) > p:nth-child(2)'
        self.redeem_view_details = By.CSS_SELECTOR,'div.swiper-slide:nth-child(4) > div:nth-child(1) > div:nth-child(3) > span:nth-child(2)'
        self.reward_required_point = By.CSS_SELECTOR,'div.swiper-slide:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
        self.REDEEMM_REWARD_btn = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-layer-container > div > div.mm2-board-popup-voucher-bottom-container > span.mm2-gold-button'
        self.Cancel_btn = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-layer-container > div > div.mm2-board-popup-voucher-bottom-container > span.mm2-board-popup-voucher-bottom-container-link'
        self.redeem_now_title = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-layer-container > div > h3'
        self.reward_REDEEM = By.CSS_SELECTOR,'div.swiper-slide:nth-child(4) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)'
        self.redeem_are_you1 = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-layer-container > div > h3'
        self.redeem_are_you2 =By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-layer-container > div > div.mm2-board-popup-voucher-confirm-content > div:nth-child(2)'

        self.explore_list = By.XPATH,"//*[@class='mm2-vouchers-item mm2-vouchers-item-fixed']"
        self.explore_img = By.CSS_SELECTOR,'.mm2-vouchers-item-fixed > div:nth-child(1)'
        self.explore_name = By.CSS_SELECTOR,'.mm2-vouchers-item-fixed > div:nth-child(2) > h3:nth-child(1)'
        self.explore_des = By.CSS_SELECTOR,'.mm2-vouchers-item-fixed > div:nth-child(2) > p:nth-child(2)'
        self.explore_btn = By.LINK_TEXT,'EXPLORE'
        self.store_mark = By.CSS_SELECTOR,'#topNav > div > div.navbar-header.pull-left > ul > li > a > img'
        self.redeem_overlay_img = By.CSS_SELECTOR,'.mm2-board-popup-voucher-image'
        self.redeem_overlay_name = By.CSS_SELECTOR,'.mm2-board-popup-voucher-name'
        self.redeem_overlay_des = By.CSS_SELECTOR,'.mm2-board-popup-voucher-caption'
        self.redeem_overlay_point = By.CSS_SELECTOR,'.mm2-board-popup-voucher-points'
        self.redeem_overlay_tac = By.CSS_SELECTOR,'.mm2-board-popup-voucher-sub-caption'
        self.redeem_overlay_close = By.CSS_SELECTOR,'.mm2-board-popup-voucher-header > span:nth-child(1)'
        self.redeem_overlay_cancel = By.CSS_SELECTOR,'span.mm2-board-popup-voucher-bottom-container-link:nth-child(1)'
        self.redeem_overlay_redeem = By.CSS_SELECTOR,'span.mm2-gold-button:nth-child(2)'
        self.voucher_view_details = By.CSS_SELECTOR,'.mm2-board-vouchers-desktop > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)'
        self.voucher_close = By.CSS_SELECTOR,'.mm2-board-popup-voucher-header > span:nth-child(1)'
        self.view_all_my_vouchers = By.LINK_TEXT,'View All My Vouchers'
        self.my_redeemed_vouchers_mark = By.LINK_TEXT,"All Bookings"


        self.element_loginuser_logout = By.XPATH, '/html/body/div[1]/div[11]/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/a[1]'
        self.element_sign_out_homepage = By.LINK_TEXT, "Sign Out"  # 定位退出

        self.element_LinkedIn = By.CLASS_NAME, 'wgt-sqbutton-linkedin'  # 定位linkedin登录
        self.element_linkedin_email = By.ID, "username"
        self.element_linkedin_pwd = By.ID, "password"
        self.element_click_linkedin_signin = By.CLASS_NAME, "btn__primary--large"


        self.element_switch_language = By.CLASS_NAME, "cl-text"  # 定位语言标志
        self.element_select_arabic = By.XPATH, './/ul[@class = "show-language"]/li[1]'  # 选择阿拉伯语
        self.element_select_english = By.XPATH, './/ul[@class = "show-language"]/li[2]'  # 选择英语
        self.element_select_spanish = By.XPATH, './/ul[@class = "show-language"]/li[3]'  # 选择西班牙语
        self.element_select_franch = By.XPATH, './/ul[@class = "show-language"]/li[4]'  # 选择法语
        self.element_select_italian = By.XPATH, './/ul[@class = "show-language"]/li[5]'  # 选择意大利语
        self.element_select_chinese_simple = By.XPATH, './/ul[@class = "show-language"]/li[6]'  # 选择简体中文
        self.element_select_chinese_traditional = By.XPATH, './/ul[@class = "show-language"]/li[7]'  # 选择繁体中文
        self.element_select_japanese = By.XPATH, './/ul[@class = "show-language"]/li[8]'  # 选择日语
        self.element_destination = By.CLASS_NAME, "hotel-title"  # 定位特色目的地
        # Register page elements


        # Property page elements
        self.link_hotels_xpath = By.XPATH, "/html/body/div[1]/div[11]/div[2]/div[1]/ul/li[3]/a/span"
        self.link_hotel_name_xpath = By.XPATH,'/html/body/div[1]/div[9]/div/div[3]/div/div[2]/div[6]/div[2]/a'  # 'Grand Copthorne Waterfront' hotel
        self.link_room_section_text = 'Rooms'


        # Retail booking flow elements
        self.destination = By.CSS_SELECTOR, "textarea.textfield-input"
        self.city_select = By.CSS_SELECTOR,'a.search-item:nth-child(9) > span:nth-child(2)'
        self.book_btn = By.CSS_SELECTOR,'.dont-close-result'
        self.explore_city = By.LINK_TEXT,'EXPLORE CITY'
        # self.click_checkin= By.XPATH,'/html/body/div[1]/div[10]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[1]/div[1]/span'
        # self.next_month = By.XPATH,'/html/body/div[1]/div[10]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/table/thead/tr[1]/th[3]/div/span'
        # self.select_date = By.NAME,'1'
        # self.expand_guests = By.CLASS_NAME,'booking-guests-arrow icon-icon_chervonDown'
        # self.element_book = By.CLASS_NAME, "dont-close-result"

        # City booking flow page
        self.btn_checkrmsrts_citybfpage = By.XPATH,"//div[@class='x-highlight'][1]" \
                                                 "//button[@class='x-fs-14 x-ff-mh x-btn x-btn-azure ']"

        # Hotel booking flow page
        self.btn_checkout_hotelbfpage = By.XPATH,"//div[@class='x-mt-20 ']/button"

        # Payment Page
        self.item_wallet_paymentpage = By.XPATH,"//div[@class='selected-content credit-card-block']"
        self.item_IG_paymentpage = By.XPATH,"//div[@class='book2-lampbox-container x-al-l x-normal mm2-ig-container']"
        self.txt_card_name = By.XPATH,"//div[@class='input-box']/input[@placeholder='Full name on the credit card']"
        self.txt_card_num = By.XPATH,"//div[@class='input-box']/input[@placeholder='XXXX XXXX XXXX XXXX']"
        self.txt_card_code = By.XPATH,"//div[@class='input-box small-size']/input[@placeholder='xxxx']"
        self.txt_card_expiry_month = By.XPATH,"//div[@class='input-box small-size']/input[@placeholder='MM']"
        self.txt_card_expiry_year = By.XPATH,"//div[@class='input-box small-size']/input[@placeholder='YYYY']"

        #hotels page
        self.All_region = By.LINK_TEXT,'All'
        self.last_All_hotels = By.LINK_TEXT,'Scottsdale'
        self.Asia_region = By.LINK_TEXT,'Asia'
        self.last_Asia_hotels = By.LINK_TEXT,'Millennium Resort Patong Phuket'
        self.Europe_region = By.LINK_TEXT,'Europe'
        self.last_Europe_hotels = By.LINK_TEXT,'Copthorne Hotel Slough-Windsor'
        self.MiddleEast_region = By.LINK_TEXT,'Middle East'
        self.last_MiddleEast_hotels = By.LINK_TEXT,'Copthorne Hotel Sharjah'
        self.NewZealand_region = By.LINK_TEXT,'New Zealand'
        self.last_NewZealand_hotel = By.LINK_TEXT,'Copthorne Hotel Wellington Oriental Bay'
        self.UnitedStates_region = By.LINK_TEXT,'United States'
        self.last_UniteStates_hotel = By.LINK_TEXT,'The McCormick Scottsdale'

        #global_tab
        """Global 菜单定位元素"""
        self.Hotels_tab = By.LINK_TEXT,'Hotels'
        self.Venues_tab = By.LINK_TEXT,'Venues'
        self.Mymillennium_tab = By.LINK_TEXT,'My Millennium'
        self.Offers_tab = By.LINK_TEXT,'Offers'

        """Offers界面定位元素"""
        self.explore_offers = (By.LINK_TEXT,'Explore Offers')
        self.offer_type = By.XPATH,'/html/body/div[1]/div[9]/div/div[2]/div[2]/div[4]/div[1]/span[1]'
        self.type_select = By.XPATH,'/html/body/div[1]/div[9]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[5]/div'
        self.booknow_offer_btn = (By.CLASS_NAME, 'wgt-sqbutton-golden')
        self.offer_book = (By.CLASS_NAME,'offers2__details-sidebar-redirect')
        self.offer_type_txt = By.XPATH,'/html/body/div[1]/div[9]/div/div[4]/div[2]/div[1]/div[1]/div/div[2]'

        """Venues 界面定位元素"""
        self.destination_filter = (By.XPATH,'/html/body/div[1]/div[9]/div/div[2]/div[2]/div[2]/div[1]/span[1]')
        self.select_destination_singapore = (By.LINK_TEXT,'Singapore')
        self.destination_type = (By.XPATH,'/html/body/div[1]/div[9]/div/div[2]/div[2]/div[2]/div[1]/span[1]')
        self.event_type_filter = (By.XPATH,'/html/body/div[1]/div[9]/div/div[2]/div[2]/div[4]/div[1]/span[1]')
        self.select_event_type_Conference = (By.XPATH,'/html/body/div[1]/div[9]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div')
        self.attendees_filter = (By.XPATH,'/html/body/div[1]/div[9]/div/div[2]/div[2]/div[6]/div[1]/span[1]')
        self.select_attendees_21 = (By.XPATH,'/html/body/div[1]/div[9]/div/div[2]/div[2]/div[6]/div[2]/div/div[2]/div[2]/div')
        self.event_type_txt = (By.XPATH,'/html/body/div[1]/div[9]/div/div[2]/div[2]/div[4]/div[1]/span[1]')
        self.attendees_type_txt = (By.XPATH,'/html/body/div[1]/div[9]/div/div[2]/div[2]/div[6]/div[1]/span[1]')

        """My Millennium 界面定位元素"""
        self.My_Millennium_link = (By.LINK_TEXT,'My Millennium')
        self.Stay_Like_A_Millionaire_link = (By.LINK_TEXT,'Stay Like A Millionaire')
        self.Participating_Hotels_link = (By.LINK_TEXT,'Participating Hotels')
        self.Frequently_Asked_Questions_link = (By.LINK_TEXT,'Frequently Asked Questions')
        self.Terms_and_Conditions_link = (By.LINK_TEXT,'Terms and Conditions')

        """Upcoming page"""
        self.upcoming_bookings = By.CSS_SELECTOR,'.mm2-board-upcoming-header'
        self.upcoming_bookings_img = By.XPATH,"//*[@class='mm2-board-upcoming-swiper-item center-center']"
        self.upcoming_bookings_date = By.XPATH,"//*[@class='mm2-board-upcoming-date']"
        self.upcoming_bookings_name = By.XPATH,"//*[@class='mm2-board-upcoming-message-header']"
        self.upcoming_bookings_no = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-upcoming-container > div > div.mm2-board-upcoming-message-container > div.m4b-scroll-container > div > div:nth-child(3) > div > div:nth-child(1) > div.mm2-board-upcoming-message-order-trunk-content'
        self.upcoming_bookings_roomtype = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-upcoming-container > div > div.mm2-board-upcoming-message-container > div.m4b-scroll-container > div > div:nth-child(3) > div > div:nth-child(2) > div.mm2-board-upcoming-message-order-trunk-content'
        self.upcoming_bookings_occupancy = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-upcoming-container > div > div.mm2-board-upcoming-message-container > div.m4b-scroll-container > div > div:nth-child(3) > div > div:nth-child(3) > div.mm2-board-upcoming-message-order-trunk-content'
        self.upcoming_bookings_rate = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-upcoming-container > div > div.mm2-board-upcoming-message-container > div.m4b-scroll-container > div > div:nth-child(3) > div > div:nth-child(4) > div.mm2-board-upcoming-message-order-trunk-content'

        """bottom section"""
        self.bottom_section = By.XPATH,"//*[@class='mm2-board-bottom-section']"
        self.bottom_section_left_img = By.XPATH,"//*[@class='mm2-board-bottom-left-img center-center']"
        self.bottom_section_left_des = By.XPATH,"//*[@class='mm2-board-bottom-left-content']"
        self.bottom_section_right_container = By.XPATH,"//*[@class='mm2-board-bottom-right-container']"
        self.bottom_section_right_title = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-bottom-section-wrapper > div > div.mm2-board-bottom-right.center-center > div.mm2-board-bottom-right-container > h3'
        self.bottom_section_right_des = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-bottom-section-wrapper > div > div.mm2-board-bottom-right.center-center > div.mm2-board-bottom-right-container > div'
        self.bottom_section_view_now_btn = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div.mm2-container > div > div.mm2-board-bottom-section-wrapper > div > div.mm2-board-bottom-right.center-center > div.mm2-board-bottom-right-container > a'

        """My account"""
        self.My_Account = By.LINK_TEXT,'My Account'
        self.myaccount_tab = By.XPATH,"//*[@class='profile-page-tab']"
        self.update_img = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.page-content.block-profile.col-1120 > div.subviews > div.avatar > img'
        self.update_change_pic = By.XPATH,"//*[@class='change-text wgt-sqbutton-dark']"
        self.picture_list = By.XPATH,"//*[@class='default-img']"
        self.profile_1st = By.XPATH,"//img[@src='https://media.millenniumhotels.com/mhb-media/B/7/1/B71AA3CF-E153-48DD-81BB-8E5981686F60/MHR_Avatars-01.png?r=170805113023']"
        self.update_title = By.NAME,'title'
        self.update_title_select = By.XPATH,"//option[@value='Mrs']"
        self.update_gender = By.NAME,'gender'
        self.update_firtname = By.NAME,'first_name'
        self.update_lastname = By.NAME,'last_name'
        self.update_phone = By.NAME,'phone'
        self.update_mobilephone = By.NAME,'secondaryphone'
        self.update_birth_year = By.NAME,'yyyy'
        self.select_year = By.XPATH,"//option[@value='2000']"
        self.update_birth_month = By.NAME, 'mm'
        self.select_month = By.XPATH, "//option[@value='01']"
        self.update_birth_day = By.NAME, 'dd'
        self.select_day = By.XPATH,"//option[@value='30']"
        self.email_address = By.XPATH,"//input[@autocomplete='email']"
        self.update_country = By.NAME,'country'
        self.select_country = By.XPATH,"//option[@value='China(CN)']"
        self.update_address = By.XPATH,"//input[@autocomplete='street-address']"
        self.update_city = By.NAME,'city'
        self.update_state = By.NAME,'province'
        self.guest_state = By.NAME,'state'
        self.select_state = By.XPATH,"//option[@value='Chongqing(CQS)']"
        self.update_zip = By.NAME,'postal_code'
        self.guest_zip = By.NAME,'postal'
        self.update_date_format = By.NAME,'dateFormat'
        self.select_date_format = By.XPATH,"//option[@value='DD/MMM/YYYY']"
        self.update_my_profile_btn = By.XPATH,"//*[@class='wgt-sqbutton-black']"
        self.update_success_note = By.XPATH,"//*[@class='tipContent']"
        self.select_self = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.page-content.block-profile.col-1120 > div.choose-guest.loading-hide > div:nth-child(3) > div > div > i'
        self.remove_guest = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.page-content.block-profile.col-1120 > div.choose-guest.loading-hide > div:nth-child(2) > div > div > div.card-info > div > h6 > div > span:nth-child(2) > a'
        self.remove_btn = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.page-content.block-profile.col-1120 > div.choose-guest.loading-hide > div:nth-child(2) > div > div > div.confirm-tip > div > div > div.info > div > span.sure'
        self.remove_tip = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.page-content.block-profile.col-1120 > div.publicTip > div > div'


        self.change_my_password = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.profile-page-tab > a:nth-child(2) > span'
        self.current_password = By.XPATH,"//input[@name='old_password']"
        self.new_password = By.XPATH,"//input[@name='password']"
        self.confirm_password = By.XPATH,"//input[@name='password_confirm']"
        self.update_password_btn = By.XPATH,"//*[@class='wgt-sqbutton-black button-change-password wgt-sqbutton-default tooltipstered']"

        self.manage_guest_profiles =By.XPATH, "//*[@class='tab-type tab-unchanged tab2']"
        self.add_new_guest = By.XPATH,"//*[@class='card bg-white add-guest']"
        self.add_btn = By.XPATH,"//*[@class='add add-btn']"
        self.save_guest = By.XPATH,"//*[@class='wgt-sqbutton-defalut wgt-sqbutton-black save-btn']"
        self.save_guest_btn = By.XPATH,"//*[@class='wgt-sqbutton-black save-btn']"
        self.close_btn = By.XPATH,"//*[@class='wgt-sqbutton-dark cancel-btn']"

        """my point management"""
        self.my_points_management = By.LINK_TEXT,'My Points Management'
        self.redeem_my_rewards_tab = By.XPATH,"//*[@class='tab-type tab2 tab-changed']"
        self.points_available = By.XPATH,"//*[@class='my-span-money']"
        self.points_expiring = By.XPATH,"//*[@class='months-span-money']"
        self.reward_panel = By.XPATH,"//*[@class='redeem-rewards']"

        self.transfer_points_tab = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-update > div.profile-page-tab > a.tab-type.tab-unchanged.tab2 > span'
        self.add_nominee = By.XPATH,"//*[@class='card bg-white add-creditcard nomination-card']"
        self.add_nominee_btn = By.XPATH,"//*[@class='add']"
        self.loyalty_number = By.XPATH,"//input[@name='loyaltyno']"
        self.nominee_email = By.XPATH,"//input[@name='email']"
        self.nominee_firtname = By.XPATH,"//input[@name='firstname']"
        self.nominee_lastname = By.XPATH,"//input[@name='lastname']"
        self.nominee_cancel = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-update > div.tab-content > div > div.transfer-points-content > div > div > div > div.point-rl.main > div.card-view-root > div > div > form > div > div > div.form-buttons > a.wgt-sqbutton-dark'
        self.nominee_nominate = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-update > div.tab-content > div > div.transfer-points-content > div > div > div > div.point-rl.main > div.card-view-root > div > div > form > div > div > div.form-buttons > a.wgt-sqbutton-blue.disabled'

        """my histoty"""
        self.my_hisoty_tab = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > ul > li:nth-child(4) > a'
        self.booking_on_mmhotel = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-update > div.profile-page-tab > a.tab-type.tab4.tab-changed > span'
        self.bookings_on_page = By.XPATH,"//*[@data-view='bookings-on-pages']"
        self.all_bookings = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-update > div.profile-page-tab > a:nth-child(2) > span'
        self.all_bookings_list = By.XPATH,"//*[@class='my-bookings-history history-box']"
        self.my_redeemed_vouchers = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-update > div.profile-page-tab > a:nth-child(3) > span'
        self.point_panel = By.XPATH,"//*[@class='mm2-my-vouchers-points-row']"
        self.other_redemption = By.LINK_TEXT,'Other Redemption'
        self.voucher_list = By.XPATH,"//*[@class='mm2-vouchers-item']"
        self.my_point_history = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-update > div.profile-page-tab > a:nth-child(4) > span'
        self.my_point_history_panel = By.XPATH,"//*[@class='my-bookings-history history-box']"


        """my commnication preferences"""
        self.my_cp = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > ul > li:nth-child(5) > a'
        self.service_commnications = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.page-content.block-profile.col-1120.loading-hide > div > ul.s-region > li.grey-input-wrapper.nomal-style'
        self.market_commnications = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.page-content.block-profile.col-1120.loading-hide > div > ul.m-region > li.grey-input-wrapper.nomal-style'
        self.checkbox_unselect = By.XPATH,"//*[@class='newRadio newCheckbox opt-sel']"
        self.checkbox_select = By.XPATH,"newRadio newCheckbox opt-sel checked"

        """my lifestyle"""
        self.my_lifestyle_tab = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > ul > li:nth-child(6) > a'
        self.my_stay_preference = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.profile-page-tab > a.tab-type.tab-changed.tab3 > span'
        self.my_favourite_destinations = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.profile-page-tab > a:nth-child(2) > span'
        self.my_interests = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.profile-page-tab > a:nth-child(3)'
        self.accessibility = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.page-content.prefer-stay.block.col-1120 > div:nth-child(2) > h5'
        self.near_lift = By.XPATH,"//*[@data-value='Near Lift']"
        self.away_from_lift = By.XPATH,"//*[@data-value='Away from Lift']"
        self.low_floor = By.XPATH,"//*[@data-value='Low Floor']"
        self.high_floor = By.XPATH,"//*[@data-value='High Floor']"
        self.room_preferences = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.page-content.prefer-stay.block.col-1120 > div:nth-child(3) > h5'
        self.smoking_room = By.XPATH,"//*[@data-value='Smoking Room']"
        self.non_smoking = By.XPATH,"//*[@data-value='Non-Smoking Room']"
        self.addtional_information = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.page-content.prefer-stay.block.col-1120 > div:nth-child(4) > h5'
        self.addtional_information_text = By.XPATH,"//*[@placeholder='Share it with us, and we will try our best to fulfill them']"
        self.update_btn = By.XPATH,"//*[@class='wgt-sqbutton-black save']"
        self.tip_content = By.XPATH,"//*[@class='tipContent']"

        self.add_destination = By.XPATH,"//*[@class='newDestination']"
        self.add_destination_btn = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > div > div.profile-manageGuestPro > div.travel-favorite.block.col-1120.page-content.loading-hide > div.select-result > div > div > span'
        self.destination_list = By.XPATH,"//*[@class='t1 down']"

        self.tell_text = By.XPATH,"//*[@class='discription']"
        self.shopping = By.XPATH,"//*[@data-interestid='BCDD1169-45A6-4F3D-B04E-138F48F3BC47']"
        self.food_and_wine = By.XPATH,"//*[@data-interestid='3F2093AD-51DA-4863-9CE9-659ABB44BC55']"
        self.sightseeing = By.XPATH,"//*[@data-interestid='D4FD07AA-A700-4D62-9BD9-05A4E2E52D24']"
        self.active_tours = By.XPATH,"//*[@data-interestid='4BE55166-0633-4D84-BA69-FC6344AE416C']"
        self.family_activities = By.XPATH,"//*[@data-interestid='C4F05806-46A1-43D4-A3DB-3D57BF40F60F']"
        self.entertainment = By.XPATH,"//*[@data-interestid='C5301918-D9FC-459C-B50B-9CBE6A21B3BB']"
        self.sporting_events = By.XPATH,"//*[@data-interestid='60E7F1F3-8AA5-4222-975B-C4E50C90B7BA']"
        self.nightlife = By.XPATH,"//*[@data-interestid='79D464C5-18D0-4E0F-8074-E47CD0C7D804']"

        """my millennium enquiry"""
        self.mm_enquiry_tab = By.CSS_SELECTOR,'body > div.global-wrapper.max-1440.nav-remove-shadow.nav-always-docked > div.main-wrapper > ul > li:nth-child(7) > a'
        self.select_subject = By.XPATH,"//*[@data-bind='type']"
        self.feedback = By.XPATH,"//*[@value='Feedback']"
        self.input_feedback = By.XPATH,"//*[@data-bind='feedback']"
        self.send_enquiry = By.XPATH,"//*[@id='opt-save']"
