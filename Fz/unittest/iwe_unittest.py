import unittest
from WebDriver.Fz.po.iweb_login import Iweb_login
class Iweb(unittest.TestCase):
    login= Iweb_login()
    def test001(self):
        self.login.iweb_login("zhangziyi","123456")
        text = self.login.element_text("css",".loginfo")
        print("获取登录文本信息：",text)
        try:
            self.assertIn("admin",text)
        except AssertionError:
            self.login.get_img("../img/")
            raise

        finally:
            self.login.iweb_out()
            # self.login.iweb_quit()
    def test002(self):
        self.login.iweb_login("","123456")
        text = self.login.element_text("css",".invalid-msg")
        print("获取登陆失败文本信息1：", text)
        try:
            self.assertIn("填写用户名或 邮箱",text)
        except AssertionError:
            self.login.get_img("../img/")
            raise
        finally:
            self.login.iweb_quit()
    login1=Iweb_login()
    def test003(self):
        self.login1.iweb_login("zhangziyi","admin")
        text = self.login1.element_text("css",".invalid-msg")
        print("获取登陆失败文本信息2：",text)
        try:
            self.assertIn("填写密码1",text)
        except:
            self.login1.get_img("../img/")
            raise
        finally:
            self.login1.iweb_quit()

if __name__ == '__main__':
    unittest.main()

