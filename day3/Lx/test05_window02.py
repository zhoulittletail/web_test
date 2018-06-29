from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
url=r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)


driver.get(r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册B.html")
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.find_element_by_css_selector("#passwordB").send_keys("123456")
sleep(3)
driver.refresh()
sleep(3)
driver.close()
sleep(4)

driver.quit()