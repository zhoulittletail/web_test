import time

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class  Common():
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def element_locat(self,locat_type,value):
        el = None
        if locat_type == "css":
            el = self.driver.find_element_by_css_selector(value)
        elif locat_type =="partial_link":
            el = self.driver.find_element_by_partial_link_text(value)
        if el !=None:
            return el
    def element_click(self,locat_type,value):
        self.element_locat(locat_type,value).click()
    def element_input(self,locat_type,value,date):
        self.element_locat(locat_type,value).send_keys(date)
    def element_text(self,locat_type,value):
        return self.element_locat(locat_type,value).text
    def get_img(self,imgpath):
        nowtime=time.strftime("%Y_%m%d %H_%M_%S")
        self.driver.get_screenshot_as_file(imgpath+"%s--%s.jpg"%(nowtime,sys.exc_info()[1]))
