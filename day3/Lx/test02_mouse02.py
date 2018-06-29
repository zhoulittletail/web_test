from time import sleep

from  selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)

action = ActionChains(driver)
element = driver.find_element_by_css_selector("#userA")
element.send_keys("aaa")
sleep(2)
action.double_click(element).perform()
sleep(3)
driver.quit()