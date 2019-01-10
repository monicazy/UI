# -*- coding: utf-8 -*-
# @Time  : 2018/12/24 13:31
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : login_datas.py

# 正常场景 - 测试数据
success_data = {"user": 'cloudhawkadmin@rongrongzhang.com', "passwd": '123456', "title": "登录_成功登录"}

# 异常用例 - 登录信息错误（用户名错误、密码错误、用户名不存在）
phone_data = [
    {"user": 'cloudhawkadmin@rongrongzhang.co', "passwd": '123456', "check": "Invalid account and/or password.",
     "title": "登录_用户名错误"},
    {"user": 'cloudhawkadmin@rongrongzhang.com', "passwd": '4444444', "check": "Invalid account and/or password.",
     "title": "登录_密码错误"},
    {"user": 'cloudhawk@rongrongzhang.com', "passwd": '123456', "check": "Invalid account and/or password.",
     "title": "登录_用户名不存在"}
]

# 异常用例 - 登录信息格式错误（错误的邮箱格式、用户名为空格、用户名为空、密码为空、密码为空格、密码小于6位）
pwd_data = [
    {"user": 'cloudhawkrongrongzhang.com', "passwd": '123456', "check": "Invalid email format", "title": "登录_错误的邮箱格式"},
    {"user": ' ', "passwd": '123456', "check": "Required", "title": "登录_用户名为空格"},
    {"user": '', "passwd": '123456', "check": "Required", "title": "登录_用户名为空"},
    {"user": 'cloudhawk@rongrongzhang.com', "passwd": '', "check": "Required", "title": "登录_密码为空"},
    {"user": 'cloudhawk@rongrongzhang.com', "passwd": ' ', "check": "Invalid password format", "title": "登录_密码为空格"},
    {"user": 'cloudhawk@rongrongzhang.com', "passwd": '1234', "check": "Invalid password format", "title": "登录_密码小于6位"}
]
