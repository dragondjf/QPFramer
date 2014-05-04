#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from .guiconfig import collectView


class BaseToolButton(QtWidgets.QPushButton):
    """docstring for BaseButton"""

    def __init__(self, text, parent=None):
        super(BaseToolButton, self).__init__()
        self.parent = parent
        self.setFlat(True)
        self.setCheckable(True)
        self.setFixedSize(80, 60)
        self.setText(text)


class NavgationBar(QtWidgets.QFrame):

    viewID = "NavgationBar"

    @collectView
    def __init__(self, parent=None):
        super(NavgationBar, self).__init__(parent)
        self.setObjectName("NavgationBar")
        self.initData()
        self.initUI()

    def initData(self):
        self.buttons = {}

    def initUI(self):
        baseHeight = 66
        self.setFixedHeight(baseHeight)
        self.monitorButton = BaseToolButton(self.tr("监控管理"))
        self.monitorButton.setObjectName("monitor")
        self.monitorButton.setChecked(True)
        self.alarmListButton = BaseToolButton(self.tr("历史告警"))
        self.alarmListButton.setObjectName("alarmList")

        self.aboutButton = BaseToolButton(self.tr("关于我们"))
        self.aboutButton.setObjectName("about")

        self.exitButton = BaseToolButton(self.tr("退出程序"))
        self.exitButton.setObjectName("exit")

        self.buttons.update({"monitor": self.monitorButton})
        self.buttons.update({"alarmList": self.alarmListButton})
        self.buttons.update({"about": self.aboutButton})
        self.buttons.update({"exit": self.exitButton})

        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(self.monitorButton)
        mainLayout.addWidget(self.alarmListButton)
        mainLayout.addWidget(self.aboutButton)
        mainLayout.addWidget(self.exitButton)        
        mainLayout.addStretch()
        mainLayout.setContentsMargins(10, 0, 0, 0)
        mainLayout.setSpacing(1)
        self.setLayout(mainLayout)

        for buttonId, button in self.buttons.items():
            button.clicked.connect(self.checkedButton)

    def checkedButton(self):
        self.sender().setChecked(True)
        for buttonId, button in self.buttons.items():
            if button is not self.sender():
                button.setChecked(False)
