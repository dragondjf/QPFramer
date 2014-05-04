#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from datetime import datetime
from .guiconfig import collectView


class StatusBar(QtWidgets.QStatusBar):

    viewID = "StatusBar"

    @collectView
    def __init__(self, parent=None):
        super(StatusBar, self).__init__(parent)
        self.parent = parent
        self.initStatusbar()
        self.initUI()
        self.startTimer(1000)

    def initStatusbar(self):
        statusbarSettings = {
            'initmessage': u'Ready',
            'minimumHeight': 30,
            'visual': True,
        }
        self.showMessage(statusbarSettings['initmessage'])
        self.setMinimumHeight(statusbarSettings['minimumHeight'])
        self.setVisible(statusbarSettings['visual'])

    def initUI(self):
        self.datatimelabel = QtWidgets.QLabel(self)
        self.datatimelabel.setObjectName("datatimelabel")
        self.datatimelabel.setText(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        self.datatimelabel.show()
        self.addPermanentWidget(self.datatimelabel)

    def timerEvent(self, event):
        self.datatimelabel.setText(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
