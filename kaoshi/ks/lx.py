# 需求：对iweb_shop项目进行前台登录设计脚本
# 要求：
# 1.	使用unittest框架
# 2.	使用Fixture(setup、tearDown)
# 3.	浏览器最大化、隐式等待30秒
# 4.	使用断言判断登录用户是否为admin，不是则截屏保存图片
# 5.	图片命名格式为脚本执行时间
# 6.	暂停2秒退出、暂停2秒关闭浏览器
# 7.	元素定位方式不限
import unittest
from time import sleep

import time
from selenium import webdriver
import sys
class Iwebshop_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def test_login(self):
        driver = self.driver
        driver.get("http://192.168.178.136/iwebshop/")
        driver.find_element_by_partial_link_text("登录").click()
        driver.find_element_by_css_selector('[name="login_info"]').send_keys("zhangziyi")
        driver.find_element_by_css_selector('[name="password"]').send_keys("123456")
        driver.find_element_by_css_selector(".submit_login").click()
        text = driver.find_element_by_css_selector(".loginfo").text
        print("登陆信息文本为：",text)
        try:
            self.assertIn("admin",text)
        except AssertionError:
            nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
            print("当前时间为：",nowtime)
            print("sys信息为：",sys.exc_info())
            driver.get_screenshot_as_file("../img/%s--%s.jpg"%(nowtime,sys.exc_info()[1]))
            raise  AssertionError
        sleep(2)
        driver.find_element_by_css_selector(".reg").click()
    def tearDown(self):
        sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()