from time import sleep

from  selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册B.html"
driver.get(url)

size = driver.find_element_by_css_selector("#userB").size
print("元素大小为：",size)
text = driver.find_element_by_css_selector("#p1").text
print("元素内容为：",text)
title = driver.title
print("页面标题为：",title)
current_url = driver.current_url
print("当前页面的url为：",current_url)
get_attribute = driver.find_element_by_link_text("B访问 新浪 网站").get_attribute("href")
print("当前页面的页面为：",get_attribute)
is_displayed = driver.find_element_by_css_selector("span").is_displayed()
print("当前属性是否可见：",is_displayed)
is_enabled = driver.find_element_by_css_selector('[value="alert"]').is_enabled()
print("当前元素是否启用：",is_enabled)
driver.quit()
