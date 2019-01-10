# -*- coding: utf-8 -*-
# @Time  : 2018/11/18 14:24
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : project_path.py
import os
from time import strftime

'''专门来读取路径的值'''
# 获取顶级目录的路径
project_path = os.path.split(os.path.dirname(__file__))[0]

# 测试报告的路径
test_report_path = os.path.join(project_path, 'TestResult', 'html_report', '%s.html'%strftime('%Y-%m-%d'))

# 配置截图的路径
screenshot_path = os.path.join(project_path, 'TestResult', 'image')

# 配置log路径
logs_path = os.path.join(project_path, 'TestResult', 'log', '%s_log.txt' % strftime('%Y_%m_%d_%H_%M'))

