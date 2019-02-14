# coding=utf-8
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from untils.base_runner import ParametrizedTestCase
from businessView.homeView import HomeView
from businessView.loginView import LoginView


class Login(ParametrizedTestCase):
    @classmethod
    def setUpClass(cls):
        super(Login, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(Login, cls).tearDownClass()

    def tearDown(self):
        self.loginView.get_screenshot()

    def test_login_by_username_password(self):
        u'''Login in by correct username and password'''
        self.loginView = LoginView(self.driver)
        self.loginView.input_username("TerryFLY300")
        self.loginView.input_password("Terry300")
        self.loginView.click_login_button()

        self.homeView = HomeView(self.driver)
        self.homeView.add_task_by_template_name()
        self.homeView.update_start_and_end_time()
        self.homeView.click_right_button()
        self.assertEqual('听音乐放松', self.homeView.check_my_task())


if __name__ == '__main__':
    unittest.main()