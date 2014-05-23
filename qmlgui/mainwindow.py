#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtQuick


class MainWindow(QtQuick.QQuickView):
    """docstring for MainWindow"""
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.setResizeMode(QtQuick.QQuickView.SizeViewToRootObject)
        self.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
        self.screensize = self.screen().availableSize()

        self.engine().addImportPath(os.sep.join([os.getcwd(), 'qml']))

        self.fullScreenFlag = False
        self.maxFlg = False
        self.setFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setIcon(QtGui.QIcon('application/images/png/QFramer.png'))
        self.setTitle("QFramer")

        context = self.rootContext()
        context.setContextProperty("mainconfig", MainConfig(self))
        self.statusChanged.connect(self.trackStatus)

        self.engine().quit.connect(QtGui.QGuiApplication.instance().quit)
        
    def loadMainWindow(self):
        # self.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
        self.setSource(QtCore.QUrl('application/appquick.qml'))
        self.rootobj = self.rootObject()
        self.rootobj.minClicked.connect(self.showMinimized)
        self.rootobj.maxClicked.connect(self.showWindow)
        self.rootobj.fullscreen.connect(self.fullscreen)
        self.prefersize = self.size()
        self.show()

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
        if hasattr(self, "dragPosition") and not self.fullScreenFlag and not self.maxFlg:
            if event.buttons() == QtCore.Qt.LeftButton:
                currentPos = event.globalPos() - self.dragPosition
                if event.pos().y() < 40:
                    self.setX(currentPos.x())
                    self.setY(currentPos.y())
                    event.accept()
        super(MainWindow, self).mouseMoveEvent(event)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F5:
            print('121212')
        super(MainWindow, self).keyPressEvent(event)

    def fullscreen(self):
        self.fullScreenFlag = not self.fullScreenFlag
        if self.fullScreenFlag:
            self.showFullScreen()
        else:
            self.showNormal()

    def showWindow(self):
        self.maxFlg = not self.maxFlg
        if self.maxFlg:
            self.setGeometry(0, 0, self.screensize.width(), self.screensize.height())
            self.resize(self.screen().availableSize())
        else:
            self.resize(self.prefersize)
            self.moveCenter()

    def moveCenter(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.setPosition(qr.topLeft())


class MainConfig(QtCore.QObject):

    titleChanged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MainConfig, self).__init__(parent)
        self.parent = parent
        self._title = self.parent.title()

    @QtCore.pyqtProperty(str, notify=titleChanged)
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @QtCore.pyqtSlot(int, result=str)
    def returnValue(self, value):
        """
        功能: 创建一个槽
        参数: 整数value
        返回值: 字符串
        """
        return width
