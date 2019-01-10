# -*- coding: utf-8 -*-
# @Time  : 2018/11/13 14:49
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : run.py.py
import unittest
import HTMLTestRunnerNew
import HTMLTestRunnerP
from TestCases import test_0_login
from Common.project_path import test_report_path

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(test_0_login.TestLogin))
suite.addTest(loader.loadTestsFromTestCase(test_0_login.TestLogin_ddt))

with open(test_report_path, "wb") as file:
    runner = HTMLTestRunnerP.HTMLTestRunner(stream=file, verbosity=2, title="UI测试报告", description="cloudhawk")
    runner.run(suite)

# 生成测试报告后发送给指定收件人
# SendEmail().send_email("3097944154@qq.com", test_report_path)
