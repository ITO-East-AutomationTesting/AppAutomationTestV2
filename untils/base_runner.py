# coding=utf-8
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from common.desired_caps import appium_desired


class ParametrizedTestCase(unittest.TestCase):
    """
        TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName=methodName)
        global devices
        devices = param

    @classmethod
    def setUpClass(cls):
        cls.driver = appium_desired(devices=devices)
        cls.devicesName = devices['deviceName']

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        pass

    @staticmethod
    def parametrize(test_case_class, param=None):
        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(test_case_class)
        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(test_case_class(name, param=param))
        return suite
