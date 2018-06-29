from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册实例.html"
driver.get(url)

driver.find_element_by_link_text("注册A网页").click()
handle = driver.current_window_handle
print(handle)
handles = driver.window_handles
print(handles)
for hand in handles:
    if hand != handle:
        driver.switch_to.window(hand)
        driver.find_element_by_css_selector("#userA").send_keys("admin")
        driver.find_element_by_css_selector("#passwordA").send_keys("admin")
        driver.find_element_by_css_selector("#telA").send_keys("186123")
        driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")

sleep( 3)
driver.quit()