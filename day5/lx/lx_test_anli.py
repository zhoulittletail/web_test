import unittest
import sys
import time
from time import sleep

from selenium import webdriver
class Iweb_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_iweb_login(self):

        driver = self.driver
        driver.get("http://192.168.178.136/iwebshop/")
        driver.find_element_by_partial_link_text("登录").click()
        driver.find_element_by_css_selector('[name="login_info"]').send_keys("zhangziyi")
        driver.find_element_by_css_selector('[name="password"]').send_keys("123456")
        driver.find_element_by_css_selector(".submit_login").click()
        text = driver.find_element_by_css_selector(".loginfo").text
        print("登陆信息文本信息为：",text)
        try:
            self.assertIn("admin",text)
        except AssertionError:
            nowtime = time.strftime("%Y_%m_%d _%H_%M_%S")
            print("当前时间为：",nowtime)
            driver.get_screenshot_as_file("../img/%s--%s.jpg"%(nowtime,sys.exc_info()[1]))
            print(sys.exc_info())
            raise AssertionError

        sleep(3)
        driver.find_element_by_css_selector(".reg").click()
    def tearDown(self):
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main
