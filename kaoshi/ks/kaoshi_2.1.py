#  需求：对《注册A.html》进行信息注册
# 账号：admin,密码：123456，电话：18600000000，电子邮件：123@qq.com
# 要求：
# 1.	定位方式统一使用CSS定位
# 2.	暂停2秒钟点击注册用户A按钮
# 3.	暂停3秒钟后关闭浏览器
from time import sleep

import selenium
from selenium import webdriver
driver = webdriver.Firefox()
url=r"file:///C:/Web%E8%87%AA%E5%8A%A8%E5%8C%96%E9%98%B6%E6%AE%B5%E8%80%83%E8%AF%95/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector("#telA").send_keys("18600000000")
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
sleep(2)
driver.find_element_by_css_selector("button").click()
sleep(3)
driver.quit()
