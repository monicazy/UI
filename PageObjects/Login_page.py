# -*- coding: utf-8 -*-
# @Time  : 2018/12/24 11:14
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : Login_page.py
from PageLocators.loginpage_locators import Loginpage_locators as loc
from Common.basepage import BasePage


class Login_page(BasePage):

    # 登录功能
    def login(self, username, passwd, remeber_user=False):
        # 输入用户名、密码、判断是否记住手机号，点击登录按钮
        doc = "登录页面_登录功能"
        self.wait_eleVisible(loc.name_text, doc=doc)
        self.input_text(loc.name_text, username, doc)
        self.input_text(loc.pwd_text, passwd, doc)
        self.click_element(loc.Defocus_text,doc)
        if remeber_user == True:
            self.click_element(loc.remeber_me_text, doc)
        self.click_element(loc.login_button, doc)

    # 获取错误提示信息 - 登录按钮上方
    def get_errorMsg_loginArea(self):
        doc = "登录页面_登录功能_获取登录按钮上方错误提示信息"
        self.wait_eleVisible(loc.errorMsg_loginArea_text, doc=doc)
        return self.get_text(loc.errorMsg_loginArea_text, doc)

    # 获取错误提示信息 - 输入框后方
    def get_errorMsg_Behindbox(self):
        doc = "登录页面_登录功能_获取输入框后方错误提示信息"
        self.wait_eleVisible(loc.errorMsg_Behindbox_text, doc=doc)
        return self.get_text(loc.errorMsg_Behindbox_text, doc)

    # 忘记密码入口
    def forgetpassword_enter(self):
        doc = "登录页面_忘记密码入口"
        self.wait_eleVisible(loc.forgetpassword_enter_text, doc=doc)
        self.click_element(loc.forgetpassword_enter_text)
