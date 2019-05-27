""" ================================================================================================================
@Description: This module defines the profile functions about dashboard, my account, my points management, my history, my communication, my lifestyle, my millennium enquiry
              Use these function and update if necessary.
@Last Update Date + Update by Whom: 5/20/2019 by Linda
====================================================================================================================="""
import datetime
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from elements.ElementsDefine import ElementsDefine
from functions.common.Common import Common
from functions.common.log import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
from selenium.webdriver.common.action_chains import ActionChains

class Profile(object):
    def __init__(self, driver):      # Initial for the elements
        self.driver = driver
        self.element = ElementsDefine()
        self.common = Common(driver)


    def enter_profile(self):
        """click to enter profile page"""
        WebDriverWait(self.driver ,10).until(EC.presence_of_element_located((self.element.expand_profile)))
        self.driver.find_element(*self.element.expand_profile).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.view_profile)))
        self.driver.find_element(*self.element.view_profile).click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.profile_img)))
            assert u"My Profile" in self.driver.title
            logger.info(self.driver.current_url)
            logger.info("Profile redirected link is right")
            print('enter profile succesfully')
        except Exception as e:
            logger.warning("Profile redirected link is wrong" ,format(e))

    def enter_myaccount(self):
        """enter profile then click my account"""
        self.driver.find_element(*self.element.My_Account).click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.myaccount_tab)))
            logger.info('enter my account ' +self.driver.current_url)
            print('enter my account successfully')
        except Exception as e:
            print(e)
            print('fail to enter my account')
            raise

    def check_profile_dashboard_my_points(self):
        """check profile dashboard-my points"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.profile_img)))
        self.common.is_element_visible((self.element.profile_img))
        logger.info("profile image is displayed")
        self.common.is_element_visible((self.element.profile_welcome))
        name = self.driver.find_element(*self.element.profile_name).text
        logger.info("welcome %s is displayed" % name)
        self.common.is_element_visible((self.element.profile_member_since))
        logger.info("member since is displayed")
        self.common.is_element_visible((self.element.profile_member_num))
        logger.info("member number is displayed")
        self.common.is_element_visible((self.element.print_member_card))
        logger.info("print member card is displayed")
        self.common.is_element_visible((self.element.point_available))
        logger.info("point available is displayed")
        self.common.is_element_visible((self.element.point_progress))
        logger.info("point progress bar is displayed")
        self.common.is_element_visible((self.element.point_expired))
        logger.info("point expiring is displayed")
        self.driver.find_element(*self.element.transfer_points).click()
        time.sleep(2)
        try:
            assert u"Transfer My Points" in self.driver.title
            logger.info(self.driver.current_url)
            logger.info("Transfer points redirected link is right")
            self.driver.back()
            time.sleep(2)
        except Exception as e:
            logger.warning("Transfer points link is wrong" ,format(e))
        self.driver.find_element(*self.element.View_Points_History).click()
        time.sleep(2)
        try:
            assert u"My History" in self.driver.title
            logger.info(self.driver.current_url)
            logger.info("view points history redirected link is right")
            self.driver.back()
            time.sleep(2)
        except Exception as e:
            logger.warning("view points history link is wrong" ,format(e))

        self.driver.find_element(*self.element.discover_rewards).click()
        time.sleep(2)
        try:
            assert u"Redeem My Rewards" in self.driver.title
            logger.info(self.driver.current_url)
            logger.info("discover rewards redirected link is right")
            self.driver.back()
            time.sleep(2)
        except Exception as e:
            logger.warning("discover rewards link is wrong" ,format(e))

    def check_profile_dashboard_earn_points(self):
        """check profile dashboard-earn points"""
        try:
            self.common.is_element_visible((self.element.task_icon))
            logger.info("task icon is displayed")
            self.common.is_element_visible((self.element.task_thumbnail_icon))
            logger.info("task thumbnail icon is displayed")
            self.common.is_element_visible((self.element.task_des))
            logger.info("task description is displayed")
            self.common.is_element_visible((self.element.task_status))
            logger.info("task status is displayed")
        except Exception as e:
            print(e)
            logger.warning('Check earn point fail!')

    def check_reward_section(self):
        """check rewards section"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.redeem_now)))
        self.common.is_element_visible(self.element.redeem_now)
        logger.info('redeem now is displayed')
        self.common.is_element_visible(self.element.reward_list_first)
        logger.info('first reward is displayed')
        self.common.is_element_visible(self.element.reward_img)
        logger.info('reward image is displayed')
        self.common.is_element_visible(self.element.reward_points)
        logger.info('reward point is displayed')
        self.common.is_element_visible(self.element.reward_name)
        logger.info('reward name is displayed')
        self.common.is_element_visible(self.element.redeem_des)
        logger.info('reward description is displayed')
        self.common.is_element_visible(self.element.redeem_view_details)
        logger.info('view details button is displayed')
        self.driver.find_element(*self.element.redeem_view_details).click()
        logger.info('click view details button')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.redeem_overlay_img)))
        try:
            self.common.is_element_visible(self.element.redeem_overlay_img)
            logger.info('reward overlay image is displayed')
            self.common.is_element_visible(self.element.redeem_overlay_name)
            logger.info('reward overlay name is displayed')
            self.common.is_element_visible(self.element.redeem_overlay_des)
            logger.info('reward overlay description is displayed')
            self.common.is_element_visible(self.element.reward_points_overlay)
            logger.info('reward overlay point is displayed')
            self.common.is_element_visible(self.element.redeem_overlay_tac)
            logger.info('reward overlay terms and conditions  is displayed')
            self.common.is_element_visible(self.element.redeem_overlay_redeem)
            logger.info('reward overlay redeem button is displayed')
            self.common.is_element_visible(self.element.redeem_overlay_cancel)
            logger.info('reward overlay cancel is displayed')
            self.common.is_element_visible(self.element.reward_REDEEM)
            logger.info('reward overlay redeem is displayed')
            self.driver.find_element(*self.element.redeem_overlay_close).click()
            logger.info('Click close button in redeem overlay')
            time.sleep(2)
            flag = self.common.is_element_visible(self.element.redeem_view_details)
            if flag:
                logger.info("close redeem overlay successfully")
            else:
                logger.info("close fail")
        except Exception as e:
            print(e)
            logger.warning("check redeem overlay fail")
        global t1, t2
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.reward_required_point)))
        except Exception as e:
            print(e)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.point_available)))
        except Exception as e:
            print(e)
        try:
            reward_required_point = self.driver.find_element(*self.element.reward_required_point)
            # print(reward_required_point)
            # print(type(reward_required_point))
            t1 =int(reward_required_point.text.replace("," ,""))
            print(t1)
        except Exception as e:
            print(e)
        try:
            user_available_point = self.driver.find_element(*self.element.point_available)
            # print(user_available_point)
            # print(type(user_available_point))
            t2 =int(user_available_point.text)
            print(t2)
        except Exception as e:
            print(e)
        if t1 > t2:
            self.common.is_element_visible(self.element.redeem_disable_status)
            logger.info('redeem button is disabled since point is not enough')
        else:
            self.common.is_element_visible(self.element.redeem_active_status)
            logger.info('redeem button is active since point is enough')
            self.driver.find_element(*self.element.redeem_active_status).click()
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.redeem_now_title)))
                assert "Redeem Now" in self.element.redeem_now_title
            except Exception as e:
                print(e)
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.redeem_are_you1)))
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.redeem_are_you2)))
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.REDEEMM_REWARD_btn)))
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.Cancel_btn)))
                logger.info('Redeem now title, description, REDEEM REWARD, Cancel are displayed properly')
            except Exception as e:
                logger.info('Redeem now title, description, REDEEM REWARD, Cancel are not displayed')
                print(e)
        self.common.is_element_visible(self.element.explore_img)
        logger.info('explore image is displayed')
        self.common.is_element_visible(self.element.explore_name)
        logger.info('explore name is displayed')
        self.common.is_element_visible(self.element.explore_des)
        logger.info('explore description is displayed')
        self.common.is_element_visible(self.element.explore_btn)
        logger.info('explore button is displayed')
        self.driver.find_element(*self.element.explore_btn).click()
        logger.info('click explore button')
        time.sleep(3)
        flag3 = self.common.is_element_visible(self.element.catalogue_available)
        if flag3:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.catalogue_available)))
            logger.info('catalogue available popup is displayed')
            self.driver.find_element(*self.element.close_catalogue).click()
            time.sleep(2)
            if flag3:
                logger.info('close catalogue successfully')
            else:
                logger.warning('fail to close catalogue')
        else:
            handle = self.driver.current_window_handle
            print(handle)
            current_title = self.driver.title
            print(current_title)
            allHandles = self.driver.window_handles
            self.driver.switch_to_window(allHandles[-1])
            # print(allHandles)
            # for newhandle in allHandles:
            #     if newhandle!=handle:
            #         self.driver.switch_to_window(newhandle)
            #         newhandle = self.driver.current_window_handle
            #         print(newhandle)
            #         new_title = self.driver.title
            #         print(new_title)
            #         logger.info('switch to new window')
            #     else:
            #         logger.info('already in new window')
            try:
                assert u"My Millennium" in self.driver.title
                logger.info("storefront redirect right")
                self.driver.close()
                allHandles = self.driver.window_handles
                self.driver.switch_to_window(allHandles[-1])
            except Exception as e:
                print(e)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.more_rewards)))
            self.common.is_element_visible(self.element.more_rewards)
            logger.info('more rewards is displayed')
            self.driver.find_element(*self.element.more_rewards).click()
            time.sleep(3)
        except Exception as e:
            print(e)
        if flag3:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.catalogue_available)))
            logger.info('catalogue available popup is displayed')
            self.driver.find_element(*self.element.close_catalogue).click()
            time.sleep(2)
            if flag3:
                logger.info('close catalogue successfully')
            else:
                logger.warning('fail to close catalogue')
        else:
            handle = self.driver.current_window_handle
            print(handle)
            current_title = self.driver.title
            print(current_title)
            allHandles = self.driver.window_handles
            self.driver.switch_to_window(allHandles[-1])
            # print(allHandles)
            # for newhandle in allHandles:
            #     if newhandle != handle:
            #         self.driver.switch_to_window(newhandle)
            #         newhandle = self.driver.current_window_handle
            #         print(newhandle)
            #         new_title = self.driver.title
            #         print(new_title)
            #         logger.info('switch to new window')
            #     else:
            #         logger.info('already in new window')
            try:
                assert u"My Millennium" in self.driver.title
                logger.info("storefront redirect is right")
                self.driver.close()
                allHandles = self.driver.window_handles
                self.driver.switch_to_window(allHandles[-1])
            except Exception as e:
                print(e)
        flag4 = self.common.is_element_visible(self.element.my_vouchers)
        if flag4:
            logger.info('my vouchers is displayed')
            self.driver.find_element(*self.element.my_vouchers).click()
            logger.info('click my vouchers')
            time.sleep(3)
            self.driver.find_element(*self.element.voucher_view_details).click()
            logger.info('click VIEW DETAILS')
            time.sleep(2)
            try:
                self.common.is_element_visible(self.element.redeem_overlay_img)
                logger.info('reward overlay image is displayed')
                self.common.is_element_visible(self.element.redeem_overlay_name)
                logger.info('reward overlay name is displayed')
                self.common.is_element_visible(self.element.redeem_overlay_des)
                logger.info('reward overlay description is displayed')
                self.common.is_element_visible(self.element.reward_points_overlay)
                logger.info('reward overlay point is displayed')
                self.common.is_element_visible(self.element.redeem_overlay_tac)
                logger.info('reward overlay terms and conditions  is displayed')
                logger.info("voucher - view detail works well")
                self.driver.find_element(*self.element.voucher_close).click()
                logger.info("click close button")
                time.sleep(2)
                flag2 = self.common.is_element_visible(self.element.voucher_view_details)
                if flag2:
                    logger.info("close voucher overlay successfully")
                else:
                    logger.info("close fail")
            except Exception as e:
                print(e)
                logger.warning("voucher - view detail fail to close")
            handle = self.driver.current_window_handle
            current_title = self.driver.title
            print(current_title)
            self.driver.find_element(*self.element.view_all_my_vouchers).click()
            logger.info('click view all my vouchers')
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.my_redeemed_vouchers_mark)))
            allHandles = self.driver.window_handles
            self.driver.switch_to_window(allHandles[-1])
            # for newhandle in allHandles:
            #     if newhandle!=handle:
            #         self.driver.switch_to_window(newhandle)
            #         newhandle = self.driver.current_window_handle
            #         print(newhandle)
            #         new_title = self.driver.title
            #         print(new_title)
            #         logger.info('switch to new window')
            #     else:
            #         logger.info('already in new window')
            try:
                assert u"My Redeemed Vouchers" in self.driver.title
                logger.info("my redeemed vouchers redirect right")
                self.driver.close()
                allHandles = self.driver.window_handles
                self.driver.switch_to_window(allHandles[-1])
            except Exception as e:
                print(e)
                logger.warning("my redeemed vouchers redirect fail")
        else:
            logger.info("no redeemed vouchers yet")

    def check_upcoming(self):
        """Check upcoming booking"""
        upcoming = self.common.is_element_visible(self.element.upcoming_bookings)
        if upcoming:
            print("Upcoming booking exist")
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.upcoming_bookings_img)))
            logger.info('booking hotel image is displayed')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.upcoming_bookings_date)))
            logger.info('booking date is displayed')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.upcoming_bookings_name)))
            hotel_name = self.driver.find_element(*self.element.upcoming_bookings_name).text
            logger.info(hotel_name)
            print('Booking hotel is displayed: ' + hotel_name)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.upcoming_bookings_no)))
            booking_num = self.driver.find_element(*self.element.upcoming_bookings_no).text
            logger.info(booking_num)
            print('Booking nunmber is displayed: ' + booking_num)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.upcoming_bookings_roomtype)))
            room_type = self.driver.find_element(*self.element.upcoming_bookings_roomtype).text
            logger.info(room_type)
            print('Booking room type is displayed: %s' + room_type)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.upcoming_bookings_occupancy)))
            occupancy = self.driver.find_element(*self.element.upcoming_bookings_occupancy).text
            logger.info(occupancy)
            print('Booking occupancy is displayed: ' + occupancy)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.upcoming_bookings_rate)))
            rate = self.driver.find_element(*self.element.upcoming_bookings_rate).text
            logger.info(rate)
            print('Booking rate is displayed: ' + rate)
        else:
            print('No upcoming bookings')

    def check_mm_bottom(self):
        """Check bottom section"""
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.bottom_section)))
            logger.info('Bottom section exist')
            print('bottom section is configured')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.bottom_section_left_img)))
            logger.info('Bottom section left image exist')
            print('bottom section left image is configured')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.bottom_section_left_des)))
            logger.info('Bottom section left description exist')
            print('bottom section left description is configured')
        except:
            logger.info('no bottom section available')
            print('bottom section is not configured')
            raise
        try:
            WebDriverWait(self.driver, 10).until \
                (EC.presence_of_element_located((self.element.bottom_section_right_container)))
            logger.info('bottom section right exists')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.bottom_section_right_title)))
            logger.info('bottom right title is displayed')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.bottom_section_right_des)))
            logger.info('bottom right des is displayed')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.bottom_section_view_now_btn)))
            logger.info('bottom right button is displayed')
            self.driver.find_element(*self.element.bottom_section_view_now_btn).click()
            WebDriverWait(self.driver, 10).until \
                (EC.presence_of_element_located((self.element.Frequently_Asked_Questions_link)))
            assert u"Frequently Asked Questions" in self.driver.title
            logger.info("view now button redirect is right")
            print(self.driver.current_url)
            self.driver.back()
        except:
            logger.info('bottom right section is not configured')
            print('bottom right section is not configured')
            raise

    def update_myaccount(self):
        """check update my profile"""
        with open("../data/profile_data_list.json") as f:
        # with open("C:\\MLP\\Automation\\Project\\data\\profile_data_list.json") as f:
            json_data = f.read()
            json_to_python = json.loads(json_data)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_img)))
            self.common.is_element_visible(self.element.update_img)
            logger.info('found profile image')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_change_pic)))
            self.driver.find_element(*self.element.update_change_pic).click()
            logger.info('click change picture')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.picture_list)))
            self.driver.find_element(*self.element.profile_1st).click()
            logger.info('click 1st default image')
            # WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((self.element.update_title)))
            self.common.is_element_visible(self.element.update_title)
            time.sleep(2)
            self.driver.find_element(*self.element.update_title).click()
            logger.info('click to select tilte')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_title_select)))
            self.driver.find_element(*self.element.update_title_select).click()
            logger.info('select title')
            assert u'Mrs' in self.driver.find_element(*self.element.update_title).text
            print('update title successfully')
            assert u'Female' in self.driver.find_element(*self.element.update_gender).text
            print('update gender successfully')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_firtname)))
            self.driver.find_element(*self.element.update_firtname).clear()
            self.driver.find_element(*self.element.update_firtname).send_keys(json_to_python['first_name'])
            print('update first name')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_lastname)))
            self.driver.find_element(*self.element.update_lastname).clear()
            self.driver.find_element(*self.element.update_lastname).send_keys(json_to_python['last_name'])
            print('update last name')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_phone)))
            self.driver.find_element(*self.element.update_phone).clear()
            self.driver.find_element(*self.element.update_phone).send_keys(json_to_python['phone'])
            print('update phone')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_mobilephone)))
            self.driver.find_element(*self.element.update_mobilephone).clear()
            self.driver.find_element(*self.element.update_mobilephone).send_keys(json_to_python['mobilephone'])
            print('update mobile phone')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_birth_year)))
            print('check birth year')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_birth_month)))
            print('check birth month')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_birth_day)))
            print('check birth day')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_country)))
            self.driver.find_element(*self.element.update_country).click()
            logger.info('click to select country')
            self.driver.find_element(*self.element.select_country).click()
            logger.info('select country')
            print('update country successfully')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_address)))
            self.driver.find_element(*self.element.update_address).clear()
            self.driver.find_element(*self.element.update_address).send_keys(json_to_python['address'])
            print('update address')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_city)))
            self.driver.find_element(*self.element.update_city).clear()
            self.driver.find_element(*self.element.update_city).send_keys(json_to_python['city'])
            print('update city')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_state)))
            self.driver.find_element(*self.element.update_state).click()
            logger.info('click to select state')
            self.driver.find_element(*self.element.select_state).click()
            logger.info('select state')
            print('update state successfully')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_zip)))
            self.driver.find_element(*self.element.update_zip).clear()
            self.driver.find_element(*self.element.update_zip).send_keys(json_to_python['postal'])
            print('update postal successfully')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_date_format)))
            self.driver.find_element(*self.element.update_date_format).click()
            logger.info('click to select date format')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.select_date_format)))
            self.driver.find_element(*self.element.select_date_format).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_my_profile_btn)))
            self.driver.find_element(*self.element.update_my_profile_btn).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_success_note)))
            logger.info('select date format')
            print('update date format successfully')
        except Exception as e:
            print(e)
            print('update my account file fail')
            raise

    def change_my_password(self):
        """check change my password"""
        cmp = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.change_my_password)))
        # cmp = self.common.is_element_visible(self.element.current_password)
        if not cmp:
            self.driver.find_element(*self.element.change_my_password).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.current_password)))
            print('enter change my password successfully')
            logger.info('enter change my password page')
            try:
                self.common.is_element_visible(self.element.current_password)
                print('current password is available to input')
                self.common.is_element_visible(self.element.new_password)
                print('new password is available to input')
                self.common.is_element_visible(self.element.confirm_password)
                print('confirm password is available to input')
                self.common.is_element_visible(self.element.update_password_btn)
                print('update password button is displayed')
            except Exception as e:
                print(e)
                print('fail to enter change my password page')
                raise
        else:
            print('no change my password page')


    def manage_guest_profiles(self):
        """check manage guest profiles page"""
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.manage_guest_profiles)))
        self.driver.find_element(*self.element.manage_guest_profiles).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.add_new_guest)))
        print('enter manage profile successfully')
        logger.info('enter manage profile page')
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.add_btn)))
            # self.common.is_element_visible(self.element.add_btn)
            self.driver.find_element(*self.element.add_btn).click()
            self.common.is_element_visible(self.element.save_guest)
            self.common.is_element_visible(self.element.close_btn)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.close_btn)))
            logger.info('enter add new guest successfully')
        except Exception as e:
            print(e)
            logger.info('fail to enter add new guest page')
        with open("C:\\MLP\\Automation\\Project\\data\\profile_data_list.json") as f:
            json_data = f.read()
            json_to_python = json.loads(json_data)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_change_pic)))
            self.driver.find_element(*self.element.update_change_pic).click()
            logger.info('click change picture')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.picture_list)))
            self.driver.find_element(*self.element.profile_1st).click()
            logger.info('click 1st default image')
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.element.update_title)))
            self.common.is_element_visible(self.element.update_title)
            time.sleep(2)
            self.driver.find_element(*self.element.update_title).click()
            logger.info('click to select tilte')
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_title_select)))
            self.driver.find_element(*self.element.update_title_select).click()
            logger.info('select title')
            assert u'Mrs' in self.driver.find_element(*self.element.update_title).text
            print('update title successfully')
            # assert u'Female' in self.driver.find_element(*self.element.update_gender).text
            # print('update gender successfully')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_firtname)))
            self.driver.find_element(*self.element.update_firtname).clear()
            self.driver.find_element(*self.element.update_firtname).send_keys(json_to_python['first_name'])
            print('input first name')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_lastname)))
            self.driver.find_element(*self.element.update_lastname).clear()
            self.driver.find_element(*self.element.update_lastname).send_keys(json_to_python['last_name'])
            print('input last name')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_phone)))
            self.driver.find_element(*self.element.update_phone).clear()
            self.driver.find_element(*self.element.update_phone).send_keys(json_to_python['phone'])
            print('input phone')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_mobilephone)))
            self.driver.find_element(*self.element.update_mobilephone).clear()
            self.driver.find_element(*self.element.update_mobilephone).send_keys(json_to_python['mobilephone'])
            print('input mobile phone')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_birth_year)))
            self.driver.find_element(*self.element.select_year).click()
            print('select birth year')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_birth_month)))
            print('check birth month')
            self.driver.find_element(*self.element.select_month).click()
            print('select birth month')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_birth_day)))
            self.driver.find_element(*self.element.select_day).click()
            print('select birth day')
            self.driver.find_element(*self.element.email_address).send_keys(json_to_python['email'])
            print('add guest email address: addguest123@mailinator.com')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_country)))
            self.driver.find_element(*self.element.update_country).click()
            logger.info('click to select country')
            self.driver.find_element(*self.element.select_country).click()
            logger.info('select country')
            print('update country successfully')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_address)))
            self.driver.find_element(*self.element.update_address).clear()
            self.driver.find_element(*self.element.update_address).send_keys(json_to_python['address'])
            print('update address')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.update_city)))
            self.driver.find_element(*self.element.update_city).clear()
            self.driver.find_element(*self.element.update_city).send_keys(json_to_python['city'])
            print('update city')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.guest_state)))
            self.driver.find_element(*self.element.guest_state).click()
            logger.info('click to select state')
            self.driver.find_element(*self.element.select_state).click()
            logger.info('select state')
            print('add state successfully')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.guest_zip)))
            self.driver.find_element(*self.element.guest_zip).clear()
            self.driver.find_element(*self.element.guest_zip).send_keys(json_to_python['postal'])
            print('add postal successfully')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.save_guest_btn)))
            self.driver.find_element(*self.element.save_guest_btn).click()
            # self.driver.find_element(*self.element.close_btn).click()
            print('add guest successfully')
            logger.info('click add/close guest')
            js = "var action=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
            time.sleep(2)
            self.driver.find_element(*self.element.select_self).click()
            logger.info('switch to self')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.remove_guest)))
            self.driver.find_element(*self.element.remove_guest).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.remove_btn)))
            self.driver.find_element(*self.element.remove_btn).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.remove_tip)))
            logger.info('remove guest successfully')
        except Exception as e:
            print(e)
            print('fail to add/close guest')
            raise


    def enter_mypointmanagement(self):
        """check my points management"""
        self.driver.find_element(*self.element.my_points_management).click()
        print('enter my points management page')
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.redeem_my_rewards_tab)))
            print('check redeem my rewards tab')
            pa = self.driver.find_element(*self.element.points_available).text
            print(pa)
            print('check point available')
            px = self.driver.find_element(*self.element.points_expiring).text
            print(px)
            print('check point expiring')
            self.common.is_element_visible(self.element.reward_panel)
            print('reward list is displayed')
        except Exception as e:
            print(e)
            print('check redeem my reward: fail')
            raise
        try:
            self.driver.find_element(*self.element.transfer_points_tab).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.add_nominee)))
            # self.common.is_element_visible(self.element.add_nominee)
            print('enter transfer my points page successfully')
            pa = self.driver.find_element(*self.element.points_available).text
            print(pa)
            print('check point available')
            px = self.driver.find_element(*self.element.points_expiring).text
            print(px)
            print('check point expiring')
            self.common.is_element_visible(self.element.add_nominee)
            print('addnominee is displayed')
            self.driver.find_element(*self.element.add_nominee_btn).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.loyalty_number)))
            self.common.is_element_visible(self.element.nominee_email)
            self.common.is_element_visible(self.element.nominee_firtname)
            self.common.is_element_visible(self.element.nominee_lastname)
            self.common.is_element_visible(self.element.nominee_cancel)
            self.common.is_element_visible(self.element.nominee_nominate)
            self.driver.find_element(*self.element.nominee_cancel).click()
            print('complete check transfter')
        except Exception as e:
            print(e)
            print('fail to check transfer')
            raise


    def enter_my_history(self):
        """check my history page"""
        self.driver.find_element(*self.element.my_hisoty_tab).click()
        print('enter my history page')
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.booking_on_mmhotel)))
            print('check redeem my rewards tab')
            self.common.is_element_visible(self.element.bookings_on_page)
            print('booking on mllenniumhotels.com is displayed')
            self.driver.find_element(*self.element.all_bookings).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.all_bookings_list)))
            print('all bookings list is displayed')
            self.driver.find_element(*self.element.my_redeemed_vouchers).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.point_panel)))
        except Exception as e:
            print(e)
            logger.info('fail to check bookings on millenniumhotels.com, all bookings, my redeemed vouchers')
            raise
        self.driver.find_element(*self.element.other_redemption).click()
        logger.info('click other redemption')
        allHandles = self.driver.window_handles
        self.driver.switch_to_window(allHandles[-1])
        try:
            assert u"My Millennium" in self.driver.title
            logger.info("my millennium-my orders redirect right")
            self.driver.close()
            allHandles = self.driver.window_handles
            self.driver.switch_to_window(allHandles[-1])
            print('my redeemed vouchers test pass')
        except Exception as e:
            print(e)
            logger('redirect fail')
            raise
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.my_point_history)))
            self.common.is_element_visible(self.element.my_point_history)
            self.driver.find_element(*self.element.my_point_history).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.my_point_history_panel)))
            self.common.is_element_visible(self.element.my_point_history_panel)
            print('my point history test pass')
        except Exception as e:
            print(e)
            logger.info('fail to check my point history')
            raise

    def enter_my_cp(self):
        """check my communication"""
        self.driver.find_element(*self.element.my_cp).click()
        print('enter my communications preferences')
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.service_commnications)))
            self.common.is_element_visible(self.element.service_commnications)
            print('service communications is displayed')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.market_commnications)))
            self.common.is_element_visible(self.element.market_commnications)
            print('market communications is displayed')
        except Exception as e:
            print(e)
            logger.info('fail to check service/market communications')
            raise
        checkboxes = self.driver.find_elements_by_tag_name("i")
        print(len(checkboxes))
        for checkbox in checkboxes:
            if checkbox.get_attribute('class') == 'newRadio newCheckbox opt-sel':
                checkbox.click()
                print('mark checkbox: %s' % checkbox)
                time.sleep(2)
        print('select all options')
        for checkbox in checkboxes:
            if checkbox.get_attribute('class') == 'newRadio newCheckbox opt-sel checked':
                checkbox.click()
                print('mark checkbox: %s' % checkbox)
                time.sleep(2)
        print('unselect all options')


    def enter_my_lifestyle(self):
        """check my lifestyle"""
        self.driver.find_element(*self.element.my_lifestyle_tab).click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.my_stay_preference)))
            print('enter my lifestyle')
        except Exception as e:
            print(e)
            print('fail to enter my lifestyle')

    def my_stay_preference(self):
        try:
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.my_stay_preference)))
            print('my stay preference is displayed')
            self.common.is_element_visible(self.element.accessibility)
            self.common.is_element_visible(self.element.near_lift)
            self.common.is_element_visible(self.element.away_from_lift)
            self.common.is_element_visible(self.element.low_floor)
            self.common.is_element_visible(self.element.high_floor)
            self.common.is_element_visible(self.element.room_preferences)
            self.common.is_element_visible(self.element.smoking_room)
            self.common.is_element_visible(self.element.non_smoking)
            self.common.is_element_visible(self.element.addtional_information)
            accessibility_list = self.driver.find_elements_by_tag_name('h6')
            print(len(accessibility_list))
            for accessibility in accessibility_list:
                if accessibility.get_attribute('class') == 'short':
                    accessibility.click()
                    print('select %s' % accessibility)
                    time.sleep(2)
            self.driver.find_element(*self.element.addtional_information_text).clear()
            self.driver.find_element(*self.element.addtional_information_text).send_keys('test message')
            self.driver.find_element(*self.element.update_btn).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((self.element.tip_content)))
            print('my stay preference test pass')
            time.sleep(2)
        except Exception as e:
            print(e)
            print('fail to enter my stay preference')
            raise


    def my_favourite_destination(self):
        """check my favourite destination"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.my_favourite_destinations)))
        self.driver.find_element(*self.element.my_favourite_destinations).click()
        print('enter my favourite destination')
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.add_destination)))
            print('my favourite destination is displayed')
            self.driver.find_element(*self.element.add_destination_btn).click()
            des_list = self.driver.find_elements_by_tag_name('li')
            print(des_list)
            for des in des_list:
                if des.get_attribute('class') == 'region':
                    des.click()
                    des_name = des.text
                    print('select ' + des_name)
                    time.sleep(1)
            print('all regions can be expanded and selected')
            js = "var action=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
            time.sleep(2)
        except Exception as e:
            print(e)
            print('test my favourite destination fail')
            raise

    def my_interests(self):
        """check my interest"""
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.my_interests)))
            self.driver.find_element(*self.element.my_interests).click()
            print('enter my interest')
        except Exception as e:
            print(e)
            print('fail to click my interest')
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.tell_text)))
            self.common.is_element_visible(self.element.shopping)
            self.common.is_element_visible(self.element.food_and_wine)
            self.common.is_element_visible(self.element.sightseeing)
            self.common.is_element_visible(self.element.active_tours)
            self.common.is_element_visible(self.element.family_activities)
            self.common.is_element_visible(self.element.entertainment)
            self.common.is_element_visible(self.element.sporting_events)
            self.common.is_element_visible(self.element.nightlife)
            interest_list = self.driver.find_elements_by_tag_name('h6')
            for i in range(0,8):
                i_text = interest_list[i].text
                print('Found interest:',i_text)
                time.sleep(1)
            print('my interest test pass')
        except Exception as e:
            print(e)
            print('fail to test my interest')
            raise

    def enter_my_millennium_enquiry(self):
        """check my millennium enquiry"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.mm_enquiry_tab)))
        self.driver.find_element(*self.element.mm_enquiry_tab).click()
        print('enter my millennium enquiry')
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.select_subject)))
            self.driver.find_element(*self.element.select_subject).click()
            logger.info('click to select subject')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.feedback)))
            self.driver.find_element(*self.element.feedback).click()
            logger.info('select feedback')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.element.input_feedback)))
            self.driver.find_element(*self.element.input_feedback).send_keys('test')
            logger.info('input message')
            # self.driver.find_element(*self.element.send_enquiry).click()
            print('my interest test pass')
        except Exception as e:
            print(e)
            print('fail to test my interest')
            raise






















