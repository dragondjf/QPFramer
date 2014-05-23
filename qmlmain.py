#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtQuick
from qmlgui import MainWindow, SplashWindow

if __name__ == '__main__':
    app = QtGui.QGuiApplication(sys.argv)

    main = MainWindow()
    splashwindow = SplashWindow(main)
    sys.exit(app.exec_())
