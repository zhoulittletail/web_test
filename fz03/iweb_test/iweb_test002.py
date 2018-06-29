import unittest
from WebDriver.fz03.po.po import Iweb_login
class Iweb_unittest(unittest.TestCase):
    login = Iweb_login()
    def test001(self):
        self.login.iweb_lohin("zhangziyi","123456")
        text = self.login.element_text("css",".loginfo")
        print("获取登陆成功文本信息：",text)
        try:
            self.assertIn("admin",text)
        except AssertionError:
            self.login.get_img("../img/")
            raise
        finally:
            self.login.iweb_out()
            self.login.iweb_quit()
    def test002(self):
        self.login.iweb_lohin("zhangziyi","12345")
        text = self.login.element_text("css",".invalid-msg")
        print("获取登陆失败文本信息1：", text)
        try:
            self.assertIn("请 填写密码",text)
        except AssertionError:
            self.login.get_img("../img/")
            raise
        finally:
            self.login.iweb_quit()
if __name__ == '__main__':
    unittest.main()