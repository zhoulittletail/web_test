from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册实例.html"
driver.get(url)
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("admin")
driver.find_element_by_css_selector("#tel").send_keys("186123")
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

driver.switch_to.frame("myframe1")
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("admin")
driver.find_element_by_css_selector("#telA").send_keys("186123")
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
driver.switch_to.default_content()
driver.switch_to.frame("myframe2")
driver.find_element_by_css_selector("#userB").send_keys("admin")
driver.find_element_by_css_selector("#passwordB").send_keys("admin")
driver.find_element_by_css_selector("#telB").send_keys("186123")
driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")
sleep( 3)
driver.quit()