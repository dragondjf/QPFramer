#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from gui.mainwindow import collectView, views
from gui.uiconfig import windowsoptions
from dataBase import signal_DB
from gui.mainwindow.qrc_icons import *


class Splitter(QtWidgets.QSplitter):

    def __init__(self, parent=None):
        super(Splitter, self).__init__(parent)

        if 'pawidth' not in windowsoptions:
            windowsoptions['pawidth'] = views['MainWindow'].width() * 0.22

        self.paListPanel = PATable(self)
        self.paListPanel.setFixedWidth(windowsoptions['pawidth'])

        self.mapPanel = MapPanel(self)

        self.addWidget(self.paListPanel)
        self.addWidget(self.mapPanel)
        self.setContentsMargins(0, 0, 0, 0)


class PATable(QtWidgets.QTableWidget):

    viewID = "PATable"

    iconsize = 36
    setting_size = 48
    video_column = 3
    settting_column = 4


    @collectView
    def __init__(self, parent=None):
        super(PATable, self).__init__(parent)
        self.parent = parent
        self.setShowGrid(False)
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setEditTriggers(self.NoEditTriggers)
        self.setIconSize(QtCore.QSize(self.iconsize, self.iconsize))

        self.initData()
        self.initHeader()
        self.initColumnWidth()
        self.initConnect()

    def initData(self):
        self.redPixmap = QtGui.QIcon("gui/skin/images/colorball3/red.png")
        self.greenPixmap = QtGui.QIcon("gui/skin/images/colorball3/green.png")
        self.yellowPixmap = QtGui.QIcon("gui/skin/images/colorball3/yellow.png")
        self.grayPixmap = QtGui.QIcon("gui/skin/images/colorball3/gray.png")
        self.colors = {
            'red': self.redPixmap,
            'green': self.greenPixmap,
            'yellow': self.yellowPixmap,
            'gray': self.grayPixmap
        }

    def initHeader(self):
        self.setColumnCount(5)
        self.horizontalHeader().hide()
        self.verticalHeader().hide()
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def initColumnWidth(self):
        self.setColumnWidth(0, self.iconsize + 6)
        self.setColumnWidth(1, 48)
        self.setColumnWidth(3, self.setting_size)
        self.setColumnWidth(4, self.setting_size)
        self.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)

    def initConnect(self):
        # self.cellClicked.connect(self.action_cellClicked)
        pass

    def action_cellClicked(self, row, column):
        self.removeColumn(self.settting_column)
        self.insertColumn(self.settting_column)
        self.setColumnWidth(self.settting_column, self.setting_size)

        settingItem = QtWidgets.QPushButton("设置")
        settingItem.clicked.connect(self.clickSetting)
        self.setCellWidget(row, self.settting_column, settingItem)

    def clickSetting(self):
        for row in range(self.rowCount()):
            if self.cellWidget(row, self.settting_column) is self.sender():
                signal_DB.settingsIndex_sin.emit(row)

    def clickVedio(self):
        for row in range(self.rowCount()):
            if self.cellWidget(row, self.video_column) is self.sender():
                signal_DB.videoIndex_sin.emit(row)

    def changeColor(self, row, bgcolor):
        for col in range(self.columnCount()):
            item = self.item(row, col)
            if item:
                if col == 0:
                    item.setIcon(self.colors[bgcolor])
                else:
                    bgBrush = QtGui.QBrush(QtGui.QColor(bgcolor))
                    item.setBackground(bgBrush)

    def addItem(self, row, message, bgcolor="gray", fgcolor="white"):
        self.insertRow(row)
        bgBrush = QtGui.QBrush(QtGui.QColor(bgcolor))
        fgBrush = QtGui.QBrush(QtGui.QColor(fgcolor))
        self.setRowHeight(row, self.iconsize + 6)
        for col in range(self.columnCount()):
            if col == 0:
                item = QtWidgets.QTableWidgetItem("")
                item.setIcon(QtGui.QIcon(self.grayPixmap))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.setItem(row, col, item)
            if col == 1:
                item = QtWidgets.QTableWidgetItem(message[0])
                # item.setIcon(QtGui.QIcon(self.grayPixmap))
                item.setBackground(bgBrush)
                item.setForeground(fgBrush)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.setItem(row, col, item)
            elif col == 2:
                item = QtWidgets.QTableWidgetItem(message[1])
                item.setBackground(bgBrush)
                item.setForeground(fgBrush)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.setItem(row, col, item)
            elif col == self.video_column:
                settingItem = QtWidgets.QPushButton()
                settingItem.setStyleSheet('''
                    QPushButton{
                        border-image: url(:/icons/dark/appbar.monitor.play.png);
                    }
                    QPushButton:pressed{
                        border-image: url(:/icons/light/appbar.monitor.play.png);
                    }
                ''')
                settingItem.setToolTip(self.tr("视频"))
                settingItem.setFixedSize(48, 48)
                settingItem.clicked.connect(self.clickVedio)
                self.setCellWidget(row, col, settingItem)
            elif col == self.settting_column:
                settingItem = QtWidgets.QPushButton()
                settingItem.setStyleSheet('''
                    QPushButton{
                        border-image: url(:/icons/dark/appbar.settings.png);
                    }
                    QPushButton:pressed{
                        border-image: url(:/icons/light/appbar.settings.png);
                    }
                ''')
                settingItem.setToolTip(self.tr("设置"))
                settingItem.setFixedSize(48, 48)
                settingItem.clicked.connect(self.clickSetting)
                self.setCellWidget(row, col, settingItem)



