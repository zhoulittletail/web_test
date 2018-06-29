import unittest
from WebDriver.UnitTest.day2.Code.sjx import Sjx
from WebDriver.UnitTest.day2.Read_Data.read_json01 import Read_json

sjxClass = Sjx()
json = Read_json()


class Test01(unittest.TestCase):
    def test001(self):
        for i in range(len(json.read_json())):
            text = sjxClass.sjx(int(json.read_json()[i]["b1"]),
                                int(json.read_json()[i]["b2"]),
                                int(json.read_json()[i]["b3"]),
                                )
            try:
                self.assertEqual(text, json.read_json()[i]["expect"])
                print(
                    json.read_json()[i]["b1"],
                    json.read_json()[i]["b2"],
                    json.read_json()[i]["b3"],
                    json.read_json()[i]["expect"], "验证成功！"
                )
            except:
                print(
                    json.read_json()[i]["b1"],
                    json.read_json()[i]["b2"],
                    json.read_json()[i]["b3"],
                    json.read_json()[i]["expect"], "——验证失败！——"
                )


if __name__ == '__main__':
    unittest.main()
