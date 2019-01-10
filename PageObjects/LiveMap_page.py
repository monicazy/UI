# -*- coding: utf-8 -*-
# @Time  : 2018/12/24 11:21
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : LiveMap_page.py

from Common.basepage import BasePage
from PageLocators.livemappage_locators import LiveMap_locators as LL
import random
import time


class LiveMapPage(BasePage):

    def isExist_LiveMapMenu_ele(self):
        # 如果存在就返回True,如果不存在，就返回False
        doc = "LiveMap页面_LiveMap菜单"
        return self.wait_elePresence(LL.Current_menu_text, doc=doc)

    # 搜索功能 -- 输入框搜索
    def select_assert(self, select_text):
        doc = "LiveMap页面_搜索车辆功能_输入框搜索"
        self.wait_eleVisible(LL.select_input_text, doc=doc)
        self.input_text(LL.select_input_text, select_text, doc)

    # 搜索功能 -- 清空搜索框输入
    def clear_input_content(self):
        doc = "LiveMap页面_搜索车辆功能_清空搜索框内容"
        self.wait_eleVisible(LL.clear_select_input_text, doc=doc)
        self.clear_content(LL.clear_select_input_text, doc)

    # 标签按钮
    def labels_button(self):
        doc = "LiveMap页面_展开标签列表_标签按钮"
        self.wait_eleVisible(LL.label_button_text, doc=doc)
        self.click_element(LL.label_button_text, doc=doc)

    # 搜索功能 -- 随机选一个标签
    def click_label_by_random(self):
        doc = "LiveMap页面_trackerlist_标签筛选"
        self.wait_eleVisible(LL.labels_list_text, doc=doc)
        eles = self.get_elements(LL.labels_list_text, doc)
        # 随机数
        index = random.randint(0, len(eles) - 1)
        eles[index].click()

    # 查询条件 -- 查询的标签是否存在于查询输入框下方
    def isExist_select_label_Below_inputbox(self):
        doc = "LiveMap页面_trackerlist_查询的标签是否存在于查询输入框下方"
        self.wait_eleVisible(LL.select_label_text, doc=doc)
        return self.wait_elePresence(LL.select_label_text, doc=doc)

    # 搜索功能 -- 关闭作为筛选条件的标签
    def close_select_label_Below_inputbox(self):
        doc = "LiveMap页面_trackerlist_关闭查询输入框下方的标签搜索"
        self.wait_eleVisible(LL.select_label_close_button_text, doc=doc)
        self.click_element(LL.select_label_close_button_text, doc)

    # 获取查询结果列表--随机获取其中一个文本
    def get_assets_list(self):
        doc = "LiveMap页面_trackerlist_获取查询结果列表"
        self.wait_eleVisible(LL.tracker_list_text, doc=doc)
        eles = self.get_elements(LL.tracker_list_value_text, doc=doc)
        index = random.randint(0, len(eles) - 1)
        return eles[index].text

    # 随机点击一个车辆
    def click_asset_on_list(self):
        doc = "LiveMap页面_trackerlist_点击车辆"
        self.wait_eleVisible(LL.tracker_list_text, doc=doc)
        eles = self.get_elements(LL.tracker_list_text, doc=doc)
        index = random.randint(0, len(eles) - 1)
        eles[index].click()

    # info table按钮
    def click_info_table_button(self):
        doc = "LiveMap页面_trackerlist_点击info_table按钮"
        self.wait_eleVisible(LL.info_table_button_text, doc=doc)
        time.sleep(0.5)
        self.click_element(LL.info_table_button_text, doc)

    # show all assets按钮
    def click_show_all_assets_button(self):
        doc = "LiveMap页面_trackerlist_点击show_all_assets按钮"
        self.wait_eleVisible(LL.show_all_asserts_button_text, doc=doc)
        self.click_element(LL.show_all_asserts_button_text, doc)

    # 搜索功能 -- 获取作为筛选条件的标签的文本
    def get_select_label_text(self):
        doc = "LiveMap页面_搜索功能_获取作为筛选条件的标签的文本"
        self.wait_eleVisible(LL.select_label_text, doc=doc)
        return self.get_text(LL.select_label_text, doc=doc)

    # 吹出框中的状态标签是否存在
    def isExist_blow_out_box_tabel_ele(self):
        doc = "LiveMap页面_吹出框中的电量图标"
        return self.wait_elePresence(LL.blow_out_box_label_text, doc=doc)

    # info table报表中的Alerts一栏是否存在
    def isExist_info_table_form_Alerts(self):
        doc = "LiveMap页面_搜索功能_info_table报表中的Alerts一栏是否存在"
        return self.wait_elePresence(LL.info_table_form_Alerts_text, doc=doc)

    # info table报表中的Alerts一栏是否可见
    def info_table_alerts_eleVisible(self):
        doc = "LiveMap页面_infotable报表_alerts字样是否可见"
        return self.wait_eleVisible(LL.info_table_form_Alerts_text, doc=doc)

    # 关闭info table 报表
    def close_info_table(self):
        doc = "LiveMap页面_关闭info_table报表"
        self.wait_eleVisible(LL.info_table_close_button_text, doc=doc)
        self.click_element(LL.info_table_close_button_text, doc=doc)