class MonitorPage(QtWidgets.QFrame):

    viewID = "MonitorPage"

    @collectView
    def __init__(self, parent=None):
        super(MonitorPage, self).__init__(parent)
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        splitter = Splitter()
        mainlayout = QtWidgets.QVBoxLayout()
        mainlayout.addWidget(splitter)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.setSpacing(0)
        self.setLayout(mainlayout)


class MapPanel(QtWidgets.QFrame):

    viewID = "MapPanel"

    @collectView
    def __init__(self, parent=None):
        super(MapPanel, self).__init__(parent)
        self.parent = parent
        self.initData()
        self.createPAContextMenu()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.scene = DiagramScene(self.paContextMenu, self)
        self.view = MapGraphicsView(self)
        self.view.setScene(self.scene)

        mainlayout = QtWidgets.QVBoxLayout()
        mainlayout.addWidget(self.view)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.setSpacing(0)
        self.setLayout(mainlayout)

    def contextMenuEvent(self, event):
        if windowsoptions['MapMenuflag']:
            self.changeBackgroundAction = QtWidgets.QAction(self.tr("修改防区地图"), self, triggered=self.view.actionChangeBackground)
            self.getPAsAction = QtWidgets.QAction(self.tr("获取所有防区"), self, triggered=self.actionGetPAs)
            self.clearPAsAction = QtWidgets.QAction(self.tr("清除所有防区"), self, triggered=self.actionClearPAs)

            menu = QtWidgets.QMenu(self)
            menu.addAction(self.changeBackgroundAction)
            # menu.addAction(self.getPAsAction)
            # menu.addAction(self.clearPAsAction)
            menu.exec_(event.globalPos())

    def createPAContextMenu(self):
        if windowsoptions['PAMenuflag']:
            self.disabledAction = QtWidgets.QAction("禁用", self, triggered=self.actionDiabled)
            self.attributeAction = QtWidgets.QAction("属性", self, triggered=self.actionAttribute)
            self.paContextMenu = QtWidgets.QMenu(self)
            self.paContextMenu.addAction(self.disabledAction)
            self.paContextMenu.addAction(self.attributeAction)
        else:
            self.paContextMenu = QtWidgets.QMenu(self)

    def actionDiabled(self):
        pass

    def actionAttribute(self):
        pass

    def actionClearPAs(self):
        self.scene.clear()

    def actionGetPAs(self):
        # pas = []

        # for i in range(20):
        #    pa = {
        #         "x": i * 30,
        #         "y": i * 30,
        #         'name': "PA1"
        #    }
        #    pas.append(pa)

        # self.scene.createItems(pas)
        pass


