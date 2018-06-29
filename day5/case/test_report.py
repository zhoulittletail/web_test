# import  unittest
# import time
# from day5.Report.HTMLTestRunner import HTMLTestRunner
# if __name__ == '__main__':
#     unittest.main
#     discover = unittest.defaultTestLoader.discover("./",pattern="test*.py")
#     file_dir = "../Report/"
#     nowtime=time.strftime("%Y_%m_%d %H_%M_%S")
#     file_name = file_dir+nowtime+"report.html"
# with open(file_name,"wb")as file:
#     HTMLTestRunner(stream=file,title="xxweb自动化测试报告",description="egqwevreu").run(discover)
import unittest

import time

from WebDriver.day5.Report.HTMLTestRunner import HTMLTestRunner
if __name__ == '__main__':
    aa = unittest.defaultTestLoader.discover("./",pattern="test*.py")
    file_dir = "../Report/"
    nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
    file_name = file_dir+ "-" +nowtime+"-report.html"
with open(file_name,"wb") as f:
    HTMLTestRunner(stream=f,title="iwebshop项目web自动化测试报告",description="环境：win7系统下").run(aa)
