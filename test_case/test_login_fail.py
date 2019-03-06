# coding=utf-8
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from untils.base_runner import ParametrizedTestCase
from businessView.loginView import LoginView


class LoginFail(ParametrizedTestCase):
    @classmethod
    def setUpClass(cls):
        super(LoginFail, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginFail, cls).tearDownClass()

    def tearDown(self):
        self.loginView.get_screenshot()

    def test_login_failed(self):
        u'''use incorrect username and password'''
        self.loginView = LoginView(self.driver)
        self.loginView.input_username(u'测试')
        self.loginView.input_password(u'asdasdasdsd')
        self.loginView.click_login_button()
        self.assertEquals('a', 'b')


if __name__ == '__main__':
    unittest.main()
