#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from gui.mainwindow import collectView
from .webkitbasepage import WebkitBasePage

class AboutPage(WebkitBasePage):

    viewID = "AboutPage"

    @collectView
    def __init__(self, parent=None):
        super(AboutPage, self).__init__(parent)
        self.setObjectName("AboutPage")
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        url = QtCore.QUrl("http://www.baidu.com")
        self.view.load(url)
