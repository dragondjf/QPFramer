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
        self.setSource(QtCore.QUrl.fromLocalFile('gui/qml/tiger/tiger.qml'))


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
