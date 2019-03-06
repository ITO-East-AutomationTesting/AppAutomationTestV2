# coding=utf-8
from appium import webdriver
import os
import sys

from untils.base_runner import ParametrizedTestCase
from businessView.loginView import LoginView


class DemoTest(ParametrizedTestCase):
    @classmethod
    def setUpClass(cls):
        super(DemoTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(DemoTest, cls).tearDownClass()

    def tearDown(self):
        self.loginView.get_screenshot()

    def testFirstOpen(self):
        u'''Login in by correct username and password'''
        self.loginView = LoginView(self.driver)
        self.loginView.input_username("TerryFLY300")
        self.loginView.input_password("Terry300")
