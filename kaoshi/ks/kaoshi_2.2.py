# 需求：对《注册实例.html》进行信息注册
# 账号：admin,密码：123456，电话：18600000000，电子邮件：123@qq.com
# 要求：
# 1.	对注册《主界面、注册A、注册B》三个注册信息进行注册信息填写
# 2.	定位方式不限
# 3.	暂停3秒钟关闭浏览器
from time import sleep

import selenium
from selenium import webdriver
driver = webdriver.Firefox()
url=r"file:///C:/Web%E8%87%AA%E5%8A%A8%E5%8C%96%E9%98%B6%E6%AE%B5%E8%80%83%E8%AF%95/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
driver.get(url)
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("123456")
driver.find_element_by_css_selector("#tel").send_keys("18600000000")
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")
driver.switch_to.frame('myframe1')
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector("#telA").send_keys("18600000000")
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
driver.switch_to.default_content()
driver.switch_to.frame('myframe2')
driver.find_element_by_css_selector("#userB").send_keys("admin")
driver.find_element_by_css_selector("#passwordB").send_keys("123456")
driver.find_element_by_css_selector("#telB").send_keys("18600000000")
driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")
sleep(3)
driver.quit()