# 导包
from time import sleep

from selenium import webdriver
# 实例化浏览器
driver = webdriver.Firefox()
# 打开项目页面url
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)
# driver.get("file:///C:/Users/23746/Desktop/web%E8%87%AA%E5%8A%A8%E5%8C%96%E7%8E%AF%E5%A2%83/%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html")
# 查找元素、操作
driver.find_element_by_id("userA").send_keys("zlh")
driver.find_element_by_id("passwordA").send_keys("123456")
# 暂停三秒
sleep(3)
# 关闭
driver.quit()