from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)
# 1.填写注册A内信息，用户名:admin;密码123456；电话：18611111111；邮箱：123@qq.com
# 读取出信息，并且判断；
driver.find_element_by_css_selector("#userA").send_keys("admin")
text = driver.find_element_by_css_selector("#userA").text
print(text)
userA = driver.find_element_by_css_selector("#userA").get_attribute("value")
print("用户名输出：",userA)
if userA == "admin":
    print("判断：输出正确！")
else:
    print("bug")

driver.find_element_by_css_selector("#passwordA").send_keys("123456")
passwordA = driver.find_element_by_css_selector("#passwordA").get_attribute("value")
print("密码输出：",passwordA)
if passwordA == "123456":
    print("判断：输出正确！")
else:
    print("bug")

driver.find_element_by_css_selector("#telA").send_keys("18611111111")
telA = driver.find_element_by_css_selector("#telA").get_attribute("value")
print("电话号码输出：",telA)
if telA == "18611111111":
    print("判断：输出正确！")
else:
    print("bug")

driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
emailA = driver.find_element_by_css_selector("#emailA").get_attribute("value")
print("邮箱输出：",emailA)
if emailA  == "123@qq.com":
    print("判断：输出正确！")
else:
    print("bug")

sleep(3)
driver.quit()