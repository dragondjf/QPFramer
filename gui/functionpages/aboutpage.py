#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from gui.mainwindow import collectView


class AboutPage(QtWidgets.QFrame):

    viewID = "AboutPage"

    @collectView
    def __init__(self, parent=None):
        super(AboutPage, self).__init__(parent)
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):

        mainlayout = QtWidgets.QVBoxLayout()
        mainlayout.addWidget(QtWidgets.QLabel("dffdfdfdfdfd"))
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.setSpacing(0)
        self.setLayout(mainlayout)
