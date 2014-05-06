#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from gui.resources import *
from gui.mainwindow.guiconfig import views


class SettingsMenu(QtWidgets.QMenu):

    """docstring for SettingsMenu"""

    def __init__(self, parent=None):
        super(SettingsMenu, self).__init__(parent)
        self.parent = parent
        self.initUI()
        self.initConnect()
        getattr(self, '%sAction' % 'English').setChecked(True)

    def initUI(self):
        self.actionlists = {}

        self.actions = [
            {
                'name': self.tr('Settings'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'Settings',
            },
            {
                'name': self.tr('Language'),
                'trigger': 'Language',
                'type': 'submenu',
                'actions': [
                    {
                        'name': 'English',
                        'icon': u'',
                        'shortcut': u'',
                        'trigger': 'English',
                        "checkable": True
                    },
                    {
                        'name': '中文',
                        'icon': u'',
                        'shortcut': u'',
                        'trigger': 'Chinese',
                        "checkable": True
                    },
                ]
            },
            {
                'name': self.tr('Exit'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'Exit',
            },
        ]
        self.creatMenus(self.actions)

    def initConnect(self):
        for item in ['English', 'Chinese']:
            getattr(self, '%sAction' % item).triggered.connect(self.updateChecked)
        getattr(self, '%sAction' % 'Exit').triggered.connect(views['MainWindow'].close)

    def updateChecked(self):
        for item in ['English', 'Chinese']:
            action = getattr(self, '%sAction' % item)
            if self.sender() is action:
                action.setChecked(True)
            else:
                action.setChecked()

    def creatMenus(self, menusettings):
        for menuaction in menusettings:
            if 'type' in menuaction and menuaction['type'] == "submenu":
                self.createSubAction(menuaction['trigger'], menuaction)
            else:
                self.creatAction(self, menuaction)

    def createSubAction(self, pmenu_name, menu):
        submenu = self.addMenu(u'%s' % menu['name'])
        setattr(
            self,
            '%smenu' % menu['trigger'],
            submenu)
        for menuaction in menu['actions']:
            self.creatAction(submenu, menuaction)

    def creatAction(self, submenu, menuaction):
        if 'checkable' in menuaction:
            setattr(
                self,
                '%sAction' % menuaction['trigger'],
                QtWidgets.QAction(
                    QtGui.QIcon(QtGui.QPixmap(menuaction['icon'])),
                    u'%s' % menuaction['name'],
                    self,
                    checkable=menuaction['checkable']
                )
            )
        else:
            setattr(
                self,
                '%sAction' % menuaction['trigger'],
                QtWidgets.QAction(
                    QtGui.QIcon(QtGui.QPixmap(menuaction['icon'])),
                    u'%s' % menuaction['name'],
                    self,
                )
            )

        action = getattr(self, '%sAction' % menuaction['trigger'])
        action.setShortcut(QtGui.QKeySequence(menuaction['shortcut']))
        submenu.addAction(action)
        self.actionlists.update({menuaction['trigger']: action})
