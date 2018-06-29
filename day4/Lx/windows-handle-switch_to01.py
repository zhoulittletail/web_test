from time import sleep

from selenium import webdriver
all_hanled= {}
def get_windows(windows):
    for wind in windows:
        driver.switch_to.window(wind)
        title=driver.title
        all_hanled[title]=wind
    return all_hanled
driver = webdriver.Firefox()
cur_window=driver.current_window_handle
driver.get(r"C:\软件测试\就业班\05 Web自动化测试\web自动化环境\课堂素材\注册实例.html")
driver.find_element_by_partial_link_text("注册A").click()
driver.find_element_by_partial_link_text("注册B").click()
windows = driver.window_handles
driver.switch_to.window(get_windows(windows)["注册B"])
driver.find_element_by_css_selector("#userB").send_keys("admin")
driver.find_element_by_css_selector("#passwordB").send_keys("123456")
driver.find_element_by_css_selector("#telB").send_keys("186123456")
driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")
driver.find_element_by_css_selector('[value="注册B"]').click()
sleep(3)
driver.quit()