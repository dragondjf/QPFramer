#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtWebKitWidgets
from PyQt5 import QtWebKit
from PyQt5 import QtNetwork

class WebkitBasePage(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(WebkitBasePage, self).__init__(parent)
        self.parent = parent
        QtWebKit.QWebSettings.globalSettings().setAttribute(\
           QtWebKit.QWebSettings.PluginsEnabled, True)

        QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(True)

        self.view = QtWebKitWidgets.QWebView(self)
        self.view.setFocus()

        self.setupInspector()
        self.splitter = QtWidgets.QSplitter(self)
        self.splitter.setOrientation(QtCore.Qt.Vertical)

        self.splitter.addWidget(self.view)
        self.splitter.addWidget(self.webInspector)

        mainlayout = QtWidgets.QVBoxLayout(self)
        mainlayout.addWidget(self.splitter)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.setSpacing(0)
        self.setLayout(mainlayout)

    def setupInspector(self):
        page = self.view.page()
        page.settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)
        self.webInspector = QtWebKitWidgets.QWebInspector(self)
        self.webInspector.setPage(page)

        shortcut = QtWidgets.QShortcut(self)
        shortcut.setKey('F12')
        shortcut.activated.connect(self.toggleInspector)
        self.webInspector.setVisible(False)

    def toggleInspector(self):
        self.webInspector.setVisible(not self.webInspector.isVisible())
