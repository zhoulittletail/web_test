# 3.  UnitTest
#     def test001()  # 正确用户 正确密码
#     重点：  1.    调用登录方法(username, password)
#             2.    获取断言(调用获取文本方法)
#             3.    截图（调用截屏方法）
#             4.    退出（调用退出浏览器方法）
#     def test002()  # 正确用户 错误密码
#         1.  调用登录方法(username, password)
#         2.   获取断言(调用获取文本方法)
#
#     def tearDown（        ）
#     调用关闭浏览器方法
import unittest
from WebDriver.fengzhuang.po.iwebshop_login import Iwebshop_login

class Iweb_test(unittest.TestCase):
    login = Iwebshop_login()
    def test001(self):

        self.login.iweb_login("zhangziyi","123456")
        text = self.login.element_tetx("css",".loginfo")
        print("获取登录信息为：",text)
        try:
            self.assertIn("admin",text)
        except AssertionError:
            self.login.get_img("../img/")
            raise
        finally:
            self.login.iweb_out()
    def test002(self):
        # login = Iwebshop_login()
        self.login.iweb_login("zhangziyi", "admin")
        text= self.login.element_tetx("css",".invalid-msg")
        print("获取登陆失败1信息：",text)
        try:
            self.assertIn("填写密码1",text)
        except AssertionError:
            self.login.get_img("../img/")
            raise
        finally:
            self.login.iweb_quit()
    # login = Iwebshop_login()
    login1 = Iwebshop_login()
    def test003(self):
        #
        self.login1.iweb_login("zhangziyi","112233")
        text = self.login1.element_tetx("css",".prompt")
        print("获取登陆失败信息：",text)
        try:
            self.assertIn("用户名和密码不匹配1",text)
        except AssertionError:
            self.login1.get_img("../img/")
            raise
        finally:
            self.login1.iweb_quit()

    login2 = Iwebshop_login()
    # login = Iwebshop_login()
    def test004(self):
        #
        self.login2.iweb_login("","123456")
        text = self.login2.element_tetx("css",".invalid-msg")
        print("获取登录失败信息2：",text)
        try:
            self.assertIn("填写用户名或邮箱2",text)
        except AssertionError:
            self.login2.get_img("../img/")
            raise
        finally:
            self.login2.iweb_quit()
if __name__ == '__main__':
    unittest.main()

