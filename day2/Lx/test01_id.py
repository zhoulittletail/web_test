# 导包

from selenium import webdriver
from time import sleep
# 实例化浏览器对象）制定浏览器
driver = webdriver.Firefox()
# 打开项目网页（打开url)
driver.get("file:///C:/Users/23746/Desktop/web自动化环境/课堂素材/注册A.html")
# 查找元素、操作元素
element=driver.find_element_by_id("userA")
element=driver.find_element_by_id("passwordA")
element.send_keys("zlh")
element.send_keys("123456")
# 暂停3秒
sleep(5)
# 关闭浏览器
driver.quit()
