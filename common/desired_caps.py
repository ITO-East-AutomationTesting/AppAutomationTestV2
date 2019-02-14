# coding=utf-8
import logging
import logging.config
import os
import sys
import yaml
from appium import webdriver

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from common.kyb_test import KybTest


base_dir = os.path.dirname(os.path.dirname(__file__))
log_file_path = os.path.join(base_dir, 'config/log.conf')
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()


def appium_desired(devices):
    kyb_caps_path = os.path.join(base_dir, 'config/kyb_caps.yaml')
    with open(kyb_caps_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)
    app_path = os.path.join(base_dir, 'app', data['appname'])

    desired_caps = {}

    if str(devices['platformName']).lower() == 'android':
        desired_caps['udid'] = devices['deviceName']
        desired_caps['app'] = devices['app']
    else:
        # others need to add
        pass

    desired_caps['platformVersion'] = devices["platformVersion"]
    desired_caps['platformName'] = devices["platformName"]
    # desired_caps["automationName"] = devices['automationName']
    desired_caps['deviceName'] = devices["deviceName"]
    desired_caps["noReset"] = "False"
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    desired_caps["systemPort"] = devices["systemPort"]

    remote = "http://127.0.0.1:" + str(devices["port"]) + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    driver.implicitly_wait(5)
    k = KybTest(driver)
    k.skip_update_guid()
    return driver