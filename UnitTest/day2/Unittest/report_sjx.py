import time

from WebDriver.day5.Report.HTMLTestRunner import HTMLTestRunner
import unittest
if __name__ == '__main__':
    file_path = "./"
    nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
    file_name=file_path+nowtime+"Report.html"
    discover = unittest.defaultTestLoader.discover("./",pattern="test*.py")
with open(file_name,"wb")as f:
    HTMLTestRunner(stream=f).run(discover)

