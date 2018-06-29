
import unittest
from day5.lx.lx_test_testcase import Test01
from day5.lx.lx_test_case import Test11
suite = unittest.TestSuite()
# suite.addTest(Test11("test11"))
# suite.addTest(Test11("test12"))
# suite.addTest(Test01("test001"))
# suite.addTest(Test01("test002"))
# suite.addTest(unittest.makeSuite(Test11))
# suite.addTest(unittest.makeSuite(Test01))
# unittest.TextTestRunner().run(suite)
aa = unittest.defaultTestLoader.discover("./",pattern="test*.py")
unittest.TextTestRunner().run(aa)
if __name__ == '__main__':
    unittest.main