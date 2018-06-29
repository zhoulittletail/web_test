from time import sleep

from  selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册实例.html"
driver.get(url)


# size = driver.find_element_by_css_selector("#password").size
# print(size)
# text = driver.find_element_by_css_selector("#p1").text
# print(text)
# url = driver.current_url
# tit = driver.title
# print(tit)
# print(url)
# dis = driver.find_element_by_css_selector("span").is_displayed()
# print(dis)
# able = driver.find_element_by_css_selector("button").is_enabled()
# print(able)
# get_attribute = driver.find_element_by_link_text("访问 新浪 网站").get_attribute("href")
# print(get_attribute)
aa = driver.find_element_by_xpath("//*[text()='注册B网页']  ").text
print(aa)
bb = driver.find_element_by_xpath("//*[starts-with(@id,'AA')]").text
print(bb)
BB = driver.find_element_by_xpath("//*[starts-with(@id,'fw')]").text
cc = driver.find_element_by_xpath("//*[contains(@id,'AA')]").text
print(cc)
print(BB)
driver.quit()
