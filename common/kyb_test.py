# coding=utf-8
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class KybTest(object):
    cancelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    confimBtn = (By.XPATH, "//*[@text='确认']")

    def __init__(self, driver):
        self.driver = driver

    def check_cancel_button(self):
        print('========Check Cancel Button========')
        try:
            cancel_button = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            print('No cancel button')
        else:
            cancel_button.click()

    def check_skip_button(self):
        print('========Check Skip Button========')
        try:
            skip_button = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            print('No skip button')
        else:
            skip_button.click()

    def skip_update_guid(self):
        self.check_cancel_button()
        time.sleep(2)
        self.check_skip_button()