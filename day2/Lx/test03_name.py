# 导包
from time import sleep

from selenium import webdriver
#  实例化浏览器
driver = webdriver.Firefox()
# 打开项目url
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)

# 查找操作元素
driver.find_element_by_name("userA").send_keys("admin")
driver.find_element_by_name("passwordA").send_keys("123456")
# 暂停
sleep(3)
# 退出
driver.quit()