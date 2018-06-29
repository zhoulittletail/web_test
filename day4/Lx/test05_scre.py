from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册实例.html"
driver.get(url)
try:
    driver.find_element_by_link_text("注册A网页").click()
    driver.find_element_by_css_selector("#userA").send_keys("admin")
    driver.find_element_by_css_selector("#passwordA").send_keys("admin")
    driver.find_element_by_css_selector("#telA").send_keys("186123")
    driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
except:
    driver.get_screenshot_as_file("../img/001.jpg")





sleep( 3)
driver.quit()