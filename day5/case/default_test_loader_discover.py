import unittest
if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover("./",pattern="test*.py")
    unittest.TextTestRunner().run(discover)