from time import sleep

from  selenium import  webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)

# 需求：
#     1. 通过脚本执行输入 用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com;
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector("#telA").send_keys("18611111111")
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")

#     2. 间隔3秒后，修改电话号码为：18600000000
sleep(3)
driver.find_element_by_css_selector("#telA").clear()
driver.find_element_by_css_selector("#telA").send_keys("18600000000")
#     3. 间隔3秒，点击注册用户A
sleep(3)
driver.find_element_by_css_selector("button").click()
#     4. 间隔3秒，关闭浏览器
sleep(3)
driver.quit()
#     5. 元素定位方法不限