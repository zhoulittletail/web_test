# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Firefox()
# url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
# driver.get(url)
#
# driver.maximize_window()
# driver.implicitly_wait(30)
#
# element = driver.find_element_by_css_selector("select")
# """
# 通过下标查找
# Select(element).select_by_index(1)
# sleep(2)
# Select(element).select_by_index(3)
# sleep(2)
# Select(element).select_by_index(2)
# """
# """
# 通过value值来查找  # 注意只需要填写value的值就可以了
# Select(element).select_by_value("sh")
# sleep(2)
# Select(element).select_by_value("cq")
# sleep(2)
# Select(element).select_by_value("gz")
# """
#
# """
# 通过select_by_visible_text显示的文本来查找
# Select(element).select_by_visible_text("A上海")
# sleep(2)
# Select(element).select_by_visible_text("A重庆")
# sleep(2)
# Select(element).select_by_visible_text("A广州")
# """
#
# #  通过CSS来查找
# # driver.find_element_by_css_selector('[value="sh"]').click()
# # sleep(2)
# # driver.find_element_by_css_selector('[value="cq"]').click()
# # sleep(2)
# # driver.find_element_by_css_selector('[value="gz"]').click()
#
# # 通过tag_name来查找
# # element = driver.find_elements_by_tag_name("option")
# # for option in element:
# #     if option.text == "A重庆":
# #         sleep(2)
# #         option.click()
# # for option in element:
# #     if option.text == "A上海":
# #         sleep(2)
# #         option.click()
# #
# # for option in element:
# #     if option.text == "A广州":
# #         sleep(2)
# #         option.click()
#
# sleep(3)
# driver.quit()

from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

"""
通过tag_name来查找option得到的是一组option，然后通过获取option的文字来跟网页打开之后显示的文字进行核对，相同就执行一个点击==选中操作
elenment = driver.find_elements_by_tag_name("option")
for option in elenment :
    if option.text =="A上海":
        sleep(2)
        option.click()
for option in elenment :
    if option.text =="A重庆":
        sleep(2)
        option.click()
for option in elenment :
    if option.text =="A广州":
        sleep(2)
        option.click()
"""
"""
通过CSS来进行查找，先定位，因为option是一组四个的，所以我们通过属性来查找就是[属性名="属性值"]，定位到之后给一个click点击操作来选中
driver.find_element_by_css_selector('[value="sh"]').click()
sleep(2)
driver.find_element_by_css_selector('[value="cq"]').click()
sleep(2)
driver.find_element_by_css_selector('[value="gz"]').click()

"""

"""
通过select下拉框select_by_index(下标值)来选择
element = driver.find_element_by_css_selector("select")
Select(element).select_by_index(1)
sleep(2)
Select(element).select_by_index(3)
sleep(2)
Select(element).select_by_index(2)
"""
"""
通过select下拉框select_by_value(属性值)来选择
element = driver.find_element_by_css_selector("select")
Select(element).select_by_value("sh")
sleep(2)
Select(element).select_by_value("cq")
sleep(2)
Select(element).select_by_value("gz")

"""

"""
通过select下拉框select_by_visible_text(显示的文本值)来选择
element = driver.find_element_by_css_selector("select")
Select(element).select_by_visible_text("A上海")
sleep(3)
Select(element).select_by_visible_text("A重庆")
sleep(3)
Select(element).select_by_visible_text("A广州")
"""



sleep(3)
driver.quit()