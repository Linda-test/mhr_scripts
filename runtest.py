import time
import unittest
from BeautifulReport import BeautifulReport

if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(".",pattern="test_M06*.py",top_level_dir=None)     #"."表示当前目录，"*tests.py "匹配当前目录下所有tests.py
    nowtime = time.strftime("%Y%m%d%H%M%S")
    BeautifulReport(discover).report(filename="Test Report_"+nowtime, description='测试报告',report_dir="./report")

