# coding=utf-8
import sys
import platform
import random
import time
import unittest
import HTMLTestRunnerCN
from datetime import datetime
from multiprocessing import Pool

from test_case.test_case_demo import DemoTest
from untils.android_debug_bridge import AndroidDebugBridge
from untils.base_runner import ParametrizedTestCase
from untils.multi_appium_server import AppiumServer
from untils.phone_information import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

base_dir = os.path.dirname(os.path.realpath(__file__))
test_cases_path = os.path.join(base_dir, 'test_case')


def runner_pool(devices):
    devices_pool = []

    for i in range(0, len(devices)):
        _initApp = {}
        _initApp["deviceName"] = devices[i]["devices"]
        _initApp["platformVersion"] = get_phone_info(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = devices[i]["port"]
        # _initApp["automationName"] = "uiautomator2"
        _initApp["systemPort"] = devices[i]["systemPort"]

        _initApp["app"] = devices[i]["app"]
        # apkInfo = ApkInfo(_initApp["app"])
        _initApp["appPackage"] = "com.tal.kaoyan"
        _initApp["appActivity"] = "com.tal.kaoyan.ui.activity.SplashActivity"
        devices_pool.append(_initApp)

    pool = Pool(len(devices_pool))
    pool.map(runner_case_app, devices_pool)
    pool.close()
    pool.join()


def runner_case_app(devices):
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(DemoTest, param=devices))
    # unittest.TextTestRunner(verbosity=2).run(suite)
    now = time.strftime('%Y%m%d%H%M%S')
    reportFile = "test_report_" + now + ".html"
    reportFilePath = os.path.join(base_dir, 'reports', reportFile)
    fp = open(reportFilePath, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='UI Automation Test Report', tester='Terry')
    runner.run(suite)
    fp.close()


if __name__ == '__main__':
    devices = AndroidDebugBridge().attached_devices()

    if len(devices) > 0:
        l_devices = []
        for device in devices:
            app = {}
            app['devices'] = device
            app["port"] = str(random.randint(4700, 4900))
            app["bport"] = str(random.randint(4700, 4900))
            app["systemPort"] = str(random.randint(4700, 4900))
            app["app"] = base_dir + "/app/kaoyan3.1.0.apk"
            l_devices.append(app)

        appium_server = AppiumServer(l_devices)
        appium_server.start_server()
        runner_pool(l_devices)

        appium_server.stop_server(l_devices)
    else:
        print("No devices.")