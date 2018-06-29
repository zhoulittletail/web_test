from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)

# driver.maximize_window()
driver.implicitly_wait(30)
js = "window.scrollTo(0,10000)"
driver.execute_script(js)
sleep(3)
js1 = "window.scrollTo(0,0)"
driver.execute_script(js1)
sleep(3)
driver.quit()