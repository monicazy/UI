# -*- coding: utf-8 -*-
# @Time  : 2019/1/2 16:36
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : livemappage_locators.py
from selenium.webdriver.common.by import By


class LiveMap_locators:
    # 当前主菜单
    Current_menu_text = (By.XPATH, '//a[text()="Live Map"]')
    # tracker list搜索框 -- 无输入值得时候
    select_input_text = (By.XPATH, '//input[@class="ng-untouched ng-pristine ng-valid"]')
    # tracker list搜索框 -- 有输入值得时候
    clear_select_input_text = (By.XPATH,'//input[@class="ng-valid ng-dirty ng-touched"]')
    # 展开标签按钮
    label_button_text = (By.XPATH, '//i[@class="iconfont icon-list"]')
    # 标签列表组
    labels_list_text = (By.XPATH, '//li[@class="label-item"]')
    # 搜索框下方 -- 作为筛选条件的标签
    select_label_text = (By.XPATH, '//span[@class="label-name"]')
    # 搜索框下方 -- 作为筛选条件的标签上的关闭按钮
    select_label_close_button_text = (By.XPATH, '//span[@class="iconfont icon-close label-close"]')
    # 车辆列表
    tracker_list_text = (By.XPATH, '//div[@class="alias text-overflow font-weight-bold"]')
    # 车辆列表--获取车辆值
    tracker_list_value_text = (By.XPATH, '//div[@class="alias text-overflow font-weight-bold"]')
    # 吹出框中车辆的状态标签
    blow_out_box_label_text = (By.XPATH, '//div[@class="tracker-status"]')
    # 车辆列表中的报表按钮
    info_table_button_text = (By.XPATH, '//span[text()="Tracker Info Table"]')
    # show all asserts按钮
    show_all_asserts_button_text = (By.XPATH, '//button[@class="show-tracker"]')
    # info table报表中的title
    info_table_title_text = (By.XPATH, '//b[text()="Tracker Info Table"]')
    # info table报表中的Alerts一栏
    info_table_form_Alerts_text = (By.XPATH, '//th[text()="Alerts"]')
    # info table报表中的关闭按钮
    info_table_close_button_text = (By.XPATH, '//i[@class="iconfont icon-close"]')
