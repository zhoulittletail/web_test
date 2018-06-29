from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)

driver.maximize_window()
driver.implicitly_wait(30)
# 先找到alerta
driver.find_element_by_css_selector("#alerta").click()
# 调出警告框
alert = driver.switch_to.alert
# 获取警告框文本信息
text = alert.text
print(text)
# 警告框进行统一操作
alert.accept()
driver.find_element_by_css_selector("#userA").send_keys("admin")

sleep(3)
driver.quit()