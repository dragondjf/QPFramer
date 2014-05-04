#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from gui import MainWindow, GuiManger
from gui import SplashScreen
from gui.uiconfig import windowsoptions


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    if windowsoptions['splashflag']:
        splash = SplashScreen(QtGui.QPixmap(windowsoptions['splashimg']))
        splash.fadeTicker(1)
        app.processEvents()
        mainwindow = MainWindow()
        guimanger = GuiManger()
        mainwindow.show()
        splash.finish(mainwindow)
    else:
        mainwindow = MainWindow()
        guimanger = GuiManger()
        mainwindow.show()
    sys.exit(app.exec_())
