from time import sleep

from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)

# Keys()
driver.find_element_by_css_selector("#userA").send_keys("admin1")
sleep(2)
driver.find_element_by_css_selector("#userA").send_keys(Keys.BACK_SPACE)
sleep(2)
driver.find_element_by_css_selector("#userA").send_keys(Keys.CONTROL,"a")
driver.find_element_by_css_selector("#userA").send_keys(Keys.CONTROL,"c")
sleep(2)
driver.find_element_by_css_selector("#passwordA").send_keys(Keys.CONTROL,"v")
sleep(2)



driver.quit()
