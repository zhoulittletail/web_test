import unittest
from WebDriver.fz0615.po.po import Login_Serch
class Iweb_unittest(unittest.TestCase):
    shop=Login_Serch()
    def test001(self):
        self.shop.iweb_serch("zhou","123456")
        self.shop.element_click("partial_link","浅灰色")
        self.shop.element_click("partial_link","M")
        self.shop.element_click("css","#number")
        self.shop.element_click("css","#join_car")
        # self.shop.element_click("partial_link","进入购物车")
        self.shop.get_img("../img/")
        car_text=self.shop.element_text("partial_link","莉兰秀人 ")
        try:
            self.assertIn("莉兰秀人 限时折扣 夏季 新款真丝连衣裙",car_text)
        except AssertionError:
            self.shop.get_img("../img/")
            raise
        finally:
            self.shop.iweb_out()
            self.shop.iweb_close()
if __name__ == '__main__':
    unittest.main()

