from time import sleep

from selenium import webdriver
# from selenium.webdriver.common.alert import Alert
driver = webdriver.Firefox()
url = r"C:\Users\23746\Desktop\web自动化环境\课堂素材\注册实例.html"
driver.get(url)
# driver.implicitly_wait(15)
"""
警告框处理
driver.find_element_by_css_selector("#alert").click()  # 先定位到alert按钮，给一个点击触发警告框
alert = driver.switch_to.alert  #  调出警告框，并实例化
text = alert.text   #  获取警告框文本信息
print("警告框文字信息为：",text)  #  输出警告框文本信息
alert.accept()  #  获取警告框“接受”选择
"""

"""
两个窗口之间通过窗口唯一的标识码handle来切换窗口
driver.find_element_by_link_text("注册A网页").click()  # 定位到A标签注册A网页，给一个click来打开这个页面
cur_handle = driver.current_window_handle  #  获取当前页面的句柄
handles = driver.window_handles   #  获取所有窗口的句柄
print("当前窗口句柄：",cur_handle)  # 输出当前页面的句柄  。注意这里输出的是一个字典
print("所以窗口句柄：",handles)# 输出所有页面的句柄 。注意这里输出的是一个列表
for handle in handles:   #  遍历 所有窗口句柄，查找handle是否包含在所有句柄这个列表中
    if handle != cur_handle:   #  对handle进行匹配，如果相同if条件不成立就不执行切换窗口句柄的操作，匹配不到时就会触发if条件，然后切换窗口
        driver.switch_to.window(handle)   #  if条件成立时执行切换窗口操作
        driver.find_element_by_css_selector("#userA").send_keys("admin")   #  这时候才可以进行定位元素传值
        driver.find_element_by_css_selector("#passwordA").send_keys("123456") #  这时候才可以进行定位元素传值
        driver.find_element_by_css_selector("#telA").send_keys("186123") #  这时候才可以进行定位元素传值
        driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com") #  这时候才可以进行定位元素传值

"""

"""
滚动条操作
js = "window.scrollTo(0,10000)"
js1 = "window.scrollTo(0,0)"
driver.execute_script(js)   #  调用js执行滚动条操作
"""

""""
表单切换操作
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("123456")
driver.find_element_by_css_selector("#tel").send_keys("186123")
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

driver.switch_to.frame("myframe1")  #  表单切换
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector("#telA").send_keys("186123")
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")


driver.switch_to.default_content()   #  返回到含有frame或iframe页面以便进行下次查找其他表单
driver.switch_to.frame("myframe2")   #  切换到另一个表单
driver.find_element_by_css_selector("#userB").send_keys("admin")
driver.find_element_by_css_selector("#passwordB").send_keys("123456")
driver.find_element_by_css_selector("#telB").send_keys("186123")
driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")

"""
"""
#   当页面执行出现异常时，然后我们进行截图保存
try:
    driver.find_element_by_css_selector("#user").send_keys("admin")
    driver.find_element_by_css_selector("#password").send_keys("123456")
    driver.find_element_by_css_selector("#tel").send_keys("186123")
    driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

    driver.switch_to.frame("myframe1")  #  表单切换
    driver.find_element_by_css_selector("#userA").send_keys("admin")
    driver.find_element_by_css_selector("#passwordb").send_keys("123456")
    driver.find_element_by_css_selector("#telB").send_keys("186123")
    driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")
except:
    driver.get_screenshot_as_file("../img/12.jpg")

"""""

"""
因为自动化没法智能的进行验证码，所有验证码需要绕开操作！
验证码这个有三种方法
1 去掉验证面操作（注销），前提时在测试环境下才可以
2 万能验证码（是在生产/线上环境下，而且项目是自己团队开发进行的，方法是再验证方法的代码后面加一个逻辑或操作加  "or xxx"
3 cookie  此方法是常用的，也是再线上环境下进行的，我们测试只需要找开发问哪几个验证的
driver.add_cookie(这里面的问开发)

添加cookie之后要刷新才能看到效果
"""

driver.find_element_by_id("user").send_keys("admin")
sleep(2)
driver.find_element_by_class_name("tel").send_keys("1234567890")
sleep(2)
driver.find_element_by_name("email").send_keys("123@qq.com")
sleep(2)
driver.find_elements_by_tag_name("input")[2].send_keys("123456")
sleep(2)
driver.find_element_by_link_text("访问 新浪 网站").click()
sleep(2)
driver.back()
driver.find_element_by_partial_link_text("访问 新浪").click()
sleep(2)
driver.find_element_by_css_selector('[type="password"]').send_keys("123qqcom")
sleep(2)


driver.quit()
