from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
url=r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)

driver.maximize_window()
sleep(3)
driver.set_window_size(1200,600)
sleep(3)
driver.set_window_position(100,120)
sleep(3)
driver.quit()