#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtQuick


class SplashWindow(QtQuick.QQuickView):
    """docstring for SplashWindow"""
    def __init__(self, mainwindow):
        super(SplashWindow, self).__init__()
        # self.setResizeMode(QtQuick.QQuickView.SizeViewToRootObject)
        self.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
        self.screensize = self.screen().availableSize()

        self.engine().addImportPath(os.sep.join([os.getcwd(), 'qml']))

        self.setFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setIcon(QtGui.QIcon('application/images/png/QFramer.png'))
        self.setTitle("QFramer")

        self.setSource(QtCore.QUrl('application/component/Splash.qml'))
        splashrootobj = self.rootObject()
        splashrootobj.timeout.connect(mainwindow.loadMainWindow)
        splashrootobj.timeout.connect(self.close)
        self.show()
