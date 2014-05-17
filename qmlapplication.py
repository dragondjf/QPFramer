#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtQml
from PyQt5 import QtQuick


class MainWindow(QtQuick.QQuickWindow):
    """docstring for MainWindow"""
    def __init__(self, qwindow=None):
        super(MainWindow, self).__init__(qwindow)
        # self.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
        # self.setResizeMode(QtQuick.QQuickView. SizeViewToRootObject)
        # self.setFlags(QtCore.Qt.FramelessWindowHint)

        # self.statusChanged.connect(self.trackStatus)
        # self.setSource(QtCore.QUrl('application/appquick.qml'))

    # def trackStatus(self, status):
    #     if status == QtQuick.QQuickView.Null:
    #         print('This QQuickView has no source set.')
    #     elif status == QtQuick.QQuickView.Ready:
    #         print('This QQuickView has loaded and created the QML component.')
    #     elif status == QtQuick.QQuickView.Loading:
    #         print('This QQuickView is loading network data.')
    #     elif status == QtQuick.QQuickView.Error:
    #         print('One or more errors has occurred. Call errors() to retrieve a list of errors.')
    #         print(self.errors())

    # def mousePressEvent(self, event):
    #     # 鼠标点击事件
    #     if event.button() == QtCore.Qt.LeftButton:
    #         self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
    #         event.accept()
    #     super(MainWindow, self).mousePressEvent(event)

    # def mouseReleaseEvent(self, event):
    #     # 鼠标释放事件
    #     if hasattr(self, "dragPosition"):
    #         del self.dragPosition
    #     super(MainWindow, self).mouseReleaseEvent(event)

    # def mouseMoveEvent(self, event):
    #     # 鼠标移动事件
    #     if hasattr(self, "dragPosition"):
    #         if event.buttons() == QtCore.Qt.LeftButton:
    #             currentPos = event.globalPos() - self.dragPosition
    #             self.setX(currentPos.x())
    #             self.setY(currentPos.y())
    #             event.accept()
    #     super(MainWindow, self).mouseMoveEvent(event)


if __name__ == '__main__':
    app = QtGui.QGuiApplication(sys.argv)

    engine = QtQml.QQmlApplicationEngine()
    engine.load("application/appwindow.qml")
    quickwindow = engine.rootObjects()[0]

    # a = engine.rootObjects()[0]

    # a = QtQuick.QQuickWindow()
    # quickwindow = MainWindow(qwindow)
    quickwindow.setIcon(QtGui.QIcon('application/images/png/QFramer.png'))
    quickwindow.show()
    # quickwindow.setSource(QtCore.QUrl('application/appquick.qml'))
    # a.show()

    sys.exit(app.exec_())
