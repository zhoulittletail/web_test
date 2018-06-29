# 2.# po
# 新建类（继承Common类）
# 1.# 定义登录方法（必须要有两个参数：username, password)
    # 1.# 点击登录（调用了封装的单击方法）
    # 2.# 输入用户名（调用了封装的输入方法）
    # 3.# 输入密码（调用了封装的输入方法）
    # 4.# 点击登录(调用了封装的单击方法)
# 2.# 定义退出方法
#   1.# 点击退出（调用封装的点击方法）
#
# 3.# 定义关闭浏览器
from time import sleep

from WebDriver.fengzhuang.common.iweb_shop_common import Iwebshop_common
class Iwebshop_login(Iwebshop_common):
    def iweb_login(self,username,password):
        self.driver.get("http://192.168.178.136/iwebshop/")
        self.element_click("partial_link","登录")
        self.element_input("css",'[name="login_info"]',username)
        self.element_input("css",'[name="password"]',password)
        self.element_click("css",'[class="submit_login"]')
    def iweb_out(self):
        sleep(3)
        self.element_click("partial_link",'安全退出')
    def iweb_quit(self):
        sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    login = Iwebshop_login()
    login.iweb_login("zhangziyi","123456")
    login.iweb_out()
    login.iweb_quit()
    # login1 = Iwebshop_login()
    # # login1.iweb_login("zhangziyi", "112233")
    # # # login1.iweb_out()
    # login1.iweb_quit()
    # login2 = Iwebshop_login()
    # # login2.iweb_login("", "123456")
    # # # login2.iweb_out()
    # login2.iweb_quit()


