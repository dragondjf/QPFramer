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
    def __init__(self, buttonIds, parent=None):
        super(NavgationBar, self).__init__(parent)
        self.parent = parent
        self.setObjectName("NavgationBar")
        self.buttonIds = buttonIds
        self.initData()
        self.initUI()

    def initData(self):
        self.buttons = {}

    def initUI(self):
        baseHeight = 66
        self.setFixedHeight(baseHeight)
        mainLayout = QtWidgets.QHBoxLayout()
        for buttonId in self.buttonIds:
            setattr(self, "%sButton" % buttonId, BaseToolButton(buttonId))
            button = getattr(self, "%sButton" % buttonId)
            button.setObjectName(buttonId)
            mainLayout.addWidget(button)
            self.buttons.update({buttonId: button})

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
