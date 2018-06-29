from time import sleep

from  selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)
driver.find_element_by_class_name("telA").send_keys("1861111111")
sleep(3)
driver.quit()