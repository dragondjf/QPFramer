#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from qmlgui import MainWindow

if __name__ == '__main__':
    app = QtGui.QGuiApplication(sys.argv)

    main = MainWindow()
    main.engine().quit.connect(app.quit)
    main.show()

    sys.exit(app.exec_())
