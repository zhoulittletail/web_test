from time import sleep

from WebDriver.Fz02.common.iweb_common import Common
class Iweb_login(Common):
    def iweb_login(self,username,password):
        self.driver.get("http://192.168.178.136/iwebshop/")
        self.element_click("partial_link","登录")
        self.element_input("css",'[name="login_info"]',username)
        self.element_input("css",'[name="password"]',password)
        self.element_click("css",".submit_login")
    def iweb_out(self):
        self.element_click("css",".reg")
    def iweb_quit(self):
        sleep(2)
        self.driver.quit()
login=Iweb_login()
login.iweb_login("zhangziyi","123456")
login.iweb_out()
login.iweb_quit()