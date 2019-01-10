# -*- coding: utf-8 -*-
# @Time  : 2019/1/4 15:42
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : test_1_livamap.py

from selenium import webdriver
from TestDatas import login_datas as LD
from PageObjects.Login_page import Login_page
from TestDatas import Common_Datas as CD
from PageObjects.LiveMap_page import LiveMapPage
from Common.my_log import MyLog
from TestDatas import login_datas as LD
from TestDatas import livemap_datas as LM
import pytest


@pytest.mark.usefixtures("livemap_web")
@pytest.mark.usefixtures("refresh_page")
class TestLiveMap:
    # 搜索功能 -- 以标签进行搜索
    # @pytest.mark.smoke
    def test_click_select_label(self, livemap_web):
        # 步骤：点击显示标签按钮，随机选择一个标签
        livemap_web[1].labels_button()
        livemap_web[1].click_label_by_random()
        # 断言：搜索输入框下方是否出现该标签
        assert livemap_web[1].isExist_select_label_Below_inputbox()
        # 关闭标签搜索
        livemap_web[1].close_select_label_Below_inputbox()

    # 搜索功能 -- tracker list搜索框搜索
    # @pytest.mark.smoke
    def test_input_select(self, livemap_web):
        MyLog().my_log("INFO", "——————————当前执行的用例是：{}——————————".format(LM.select_assert_success["title"]))
        # 步骤：tracker list搜索框输入查询信息
        livemap_web[1].select_assert(LM.select_assert_success["data"])
        # 断言：tracker list中是否过滤出指定终端
        assert LM.select_assert_success["data"] in livemap_web[1].get_assets_list()
        # 清空搜索框
        # livemap_web[1].clear_input_content()

    # 随机点击终端出现地图弹出框
    def test_click_asset(self,livemap_web):
        MyLog().my_log("INFO", "——————————当前执行的用例是：随机点击终端出现地图弹出框——————————")
        # 步骤：随机点击list中的终端
        livemap_web[1].click_asset_on_list()
        # 断言：吹出框中的状态标签是否存在
        assert livemap_web[1].isExist_blow_out_box_tabel_ele()

    # 成功点击info table按钮
    def test_click_info_table(self,livemap_web):
        MyLog().my_log("INFO", "——————————当前执行的用例是：成功点击info table按钮——————————")
        # 步骤：点击info table按钮
        livemap_web[1].click_info_table_button()
        # 断言：表格中是否出现Alerts字样
        assert livemap_web[1].isExist_info_table_form_Alerts()

    # 关闭infotable报表
    def test_close_info_table(self,livemap_web):
        MyLog().my_log("INFO", "——————————当前执行的用例是：关闭infotable报表——————————")
        # 步骤：点击关闭图标
        livemap_web[1].click_info_table_button()
        livemap_web[1].close_info_table()
        # 断言：infotable报表表格中Alerts字样是否不存在了
        assert not livemap_web[1].info_table_alerts_eleVisible()