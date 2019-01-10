# -*- coding: utf-8 -*-
# @Time  : 2018/12/24 15:17
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : loginpage_locators.py

from selenium.webdriver.common.by import By


class Loginpage_locators:
    # 用户名输入框
    name_text = (By.XPATH, '//input[@class="username form-control ng-untouched ng-pristine ng-invalid"]')
    # 密码输入框
    pwd_text = (By.XPATH, '//input[@class="password form-control ng-untouched ng-pristine ng-invalid"]')
    # 登录按钮
    login_button = (By.XPATH, '//button[@class="btn btn-auth btn-block"]')
    # 记住我选择框
    remeber_me_text = (By.XPATH, '//span[text()="Remember me"]')
    # 错误提示框 - 登录按钮上方
    errorMsg_loginArea_text = (By.XPATH, '//div[@class="auth-error mt-10 mb-5"]')
    # 错误提示框 - 用户名输入框后方
    errorMsg_Behindbox_text = (By.XPATH, '//div[@class="error-item"]')
    # 页脚 - 输入框失焦操作用
    Defocus_text = (By.XPATH, '//footer[@class="page-footer"]')
    # 忘记密码入口
    forgetpassword_enter_text = (By.XPATH, '//a[@class="pull-right"]')

