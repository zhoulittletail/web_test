import time

from WebDriver.day5.Report.HTMLTestRunner import HTMLTestRunner
import unittest
if __name__ == '__main__':
    filepath="./"
    nowtime=time.strftime("%Y_%m_%d %H_%M_%S")
    filename=filepath+nowtime+"report.html"
    discover = unittest.defaultTestLoader.discover("./",pattern="test*.py")
    with open(filename,"wb")as f:
        HTMLTestRunner(stream=f).run(discover)