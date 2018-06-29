from time import sleep

from  selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)
driver.find_element_by_link_text("访问 新浪 网站").click()



sleep(3)
driver.quit()