#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore


class SignalDB(QtCore.QObject):

    # login_sin = QtCore.pyqtSignal(dict)
    # pas_sin = QtCore.pyqtSignal(list)
    # alarm_sin = QtCore.pyqtSignal(list)
    # simpleAlarm_sin = QtCore.pyqtSignal(dict)

    # settingsIndex_sin = QtCore.pyqtSignal(int)
    # videoIndex_sin = QtCore.pyqtSignal(int)

    def __init__(self):
        super(SignalDB, self).__init__()

signal_DB = SignalDB()
