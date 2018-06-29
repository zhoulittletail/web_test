import unittest
from WebDriver.Fz02.po.login_po import Iweb_login
class Iwebshop(unittest.TestCase):
    login=Iweb_login()
    def test001(self):
        self.login.iweb_login("zhangziyi","123456")
        text = self.login.element_text("css",".loginfo")
        print("获取登录信息文本:",text)
        try:
            self.assertIn("admin",text)
        except AssertionError:
            self.login.get_img("../img/")
            raise
        finally:
            self.login.iweb_out()
            self.login.iweb_quit()
    login3=Iweb_login()
    def test002(self):
        self.login3.iweb_login("zhangziyi", "12345")
        text = self.login3.element_text("css", ".invalid-msg")
        print("获取登录信息文本1:", text)
        try:
            self.assertIn("填写密码1", text)
        except AssertionError:
            self.login3.get_img("../img/")
            raise
        finally:
            self.login3.iweb_quit()
    login1 = Iweb_login()
    def test003(self):
        self.login1.iweb_login("zhangziyi", "12345wte")
        text = self.login1.element_text("css",".prompt")
        print("获取登录信息文本2:", text)
        try:
            self.assertIn("用户名和密码不匹配1", text)
        except AssertionError:
            self.login1.get_img("../img/")
            raise
        finally:
            self.login1.iweb_quit()
    login2=Iweb_login()
    def test004(self):
        self.login2.iweb_login(" ", "123456")
        text = self.login2.element_text("css", ".invalid-msg")
        print("获取登录信息文本2:", text)
        try:
            self.assertIn("填写用户名 邮箱",text)
        except AssertionError:
            self.login2.get_img("../img/")
            raise
        finally:
            self.login2.iweb_quit()
if __name__ == '__main__':
    unittest.main()