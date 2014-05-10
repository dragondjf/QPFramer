#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import collections
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from .navgationbar import NavgationBar
from .titlebar import TitleBar
from .guiconfig import collectView, views
from gui.functionpages import QssMakerPage, AboutPage, QWebBrowserPage, QmlViewer


buttonIds = ['Home', 'QssMaker', 'Qexer', 'QtWebkit', 'QmlViewer', 'About', 'Exit']

mapButtonPage = collections.OrderedDict({
    'QssMaker': QssMakerPage,
    'About': AboutPage,
    'QtWebkit': QWebBrowserPage,
    'QmlViewer': QmlViewer
})


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

        self.titlebar = TitleBar(self)
        self.navgationbar = NavgationBar(buttonIds, self)

        self.stackwiaget = QtWidgets.QStackedWidget()

        for key, classPage in mapButtonPage.items():
            if hasattr(classPage, 'viewID'):
                setattr(self, classPage.viewID, classPage())
                page = getattr(self, classPage.viewID)
                self.stackwiaget.addWidget(page)
                self.pages.update({key: page})

        mainlayout = QtWidgets.QVBoxLayout()
        mainlayout.addWidget(self.titlebar)
        mainlayout.addWidget(self.navgationbar)
        mainlayout.addWidget(self.stackwiaget)
        # mainlayout.addStretch()
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.setSpacing(0)
        self.setLayout(mainlayout)

        self.createPageConnection()

    def createPageConnection(self):
        for buttonID, button in self.navgationbar.buttons.items():
            button.clicked.connect(self.swicthPage)

    def swicthPage(self):
        buttons = self.navgationbar.buttons
        for key, page in self.pages.items():
            if buttons[key] is self.sender():
                self.stackwiaget.setCurrentWidget(page)
