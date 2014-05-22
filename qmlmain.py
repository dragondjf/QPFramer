#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from qmlgui import MainWindow

if __name__ == '__main__':
    app = QtGui.QGuiApplication(sys.argv)

    main = MainWindow()
    main.engine().quit.connect(app.quit)
    
    print(main.engine().importPathList())
    print(main.engine().pluginPathList())
    main.show()

    sys.exit(app.exec_())
