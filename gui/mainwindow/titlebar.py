#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from .qrc_icons import *
from .guiconfig import collectView, views
from gui.uiconfig import __softwarename__ 

class TitleBar(QtWidgets.QFrame):

    viewID = "TitleBar"

    @collectView
    def __init__(self, parent=None):
        super(TitleBar, self).__init__(parent)

        self.setObjectName("TitleBar")
        self.initData()
        self.initUI()

    def initData(self):
        self.clothesIcon = QtGui.QIcon(":/icons/dark/appbar.clothes.shirt.png")
        self.minIcon = QtGui.QIcon(":/icons/dark/appbar.minus.png")
        self.maxIcon = QtGui.QIcon(":/icons/dark/appbar.fullscreen.box.png")
        self.normalIcon = QtGui.QIcon(":/icons/dark/appbar.app.png")
        self.closeIcon = QtGui.QIcon(":/icons/dark/appbar.close.png")

    def initUI(self):
        baseHeight = 20
        self.setFixedHeight(baseHeight)
        iconBaseSize = QtCore.QSize(20, baseHeight)

        self.titleLabel = QtWidgets.QLabel(__softwarename__)
        self.titleLabel.setObjectName("TitleLabel")

        self.skinButton = QtWidgets.QToolButton()
        self.skinButton.setIcon(self.clothesIcon)
        self.skinButton.setIconSize(iconBaseSize)

        self.minButton = QtWidgets.QToolButton()
        self.minButton.setIcon(self.minIcon)
        self.minButton.setIconSize(iconBaseSize)

        self.maxButton = QtWidgets.QToolButton()
        self.maxButton.setIconSize(iconBaseSize)
        self.initfullScreen()

        self.closeButton = QtWidgets.QToolButton()
        self.closeButton.setIconSize(iconBaseSize)
        self.closeButton.setIcon(QtGui.QIcon(":/icons/dark/appbar.close.png"))

        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(self.titleLabel)
        mainLayout.addStretch()
        mainLayout.addWidget(self.skinButton)
        mainLayout.addWidget(self.minButton)
        mainLayout.addWidget(self.maxButton)
        mainLayout.addWidget(self.closeButton)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)

        self.minButton.clicked.connect(self.actionMin)
        self.maxButton.clicked.connect(self.actionMax)
        self.closeButton.clicked.connect(self.actionClose)

    def initfullScreen(self):
        mainwindow = views['MainWindow']
        if mainwindow.fullscreenflag:
            mainwindow.showFullScreen()
            self.maxButton.setIcon(self.maxIcon)
        else:
            mainwindow.showNormal()
            self.maxButton.setIcon(self.normalIcon)

    def actionMin(self):
        mainwindow = views['MainWindow']
        mainwindow.showMinimized()

    def actionMax(self):
        mainwindow = views['MainWindow']
        if mainwindow.isFullScreen():
            mainwindow.showNormal()
            self.maxButton.setIcon(self.maxIcon)
        else:
            mainwindow.showFullScreen()
            self.maxButton.setIcon(self.normalIcon)

    def actionClose(self):
        mainwindow = views['MainWindow']
        mainwindow.close()

    def mouseDoubleClickEvent(self, event):
        self.actionMax()



class DialogTitleBar(QtWidgets.QFrame):

    def __init__(self, title='', parent=None):
        super(DialogTitleBar, self).__init__(parent)
        self.parent = parent
        self.title = title
        self.setObjectName("TitleBar")
        self.initData()
        self.initUI()

    def initData(self):
        self.minIcon = QtGui.QIcon(":/icons/dark/appbar.minus.png")
        self.maxIcon = QtGui.QIcon(":/icons/dark/appbar.fullscreen.box.png")
        self.normalIcon = QtGui.QIcon(":/icons/dark/appbar.app.png")
        self.closeIcon = QtGui.QIcon(":/icons/dark/appbar.close.png")

    def initUI(self):
        baseHeight = 20
        self.setFixedHeight(baseHeight)

        iconBaseSize = QtCore.QSize(20, baseHeight)
        self.minButton = QtWidgets.QToolButton()
        self.minButton.setIcon(self.minIcon)
        self.minButton.setIconSize(iconBaseSize)

        self.maxButton = QtWidgets.QToolButton()
        self.maxButton.setIconSize(iconBaseSize)
        self.maxButton.setIcon(self.normalIcon)

        self.closeButton = QtWidgets.QToolButton()
        self.closeButton.setIconSize(iconBaseSize)
        self.closeButton.setIcon(QtGui.QIcon(":/icons/dark/appbar.close.png"))

        self.titleLabel = QtWidgets.QLabel(self.title)

        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(self.titleLabel)
        mainLayout.addStretch()
        mainLayout.addWidget(self.minButton)
        mainLayout.addWidget(self.maxButton)
        mainLayout.addWidget(self.closeButton)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)

        self.minButton.clicked.connect(self.actionMin)
        self.maxButton.clicked.connect(self.actionMax)
        self.closeButton.clicked.connect(self.actionClose)

    def actionMin(self):
        mainwindow = self.parent
        mainwindow.showMinimized()

    def actionMax(self):
        mainwindow = self.parent
        if mainwindow.isFullScreen():
            mainwindow.showNormal()
            self.maxButton.setIcon(self.maxIcon)
        else:
            mainwindow.showFullScreen()
            self.maxButton.setIcon(self.normalIcon)

    def actionClose(self):
        mainwindow = self.parent
        mainwindow.close()

    def mouseDoubleClickEvent(self, event):
        self.actionMax()
