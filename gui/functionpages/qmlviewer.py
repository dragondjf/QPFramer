#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtQuick
from PyQt5 import QtWidgets
from gui.mainwindow import collectView
from gui.resources import *


class QuickViwer(QtQuick.QQuickView):
    """docstring for QuickViwer"""

    def __init__(self, parent=None):
        super(QuickViwer, self).__init__(parent)
        self.setResizeMode(self.SizeRootObjectToView)
        self.con = MyClass()
        context = self.rootContext()
        context.setContextProperty("myclass", self.con)
        self.setSource(QtCore.QUrl.fromLocalFile('gui/qml/demo.qml'))
        rootobj = self.rootObject()
        rootobj.clicked.connect(self.on_qml_mouse_clicked)
        rootobj.changeText('Do it well', 'green')

        self.statusChanged.connect(self.trackStatus)

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

    def on_qml_mouse_clicked(self):
        print('mouse clicked')


width = '''class QuickViwer(QtQuick.QQuickView):
    """docstring for QuickViwer"""

    def __init__(self, parent=None):
        super(QuickViwer, self).__init__(parent)
        self.setResizeMode(self.SizeRootObjectToView)
        con = MyClass()
        context = self.rootContext()
        context.setContextProperty("myclass", width)
        self.setSource(QtCore.QUrl.fromLocalFile('gui/qml/demo.qml'))
        rootobj = self.rootObject()
        rootobj.clicked.connect(self.on_qml_mouse_clicked)
        rootobj.test()'''

class MyClass(QtCore.QObject):

    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self._name = '545454545454'

    @QtCore.pyqtProperty(str)
    def name(self):
        return self._name

    @QtCore.pyqtSlot(int, result=str)
    def returnValue(self, value):
        """
        功能: 创建一个槽
        参数: 整数value
        返回值: 字符串
        """
        return width


class QmlViewer(QtWidgets.QFrame):

    viewID = "QmlViewer"

    @collectView
    def __init__(self, parent=None):
        super(QmlViewer, self).__init__(parent)
        self.parent = parent
        self.setObjectName("QmlViewer")
        self.creatContainer()
        self.initUI()
        self.initConnect()

    def creatContainer(self):
        self.view = QuickViwer()
        self.container = self.createWindowContainer(self.view, self)

    def initUI(self):
        # self.resize(400, 300)
        self.qmlopenIcon = QtGui.QIcon(":/icons/dark/appbar.upload.png")
        iconBaseSize = QtCore.QSize(20, 20)

        navLayout = QtWidgets.QHBoxLayout()
        self.urlLineEdit = QtWidgets.QLineEdit()
        self.urlLineEdit.setFixedHeight(25)

        self.openqmlButton = QtWidgets.QToolButton()
        self.openqmlButton.setIcon(self.qmlopenIcon)
        self.openqmlButton.setIconSize(iconBaseSize)
        navLayout.addWidget(self.openqmlButton)
        navLayout.addWidget(self.urlLineEdit)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(navLayout)
        mainLayout.addWidget(self.container)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)

    def initConnect(self):
        self.openqmlButton.clicked.connect(self.getQmlUrl)
        self.urlLineEdit.editingFinished.connect(self.loadQML)
        self.urlLineEdit.returnPressed.connect(self.loadQML)
        self.urlLineEdit.textChanged.connect(self.loadQML)

    def getQmlUrl(self):
        self.qmlurl = QtWidgets.QFileDialog.getOpenFileName(self,
            self.tr("Open QML"), os.sep.join([os.getcwd(), 'gui', 'qml']) , self.tr("QML Files (*.qml)"))[0]
        self.urlLineEdit.setText(self.qmlurl)

    def loadQML(self):
        try:
            self.view.setSource(QtCore.QUrl.fromLocalFile(self.urlLineEdit.text()))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view = QmlViwer()
    view.show()
    sys.exit(app.exec_())
