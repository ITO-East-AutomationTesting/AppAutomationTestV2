# coding=utf-8
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from untils.base_runner import ParametrizedTestCase
from businessView.loginView import LoginView
from businessView.registerView import RegisterView
from businessView.informatonView import InformationView
from businessView.homeView import HomeView
import random


class Register(ParametrizedTestCase):
    @classmethod
    def setUpClass(cls):
        super(Register, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(Register, cls).tearDownClass()

    def tearDown(self):
        self.loginView.get_screenshot()

    def test_register_by_username_password(self):
        u'''Register by username and password'''
        self.loginView = LoginView(self.driver)
        self.loginView.click_register_button()
        self.registerView = RegisterView(self.driver)

        user_name = 'Terry' + 'FLY' + str(random.randint(100, 500))
        self.registerView.input_username(user_name)

        user_pwd = 'Terry' + str(random.randint(500, 800))
        self.registerView.input_password(user_pwd)

        email = 'Terry' + str(random.randint(1000, 9000)) + '@163.com'
        self.registerView.input_email(email)

        self.registerView.click_register_button()
        informationView = InformationView(self.driver)

        informationView.select_time_by_text('2016')

        informationView.select_school_by_name(u'河北', u'保定学院')

        informationView.select_major_by_text(u'工学', u'计算机科学与技术', u'计算机科学与技术')

        informationView.click_go_kyb_button()

        homeView = HomeView(self.driver)

        self.assertTrue(homeView.home_view_is_loaded, "my self button not display.")

        homeView.add_task_by_template_name()
        homeView.update_start_and_end_time()
        homeView.click_right_button()
        # self.assertEqual('听音乐放松', self.homeView.check_my_task())


if __name__ == '__main__':
    unittest.main()