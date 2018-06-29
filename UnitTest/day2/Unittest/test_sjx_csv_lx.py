import unittest
from WebDriver.UnitTest.day2.Code.sjx import Sjx
from WebDriver.UnitTest.day2.Read_Data.read_csv import Read_csv
sjxClass = Sjx()
csv = Read_csv()
class Test01(unittest.TestCase):
    def test001(self):
        for i in range(len(csv.read_csv())):
            text = sjxClass.sjx(int(csv.read_csv()[0][0]),
                         int(csv.read_csv()[0][1]),
                         int(csv.read_csv()[0][2]),
                         )
            try:
                self.assertEqual(text,csv.read_csv()[0][3])
                print((csv.read_csv()[0][0]),
                      (csv.read_csv()[0][1]),
                      (csv.read_csv()[0][2]),
                      (csv.read_csv()[0][3]),"验证成功！")
            except:
                print((csv.read_csv()[0][0]),
                      (csv.read_csv()[0][1]),
                      (csv.read_csv()[0][2]),
                      (csv.read_csv()[0][3]), "————验证失败！————")
if __name__ == '__main__':
    unittest.main()
