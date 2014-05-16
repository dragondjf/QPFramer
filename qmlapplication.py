#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtQml
from PyQt5 import QtQuick

if __name__ == '__main__':
    app = QtGui.QGuiApplication(sys.argv)

    engine = QtQml.QQmlApplicationEngine()
    engine.load("application/gallery/main.qml")
    quickwindow = engine.rootObjects()[0]
    quickwindow.show()

    sys.exit(app.exec_())
