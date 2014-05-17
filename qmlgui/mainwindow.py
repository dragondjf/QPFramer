#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtQuick


class MainWindow(QtQuick.QQuickView):
    """docstring for MainWindow"""
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
        self.setResizeMode(QtQuick.QQuickView. SizeViewToRootObject)
        self.setFlags(QtCore.Qt.FramelessWindowHint)

        self.statusChanged.connect(self.trackStatus)
        self.setSource(QtCore.QUrl('application/appquick.qml'))

    def trackStatus(self, status):
        if status == QtQuick.QQuickView.Null:
            print('This QQuickView has no source set.')
        elif status == QtQuick.QQuickView.Ready:
            print('This QQuickView has loaded and created the QML component.')
        elif status == QtQuick.QQuickView.Loading:
            print('This QQuickView is loading network data.')
        elif status == QtQuick.QQuickView.Error:
            print('One or more errors has occurred. Call errors() to retrieve a list of errors.')
            print(self.errors())

    def mousePressEvent(self, event):
        # 鼠标点击事件
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
        super(MainWindow, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # 鼠标释放事件
        if hasattr(self, "dragPosition"):
            del self.dragPosition
        super(MainWindow, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        # 鼠标移动事件
        if hasattr(self, "dragPosition"):
            if event.buttons() == QtCore.Qt.LeftButton:
                currentPos = event.globalPos() - self.dragPosition
                self.setX(currentPos.x())
                self.setY(currentPos.y())
                event.accept()
        super(MainWindow, self).mouseMoveEvent(event)
