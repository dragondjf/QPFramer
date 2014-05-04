#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from .menubar import MenuBar
from .statusbar import StatusBar
from .centerwindow import CenterWindow
from gui.uiconfig import windowsoptions
from gui.uiutil import set_skin, changebg
import gui.dialogs as dialogs
from .guiconfig import collectView, views


class MainWindow(QtWidgets.QMainWindow):

    viewID = "MainWindow"

    @collectView
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinimizeButtonHint)  # 无边框， 带系统菜单， 可以最小化

        self.initMainWindow()
        self.createCenterWindow()
        self.createMenus()
        self.createToolbars()
        self.createStatusbar()
        self.setskin()

    def initMainWindow(self):
        mainwindowSettings = windowsoptions['mainwindow']
        title = mainwindowSettings['title']
        minsize = mainwindowSettings['minsize']
        size = mainwindowSettings['size']
        windowicon = mainwindowSettings['icon']
        fullscreenflag = mainwindowSettings['fullscreenflag']

        desktopWidth = QtWidgets.QDesktopWidget().availableGeometry().width()
        desktopHeight = QtWidgets.QDesktopWidget().availableGeometry().height()

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(windowicon))  # 设置程序图标
        self.setMinimumSize(minsize[0]*desktopWidth, minsize[1]*desktopHeight)
        self.resize(size[0]*desktopWidth, size[1]*desktopHeight)

        self.moveCenter()  # 将窗口固定在屏幕中间
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.fullscreenflag = fullscreenflag  # 初始化时非窗口最大话标志

    def createCenterWindow(self):
        self.centeralwindow = CenterWindow(self)
        self.setCentralWidget(self.centeralwindow)

    def createMenus(self):
        menubar = MenuBar(self)
        self.setMenuBar(menubar)

    def createToolbars(self):
        pass

    def createStatusbar(self):
        statusbar = StatusBar(self)
        self.setStatusBar(statusbar)

    def setskin(self):
        set_skin(self, 'gui/skin/qss/main.qss')  # 设置主窗口样式
        changebg(self, windowsoptions['frameqss'])

    def moveCenter(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif event.key() == QtCore.Qt.Key_F11:
            views['TitleBar'].actionMax()
        elif event.key() == QtCore.Qt.Key_F9:
            bar = self.menuBar()
            bar.setVisible(not bar.isVisible())
        elif event.key() == QtCore.Qt.Key_F8:
            bar = self.statusBar()
            bar.setVisible(not bar.isVisible())

    def mousePressEvent(self, event):
        # 鼠标点击事件
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseReleaseEvent(self, event):
        # 鼠标释放事件
        if hasattr(self, "dragPosition"):
            del self.dragPosition

    def mouseMoveEvent(self, event):
        # 鼠标移动事件
        if hasattr(self, "dragPosition"):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()

    def closeEvent(self, evt):
        flag, exitflag = dialogs.exit(windowsoptions['exitdialog'])
        if flag:
            for item in exitflag:
                if item == 'minRadio' and exitflag[item]:
                    self.showMinimized()
                    evt.ignore()
                elif item == 'exitRadio' and exitflag[item]:
                    evt.accept()
                elif item == 'exitsaveRadio' and exitflag[item]:
                    evt.accept()
                    self.saveoptions()
                    if not os.path.exists("options"):
                        os.mkdir("options")
                    with open("options\windowsoptions.json", 'w') as f:
                        json.dump(windowsoptions, f, indent=4)
        else:
            evt.ignore()

    def saveoptions(self):
        from gui.uiconfig import windowsoptions
        windowsoptions['mainwindow']['fullscreenflag'] = self.isFullScreen()
