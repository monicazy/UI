# -*- coding: utf-8 -*-
# @Time  : 2019/1/9 13:56
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : conftest.py
import pytest
from selenium import webdriver
from TestDatas import login_datas as LD
from PageObjects.Login_page import Login_page
from TestDatas import Common_Datas as CD
from PageObjects.LiveMap_page import LiveMapPage
from PageObjects.forgetpasswd_page import Forgetpasswd
from Common.my_log import MyLog

driver = None


@pytest.fixture(scope="class")
def login_web():
    MyLog().my_log("INFO", "==========所有测试用例之前的，seupclass==用例类前置：初始化浏览器，打开登录页==========")
    global driver
    # 前置条件
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    driver.maximize_window()
    lg = Login_page(driver)
    yield (driver, lg)
    # 后置条件：关闭浏览器
    MyLog().my_log("INFO", "==========所有测试用例之后的，teardwonclass==用例类后置：关闭浏览器==========")
    driver.quit()


@pytest.fixture
def refresh_page():
    global driver
    yield
    # 刷新浏览器
    MyLog().my_log("INFO", "==========每个测试用例之后的，teardwon==用例后置：刷新浏览器==========")
    driver.refresh()


@pytest.fixture(scope="class")
def livemap_web():
    MyLog().my_log("INFO", "==========所有测试用例之前的，seupclass==用例类前置：初始化浏览器，打开登录页==========")
    global driver
    # 前置条件
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    driver.maximize_window()
    lg = Login_page(driver)
    LP = LiveMapPage(driver)
    # 登录
    lg.login(LD.success_data["user"], LD.success_data["passwd"])
    yield (driver, LP)
    # 后置条件：关闭浏览器
    MyLog().my_log("INFO", "==========所有测试用例之后的，teardwonclass==用例类后置：关闭浏览器==========")
    driver.quit()
