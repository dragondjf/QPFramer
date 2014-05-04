#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from .navgationbar import NavgationBar
from .titlebar import TitleBar
from .guiconfig import collectView, views
# from gui.functionpages import MonitorPage, AlarmListPage, AboutPage


class CenterWindow(QtWidgets.QFrame):

    viewID = "CenterWindow"

    @collectView
    def __init__(self, parent=None):
        super(CenterWindow, self).__init__(parent)
        self.setObjectName("CenterWindow")
        self.initData()
        self.initUI()

    def initData(self):
        self.pages = {}

    def initUI(self):

        titlebar = TitleBar(self)
        navgationbar = NavgationBar(self)

        # monitorpage = MonitorPage()
        # alarmlistpage = AlarmListPage()
        # aboutpage = AboutPage()

        # self.pages.update({"monitor": monitorpage})
        # self.pages.update({"alarmList": alarmlistpage})
        # self.pages.update({"about": aboutpage})

        # self.stackwiaget = QtWidgets.QStackedWidget()
        # self.stackwiaget.addWidget(monitorpage)
        # self.stackwiaget.addWidget(alarmlistpage)
        # self.stackwiaget.addWidget(aboutpage)

        mainlayout = QtWidgets.QVBoxLayout()
        mainlayout.addWidget(titlebar)
        mainlayout.addWidget(navgationbar)
        # mainlayout.addWidget(self.stackwiaget)
        mainlayout.addStretch()
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.setSpacing(0)
        self.setLayout(mainlayout)

        # self.createPageConnection()

    def createPageConnection(self):
        for buttonID, button in views['NavgationBar'].buttons.items():
            button.clicked.connect(self.swicthPage)

    def swicthPage(self):
        buttons = views['NavgationBar'].buttons
        for key, page in self.pages.items():
            if buttons[key] is self.sender():
                self.stackwiaget.setCurrentWidget(page)
