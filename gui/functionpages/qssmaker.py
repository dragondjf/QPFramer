#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from gui.mainwindow import collectView, views
from gui.uiconfig import windowsoptions


class QssMaker(QtWidgets.QFrame):

    viewID = "QssMaker"

    @collectView
    def __init__(self, parent=None):
        super(QssMaker, self).__init__(parent)
        self.parent = parent
        self.setObjectName("QssMaker")
        self.initUI()

    def initUI(self):
        mainlayout = QtWidgets.QHBoxLayout()
        # mainlayout.addWidget(self.congig)
        # mainlayout.addWidget(self.stackwiaget)
        # mainlayout.addStretch()
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.setSpacing(0)
