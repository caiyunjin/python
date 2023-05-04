"""
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-05-01 20:27:16
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-05-02 10:42:56
FilePath: \py\Qt\mainwindow.py
Description: 

Copyright (c) 2023 by 蔡沄金, All Rights Reserved. 
"""
from PySide6.QtWidgets import QMainWindow
from login import LoginWindow
from UI.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 创建ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 创建登录类
        self.loginWindow = LoginWindow(self)
        # 隐藏自己
        self.hide()
