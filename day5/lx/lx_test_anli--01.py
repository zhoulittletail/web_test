import sys
from time import sleep

import unittest

import time
from selenium import webdriver
class Iwebshop_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def test_login(self):
        driver = self.driver
        driver.get("http://192.168.178.136/iwebshop/")
        driver.find_element_by_partial_link_text("登录").click()
        driver.find_element_by_css_selector('[name="login_info"]').send_keys("zhouxun")
        driver.find_element_by_css_selector('[name="password"]').send_keys("123456")
        driver.find_element_by_css_selector(".submit_login").click()
        text = driver.find_element_by_css_selector(".loginfo").text
        print("登录信息获取文本为：",text)
        try:
            self.assertIn("admin",text)
        except AssertionError:
            nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
            print("当前时间戳为：",nowtime)
            driver.get_screenshot_as_file("../img/%s__%s.jpg"%(nowtime,sys.exc_info()[1]))
            raise AssertionError
        sleep(3)
    def tearDown(self):
        sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    unittest.main


