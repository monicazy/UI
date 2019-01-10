# -*- coding: utf-8 -*-
# @Time  : 2018/12/24 16:24
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : forgetpasswd_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.forgetpasswd_locators import Forgetpwd_locators as floc
from Common.my_log import MyLog
from Common.basepage import BasePage


class Forgetpasswd(BasePage):
    # 重置密码按钮是否存在
    def isExist_resetpwd_ele(self):
        # 如果通过重置文本找到该元素，则返回True，否则返回False
        doc = "重置密码页面_重置密码按钮"
        return self.wait_elePresence(floc.forgetpasswdbutton_text, doc=doc)
