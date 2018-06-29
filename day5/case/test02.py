import unittest
class Test02(unittest.TestCase):
    def setUp(self):
        print("Test02-->setUp被执行")
    def tearDown(self):
        print("Test02-->tearDown被执行")
    def test001(self):
        print("Test02-->test001被执行！")