from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册A.html"
driver.get(url)
# 2.上传文件成功后，如果让程序判断上传成功？

driver.find_element_by_css_selector('[type="file"]').send_keys("C:\\Users\23746\Desktop\周兰花作业day3\q.jpg")
value = driver.find_element_by_css_selector('[type="file"]').get_attribute("value")
print(value)
if value == "q.jpg":
    print("上传成功！")
sleep(3)
driver.quit()