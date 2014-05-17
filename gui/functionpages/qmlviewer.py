#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtQuick
from PyQt5 import QtWidgets
from gui.mainwindow import collectView


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

    def creatContainer(self):
        self.view = QuickViwer()
        self.container = self.createWindowContainer(self.view, self)

    def initUI(self):
        # self.resize(400, 300)
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.container)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view = QmlViwer()
    view.show()
    sys.exit(app.exec_())
