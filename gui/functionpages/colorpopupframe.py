#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from gui.mainwindow import collectView, views
from gui.uiconfig import windowsoptions
from gui.uiconfig import makeFrameQss

def set_skin(widget, qssfile):
    if os.path.exists(qssfile):
        fd = open(qssfile, "r")
        style = fd.read()
        fd.close()
        widget.setStyleSheet(style)


class ColorLabel(QtWidgets.QLabel):

    def __init__(self, color, parent=None):
        super(ColorLabel, self).__init__(parent)
        self.parent = parent
        self.setFixedHeight(self.parent.height() / 2 - 2)
        self.setStyleSheet('''QLabel{background-color:%s}'''% color)
        self.bgcolor = color
        self.setAttribute(QtCore.Qt.WA_Hover)
        self.installEventFilter(self.parent)


class ColorPopupFrame(QtWidgets.QFrame):

    viewID = "ColorPopupFrame"

    @collectView
    def __init__(self, parent=None):
        super(ColorPopupFrame, self).__init__(parent)
        self.parent = parent
        self.setWindowFlags(QtCore.Qt.Popup)
        self.initData()
        self.initUI()
        self.initConnect()
        
        if 'TitleBar' in views:
            p = views['TitleBar'].mapToGlobal(views['TitleBar'].skinButton.pos())
            xpos = p.x() - self.width()
            ypos = p.y() + views['TitleBar'].height()
        else:
            xpos = QtGui.QCursor.pos().x() - self.width()
            ypos = QtGui.QCursor.pos().y() + 20
        self.move(QtCore.QPoint(xpos, ypos))
        self.installEventFilter(self)

    def initData(self):
        self.color = {
            'bg1': 'rgb(54, 178, 230)',
            'bg2': 'rgb(55, 56, 57)',
            'bg3': 'rgb(41, 153, 66)',
            'bg4': 'rgb(212, 200, 30)',
            'bg5': 'rgb(219, 68, 68)',
        }
        self.bgcolor = None

    def initUI(self):
        # 主布局
        self.resize(200, 100)
        self.bgLabel1 = ColorLabel(self.color['bg1'], self)

        self.bgLabel2 = ColorLabel(self.color['bg2'], self)

        self.bgLabel3 = ColorLabel(self.color['bg3'], self)

        self.bgLabel4 = ColorLabel(self.color['bg4'], self)

        self.bgLabel5 = ColorLabel(self.color['bg5'], self)

        self.customColorButton = QtWidgets.QPushButton(self.tr("自定义"))
        self.customColorButton.setFixedHeight(self.height() / 2 - 2)
        self.customColorButton.setObjectName("customColorButton")

        mainlayout = QtWidgets.QGridLayout()
        mainlayout.addWidget(self.bgLabel1, 0, 0)
        mainlayout.addWidget(self.bgLabel2, 0, 1)
        mainlayout.addWidget(self.bgLabel3, 0, 2)
        mainlayout.addWidget(self.bgLabel4, 1, 0)
        mainlayout.addWidget(self.bgLabel5, 1, 1)
        mainlayout.addWidget(self.customColorButton, 1, 2)
        mainlayout.setContentsMargins(2, 2, 2, 2)
        mainlayout.setSpacing(0)
        self.setLayout(mainlayout)

    def initConnect(self):
        self.customColorButton.clicked.connect(self.customColor)

    def customColor(self):

        colordialog = QtWidgets.QColorDialog(QtGui.QColor("green"))
        colordialog.colorSelected.connect(self.updateBg)
        colordialog.exec_()

    def updateBg(self, color):
        self.bgcolor = 'rgb(%s, %s, %s)' % (color.red(), color.green(), color.blue())
        windowsoptions['frameqss'] = makeFrameQss(self.bgcolor)
        views['MainWindow'].setskin()

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

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            self.close()
            return  True
        elif isinstance(event, QtGui.QHoverEvent):
            if self.bgcolor != obj.bgcolor:
                self.bgcolor = obj.bgcolor
                windowsoptions['frameqss'] = makeFrameQss(obj.bgcolor)
                views['MainWindow'].setskin()
            return  False
        else:
            return super(ColorPopupFrame, self).eventFilter(obj, event)
