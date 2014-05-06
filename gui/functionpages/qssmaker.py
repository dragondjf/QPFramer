#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from gui.mainwindow import collectView, views
from gui.uiconfig import windowsoptions


class QssMakerPage(QtWidgets.QFrame):

    viewID = "QssMakerPage"

    @collectView
    def __init__(self, parent=None):
        super(QssMakerPage, self).__init__(parent)
        self.parent = parent
        self.setObjectName("QssMakerPage")
        self.initUI()

    def initUI(self):
        mainlayout = QtWidgets.QHBoxLayout()
        # mainlayout.addWidget(self.congig)
        # mainlayout.addWidget(self.stackwiaget)
        # mainlayout.addStretch()
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.setSpacing(0)
