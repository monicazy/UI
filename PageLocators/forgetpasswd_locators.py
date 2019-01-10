# -*- coding: utf-8 -*-
# @Time  : 2018/12/24 16:20
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : forgetpasswd_locators.py
from selenium.webdriver.common.by import By


class Forgetpwd_locators:
    # 重置密码按钮(属性与登录按钮相同，所以写成文本寻找)
    forgetpasswdbutton_text = (By.XPATH, '//button[text()="Reset Password"]')