from WebDriver.fz03.common.Common import Common
class Iweb_login(Common):
    def iweb_lohin(self,username,password):
        self.driver.get("http://192.168.178.140/iwebshop")
        self.element_click("partial_link","登录")
        self.element_input("css",'[name="login_info"]',username)
        self.element_input("css",'[name="password"]',password)
        self.element_click("css",".submit_login")
    def iweb_out(self):
        self.element_click("css",".reg")
    def iweb_quit(self):
        self.driver.quit()
if __name__ == '__main__':

    login = Iweb_login()
    login.iweb_lohin("zhangziyi","123456")
    login.iweb_out()
    login.iweb_quit()
