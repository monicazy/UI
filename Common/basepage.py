# -*- coding: utf-8 -*-
# @Time  : 2018/12/28 11:03
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : basepage.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.my_log import MyLog
from datetime import datetime
from time import strftime
from Common.project_path import screenshot_path
import time
import win32gui
import win32con


# 封装基本函数 - 执行日志、异常处理、失败截图
# 所有的页面公共的部分（基本操作）


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, times=30, poll_frequency=0.5, doc=""):
        """
        :param locator: 元素定位。元组形式（元素定位类型、元素定位方式）
        :param times: 超时前的秒数
        :param poll_frequency: 轮询频率，默认情况下，为0.5秒。
        :param doc: 模块名_页面名称_操作名称
        :return: None
        """
        MyLog().my_log("INFO", "{}等待元素{}可见".format(doc, locator))
        try:
            # 开始等待的时间
            start = datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间
            end = datetime.now()
            # 求一个差值写在日志当中，等待了多久,单位毫秒
            MyLog().my_log("INFO", "元素等待结束，等待时间为：{}".format((end - start).microseconds))
            time.sleep(0.5)
            return True
        except:
            MyLog().my_log("exception", "等待元素可见失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            return False

    # 等待元素存在
    def wait_elePresence(self, locator, times=30, poll_frequency=0.5, doc=""):
        MyLog().my_log("INFO", "{}等待元素{}存在".format(doc, locator))
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            return True
        except:
            MyLog().my_log("exception", "等待元素存在失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            return False

    # 查找元素
    def get_element(self, locator, doc=""):
        MyLog().my_log("INFO", "{}查找元素：{}".format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            MyLog().my_log("exception", "查找元素失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            raise

    # 查找多个元素
    def get_elements(self, locator, doc=""):
        MyLog().my_log("INFO", "{}查找元素：{}".format(doc, locator))
        try:
            return self.driver.find_elements(*locator)
        except:
            MyLog().my_log("exception", "查找元素失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        MyLog().my_log("INFO", "{}点击元素：{}".format(doc, locator))
        # 找到要点击的元素
        ele = self.get_element(locator)
        try:
            ele.click()
        except:
            MyLog().my_log("exception", "点击元素失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            raise

    # 清空内容
    def clear_content(self,locator, doc=""):
        MyLog().my_log("INFO", "清空输入框内的数据")
        try:
            time.sleep(0.5)
            self.get_element(locator).clear()
        except:
            MyLog().my_log("exception", "清空失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):
        MyLog().my_log("INFO", "{}输入元素：{}".format(doc, locator))
        # 找到输入框的元素
        ele = self.get_element(locator)
        try:
            ele.send_keys(text)
        except:
            MyLog().my_log("exception", "元素输入失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        MyLog().my_log("INFO", "获取{}元素的文本内容".format(locator))
        # 找到指定的元素
        ele = self.get_element(locator)
        try:
            # 获取属性值
            return ele.text
        except:
            MyLog().my_log("exception", "获取元素的文本内容失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            raise

    # 获取元素的属性值
    def get_element_attribute(self, locator, attribute_text, doc=""):
        MyLog().my_log("INFO", "获取{}元素的属性".format(locator))
        # 找到指定的元素
        ele = self.get_element(locator)
        try:
            # 获取属性值
            return ele.get_attribute(attribute_text)
        except:
            MyLog().my_log("exception", "获取元素的属性失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            raise

    # alert处理
    def alert_action(self, action='accept', doc=""):
        MyLog().my_log("INFO", "等待alert弹出框出现！")
        # 等待alert出现
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        try:
            # alert切换  不是html页面
            alert = self.driver.switch_to.alert
            if action == "accept":
                # 点击确认
                alert.accept()
            elif action == "dismiss":
                # 点击取消
                alert.dismiss()
            elif action == "text":
                # 获取弹窗框里的文字
                return alert.text
        except:
            MyLog().my_log("exception", "alert处理执行失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            raise

    # iframe切换
    def switch_iframe(self, locator, iframe_reference="enter", doc=""):
        try:
            if iframe_reference == "enter":
                # 切入iframe
                WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(locator))
                time.sleep(0.5)
            elif iframe_reference == "out_main":
                # 切出iframe，回到默认主页面
                self.driver.switch_to.default_content()
            elif iframe_reference == "out_up":
                # 切出iframe，返回父级页面（上一级）
                self.driver.switch_to.parent_frame()
        except:
            MyLog().my_log("exception", "iframe_{}切换失败！！！".format(iframe_reference))
            # 截图
            self.save_current_screenshot(doc)
            raise

    # 上传操作
    def upload_file(filepath, title="打开"):
        """
        :param filepath:需要上传的文件路径
        :param title: 弹窗窗口名，默认谷歌浏览器“打开”，火狐为“文件上传”
        :return: None
        """
        # 一级窗口
        dialog = win32gui.FindWindow("#32770", title)
        # 二级窗口
        comboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级窗口
        combox = win32gui.FindWindowEx(comboxex32, 0, "ComboBox", None)
        # 文本的输入窗口 - 四级
        edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
        # 打开按钮 - 二级窗口
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")

        # 输入文件地址
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)  # 发送文件路径
        # 点击 打开按钮    提交文件
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    # 滚动条处理
    # 窗口切换
    # 截图
    def save_current_screenshot(self, name):
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        file_name = screenshot_path + "\\" + "{}_{}.png".format(name, '%s' % strftime('%Y-%m-%d_%H_%M_%S'))
        self.driver.save_screenshot(file_name)
        MyLog().my_log("INFO", "截取网页成功，文件路径为：{}".format(file_name))

    # 断言
    def assert_common(self, assert_sentence, doc="断言失败"):
        try:
            assert_sentence
        except:
            MyLog().my_log("exception", "断言失败！！！")
            # 截图
            self.save_current_screenshot(doc)
            raise
