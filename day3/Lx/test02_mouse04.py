from time import sleep

from  selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)
action = ActionChains(driver)
elenment = driver.find_element_by_css_selector("button")
action.move_to_element(elenment).perform()


sleep(3)
driver.quit()