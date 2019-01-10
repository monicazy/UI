# -*- coding: utf-8 -*-
# @Time  : 2018/12/24 14:08
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : test_0_login.py

from TestDatas import login_datas as LD
from PageObjects.LiveMap_page import LiveMapPage
from PageObjects.forgetpasswd_page import Forgetpasswd
from Common.my_log import MyLog
import pytest


# @pytest.mark.usefixtures("login_web")
# @pytest.mark.usefixtures("refresh_page")
# class TestLogin:
#     # 异常用例 - 登录信息错误（用户名错误、密码错误、用户名不存在）
#     @pytest.mark.parametrize("data", LD.phone_data)
#     def test_login1_wrong(self, data,login_web):
#         MyLog().my_log("INFO", "——————————当前执行的用例是：{}——————————".format(data["title"]))
#         # 步骤：输入用户名、密码
#         login_web[1].login(data["user"], data["passwd"])
#         # 断言 对比文本内容是否与期望值一致
#         assert login_web[1].get_errorMsg_loginArea() == data["check"]
#
#     # 异常用例 - 登录信息格式错误（错误的邮箱格式、用户名为空、密码为空、密码小于6位）
#     @pytest.mark.parametrize("data", LD.pwd_data)
#     def test_login2_formaterror(self, data,login_web):
#         MyLog().my_log("INFO", "——————————当前执行的用例是：{}——————————".format(data["title"]))
#         # 步骤：输入用户名、密码
#         login_web[1].login(data["user"], data["passwd"])
#         # 断言 对比文本内容是否与期望值一致
#         assert login_web[1].get_errorMsg_Behindbox() == data["check"]
#
#     # 正常用例--登录成功
#     # @pytest.mark.smoke
#     def test_login_success(self,login_web):
#         MyLog().my_log("INFO","——————————当前执行的用例是：{}——————————".format(LD.success_data["title"]))
#         # 步骤 输入用户名、密码
#         login_web[1].login(LD.success_data["user"], LD.success_data["passwd"])
#         # 断言 首页当中 - 能否找到处于选中状态的LiveMap一级菜单
#         assert LiveMapPage(login_web[0]).isExist_LiveMapMenu_ele()
#
#
# # 忘记密码入口
# @pytest.mark.usefixtures("login_web")
# @pytest.mark.usefixtures("refresh_page")
# def test_forgetpasswd_enter(login_web):
#     MyLog().my_log("INFO", "——————————当前执行的用例是：忘记密码入口——————————")
#     # 调用函数,点击忘记密码按钮
#     login_web[1].forgetpassword_enter()
#     # 断言 是否在重置密码页面通过Reset Password字样找到重置按钮
#     assert Forgetpasswd(login_web[0]).isExist_resetpwd_ele()

