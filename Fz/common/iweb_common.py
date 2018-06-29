# 0.init （初始化：实例化浏览器、最大化浏览器、隐式等待）
# 1.定位封装方法（目的：给接下来要定位的方法使用）
# 2.定位方法_点击
# 3.定位方法_输入
# 4.定位方法_获取文本
# 5.定位方法_截图
import time

import sys
from selenium import webdriver
class Common():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def element_locat(self,locat_type,value):
        el = None
        if locat_type == "css":
            el = self.driver.find_element_by_css_selector(value)
        elif locat_type == "partial_link":
            el = self.driver.find_element_by_partial_link_text(value)
        if el != None:
            return el
    def element_click(self,locat_type,value):
        self.element_locat(locat_type,value).click()
    def element_input(self,locat_type,value,data):
        self.element_locat(locat_type,value).send_keys(data)
    def element_text(self,locat_type,value):
        return self.element_locat(locat_type,value).text
    def get_img(self,imgpath):
        nowtime=time.strftime("%Y_%m_%d %H_%M_%S")
        self.driver.get_screenshot_as_file(imgpath+"%s--%s.jpg"%(nowtime,sys.exc_info()[1]))