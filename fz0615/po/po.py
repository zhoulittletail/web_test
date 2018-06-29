from WebDriver.fz0615.common.common import Common
class Login_Serch(Common):
    def iweb_serch(self,username,passwd):
        self.driver.get("http://192.168.178.140/iwebshop/")
        # input = self.element_input("css",'[name="word"]',serch_name)
        # input.send_keys(Keys.ENTER)
        # serch_text=self.element_text("css",".red")
        self.element_click("partial_link","女装")
        self.element_click("partial_link","莉兰秀人 限时折扣 促销 夏季 新款真丝连衣裙")
        self.element_click("partial_link","登录")
        self.element_input("css",'[name="login_info"]',username)
        self.element_input("css",'[name="password"]',passwd)
        self.element_click("css",".submit_login")
    def iweb_out(self):
        self.element_click("css",".reg")
    def iweb_close(self):
        self.driver.quit()
if __name__ == '__main__':

    shop=Login_Serch()
    shop.iweb_serch("zhou","123456")
    shop.iweb_close()