class PAItem(QtWidgets.QGraphicsPixmapItem):

    size = 48

    def __init__(self, contextMenu, parent=None):
        super(PAItem, self).__init__(parent)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setTransformationMode(QtCore.Qt.SmoothTransformation)
        self.contextMenu = contextMenu
        self.initData()
        self.setPixmap(self.grayPixmap)

    def initData(self):
        self.redPixmap = QtGui.QPixmap("gui/skin/images/colorball3/red.png").scaled(self.size, self.size)
        self.greenPixmap = QtGui.QPixmap("gui/skin/images/colorball3/green.png").scaled(self.size, self.size)
        self.yellowPixmap = QtGui.QPixmap("gui/skin/images/colorball3/yellow.png").scaled(self.size, self.size)
        self.grayPixmap = QtGui.QPixmap("gui/skin/images/colorball3/gray.png").scaled(self.size, self.size)

        self.pixmaps = [
            self.grayPixmap, self.grayPixmap,
            self.greenPixmap, self.greenPixmap,
            self.redPixmap, self.yellowPixmap, self.redPixmap
        ]

    def contextMenuEvent(self, event):
        self.scene().clearSelection()
        self.setSelected(True)
        self.contextMenu.exec_(event.screenPos())

class PATextItem(QtWidgets.QGraphicsTextItem):

    def __init__(self, text, parent=None):
        super(PATextItem, self).__init__(parent)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setDefaultTextColor (QtGui.QColor('black'))
        self.setHtml("<h4>%s</h4>" % text)


class DiagramScene(QtWidgets.QGraphicsScene):

    itemInserted = QtCore.pyqtSignal(PAItem)

    itemSelected = QtCore.pyqtSignal(PAItem)

    viewID = "DiagramScene"

    @collectView
    def __init__(self, itemMenu, parent=None):
        super(DiagramScene, self).__init__(parent)
        self.itemMenu = itemMenu

    def mouseMoveEvent(self, event):
        for item in self.selectedItems():
            if item.pos().x() < 5:
                item.setX(5)
            elif item.pos().y() < 5:
                item.setY(5)
            elif item.pos().x() > self.width() - 69:
                item.setX(self.width() - 69)
            elif item.pos().y() > self.height() - 69:
                item.setY(self.height() - 69)
            else:
                super(DiagramScene, self).mouseMoveEvent(event)


class MapGraphicsView(QtWidgets.QGraphicsView):

    viewID = "MapGraphicsView"

    @collectView
    def __init__(self, parent=None):
        """
        QGraphicsView that will show an image scaled to the current widget size
        using events
        """
        self.parent = parent
        super(MapGraphicsView, self).__init__(parent)
        self.setDragMode(self.ScrollHandDrag)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setRubberBandSelectionMode(QtCore.Qt.ContainsItemShape)
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.BoundingRectViewportUpdate)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setResizeAnchor(self.AnchorUnderMouse)
        self.setCacheMode(QtWidgets.QGraphicsView.CacheBackground)

    def actionChangeBackground(self, firstFalg=False):
        if "viewbgfile" in windowsoptions:
            if firstFalg:
                bgfile = windowsoptions["viewbgfile"]
            else:
                bgfile = self.setOpenFileName()
        else:
            if firstFalg:
                return
            bgfile = self.setOpenFileName()

        if bgfile:
            windowsoptions["viewbgfile"] = bgfile
            self.initScene(bgfile)

    def initScene(self, bgfile):
        if views['MainWindow'].isFullScreen():
            self.viewWidth = self.parent.size().width()-5
            self.viewHeight = self.parent.size().height()-5
            windowsoptions["viewWidth"] = self.viewWidth
            windowsoptions["viewHeight"] = self.viewHeight
        else:
            if 'viewWidth' in windowsoptions:
                self.viewWidth = windowsoptions["viewWidth"]
                self.viewHeight = windowsoptions["viewHeight"]
            else:
                return
        self.scene().setSceneRect(QtCore.QRectF(0, 0, self.viewWidth, self.viewHeight))
        bgPixmap = QtGui.QPixmap(bgfile).scaled(self.viewWidth, self.viewHeight)
        bgBrush = QtGui.QBrush(bgPixmap)
        self.scene().setBackgroundBrush(bgBrush)

    def setOpenFileName(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                "QFileDialog.getOpenFileName()",
                self.tr("All(*); Images (*.png *.xpm *.jpg)"),options=options)
        if fileName:
            return fileName

    def resizeEvent(self, event):
        self.actionChangeBackground(True)
        super(MapGraphicsView, self).resizeEvent(event)
