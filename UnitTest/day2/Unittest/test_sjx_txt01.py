import unittest
from WebDriver.UnitTest.day2.Code.sjx import Sjx
from WebDriver.UnitTest.day2.Read_Data.read_txt01 import Read_txt01
sjxClass = Sjx()
txt = Read_txt01()
class Test_txt01(unittest.TestCase):
    def test001(self):
        for i in range(len(txt.read_txt01())):
            text = sjxClass.sjx(int(txt.read_txt01()[i][0]),
                                int(txt.read_txt01()[i][1]),
                                int(txt.read_txt01()[i][2]),

                                )
            try:
                self.assertEqual(text,txt.read_txt01()[i][3])
                print(
                    (txt.read_txt01()[i][0]),
                    (txt.read_txt01()[i][1]),
                    (txt.read_txt01()[i][2]),
                    (txt.read_txt01()[i][3]),"验证成功！"
                      )
            except:
                print((txt.read_txt01()[i][0]),
                    (txt.read_txt01()[i][1]),
                    (txt.read_txt01()[i][2]),
                    (txt.read_txt01()[i][3]),"——验证失败！——")
if __name__ == '__main__':
    unittest.main()