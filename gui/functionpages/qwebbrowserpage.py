#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtWebKitWidgets
from gui.mainwindow import collectView
from .webkitbasepage import WebkitBasePage
from gui.resources import *


class QWebToolBar(QtWidgets.QToolBar):

    viewID = "QWebToolBar"

    @collectView
    def __init__(self, view, parent=None):
        super(QWebToolBar, self).__init__(parent)
        self.parent = parent
        self.view = view
        self.setObjectName("QWebToolBar")
        self.initData()
        self.initUI()
        self.initConnect()

    def initData(self):
        self.homeurl = "http://www.google.com.hk/"

    def initUI(self):
        baseheight = 30

        self.setFixedHeight(baseheight)
        self.progressbar = QtWidgets.QProgressBar(self)
        self.progressbar.setFixedHeight(baseheight-2)
        self.progressbar.setMaximum(100)
        self.progressbar.setMinimum(0)
        self.progressbar.setAlignment(QtCore.Qt.AlignLeft)

        self.locationEdit = QtWidgets.QLineEdit(self.homeurl, self.progressbar)
        self.locationEdit.move(0,0)

        self.setIconSize(QtCore.QSize(30, 30))
        self.backAction = self.view.pageAction(QtWebKitWidgets.QWebPage.Back)
        self.backAction.setIcon(QtGui.QIcon(":/icons/dark/appbar.arrow.left.png"))

        self.forwardAction = self.view.pageAction(QtWebKitWidgets.QWebPage.Forward)
        self.forwardAction.setIcon(QtGui.QIcon(":/icons/dark/appbar.arrow.right.png"))

        self.reloadAction = self.view.pageAction(QtWebKitWidgets.QWebPage.Reload)
        self.reloadAction.setIcon(QtGui.QIcon(":/icons/dark/appbar.refresh.png"))

        self.stopAction = self.view.pageAction(QtWebKitWidgets.QWebPage.Stop)
        self.stopAction.setIcon(QtGui.QIcon(":/icons/dark/appbar.home.png"))

        self.addAction(self.backAction)
        self.addAction(self.forwardAction)
        self.addAction(self.reloadAction)
        self.addAction(self.stopAction)
        self.addWidget(self.progressbar)

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        self.widgetForAction(self.backAction).setFixedSize(baseheight, baseheight)
        self.widgetForAction(self.forwardAction).setFixedSize(baseheight, baseheight)
        self.widgetForAction(self.reloadAction).setFixedSize(baseheight, baseheight)
        self.widgetForAction(self.stopAction).setFixedSize(baseheight, baseheight)

    def initConnect(self):
        self.stopAction.triggered.connect(self.goHome)

    def goHome(self):
        self.progressbar.setValue(0)
        self.locationEdit.setText(self.homeurl)
        self.locationEdit.returnPressed.emit()

    def resizeEvent(self, event):
        self.locationEdit.resize(self.progressbar.size())
        super(QWebToolBar, self).resizeEvent(event)


class QWebBrowserPage(WebkitBasePage):

    viewID = "QWebBrowserPage"

    @collectView
    def __init__(self, parent=None):
        super(QWebBrowserPage, self).__init__(parent)
        self.setObjectName("QWebBrowserPage")
        self.parent = parent
        self.initData()
        self.initUI()
        self.initConnect()

    def initData(self):
        pass

    def initUI(self):
        self.toolBar = QWebToolBar(self.view)
        self.layout().insertWidget(0, self.toolBar)

    def initConnect(self):
        self.view.loadFinished.connect(self.adjustLocation)
        self.view.loadProgress.connect(self.setProgress)
        self.view.loadFinished.connect(self.finishLoading)

        self.toolBar.locationEdit.returnPressed.connect(self.changeLocation)

        url = QtCore.QUrl(self.toolBar.homeurl)
        self.view.load(url)

    def changeLocation(self):
        url = QtCore.QUrl.fromUserInput(self.toolBar.locationEdit.text())
        self.view.load(url)
        self.view.setFocus()
        self.adjustLocation()
        
    def adjustLocation(self):
        try:
            self.toolBar.locationEdit.setText(self.toolBar.locationEdit.text())
        except Exception as e:
            print(e)

    def adjustTitle(self):
        # if 0 < self.progress < 100:
        #     self.setWindowTitle("%s (%s%%)" % (self.view.title(), self.progress))
        # else:
        #     self.setWindowTitle(self.view.title())
        if 0 < self.progress < 100:
            self.toolBar.progressbar.setValue(self.progress)
        else:
            self.toolBar.progressbar.hide()

    def setProgress(self, p):
        self.progress = p
        self.adjustTitle()

    def finishLoading(self):
        self.progress = 100
        self.adjustTitle()
