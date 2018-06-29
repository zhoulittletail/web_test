from time import sleep

from  selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\drop.html"
driver.get(url)
action = ActionChains(driver)
source = driver.find_element_by_id("div1")
target = driver.find_element_by_id("div2")
action.drag_and_drop(source,target).perform()  #  第一种拖拽方式
action.drag_and_drop_by_offset(source,200,400).perform()  # 第二种拖拽方式


sleep(3)
driver.quit()