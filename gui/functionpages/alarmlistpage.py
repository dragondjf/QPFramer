#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from gui.mainwindow import collectView
# from gui.mainwindow.guimanger import signal_DB, status_color, status_name_zh


class AlarmListPage(QtWidgets.QFrame):

    viewID = "AlarmListPage"

    @collectView
    def __init__(self, parent=None):
        super(AlarmListPage, self).__init__(parent)
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        alarmBar = AlarmBar(self)
        alarmTable = AlarmTable(self)

        mainlayout = QtWidgets.QVBoxLayout()
        mainlayout.addWidget(alarmBar)
        mainlayout.addWidget(alarmTable)
        mainlayout.addSpacing(5)
        mainlayout.setContentsMargins(0, 2, 0, 0)
        mainlayout.setSpacing(0)
        self.setLayout(mainlayout)

class AlarmBar(QtWidgets.QFrame):

    viewID = "AlarmBar"

    @collectView
    def __init__(self, parent=None):
        super(AlarmBar, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setFixedHeight(30)


class AlarmTable(QtWidgets.QTableWidget):

    viewID = "AlarmTable"

    @collectView
    def __init__(self, parent=None):
        super(AlarmTable, self).__init__(parent)
        self.parent = parent
        self.setObjectName("AlarmTable")
        # self.setEditTriggers(self.DoubleClicked)
        self.setEditTriggers(self.NoEditTriggers)
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalHeader().setVisible(False)

        self.initHeader()
        self.initColumnWidth()

        # signal_DB.alarm_sin.connect(self.addItem)

    def initHeader(self):
        self.setColumnCount(7)
        headerview = QtWidgets.QHeaderView(QtCore.Qt.Horizontal, self)
        self.setHorizontalHeader(headerview)
        self.setHorizontalHeaderLabels(['告警编号', '告警类型', '采集器', '防区', '发生时间', '备注', '是否确认'])

    def initColumnWidth(self):
        self.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Fixed)
