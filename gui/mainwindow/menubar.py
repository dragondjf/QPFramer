#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from .guiconfig import collectView


class MenuBar(QtWidgets.QMenuBar):

    viewID = "MenuBar"

    @collectView
    def __init__(self, parent):
        super(MenuBar, self).__init__()
        self.parent = parent
        self.actionlists = {}
        self.menusettings = {
            'visual': False,
            'menus': [
                {
                    'name': self.tr('File'),
                    'trigger': 'File',
                    'actions': [
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
                                    'name': 'Chinese',
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
                },
                {
                    'name': self.tr('Screen'),
                    'trigger': 'Screen',
                    'actions': [
                        {
                            'name': self.tr('MFD3'),

                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'MFD3',
                            "checkable": True
                        },
                        {
                            'name': self.tr('MFD4'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'MFD4',
                            "checkable": True
                        },
                    ]
                },
                {
                    'name': self.tr('Device'),
                    'trigger': 'Device',
                    'actions': [
                        # {
                        #     'name': self.tr('Enable Bluetooth'),
                        #     'icon': u'',
                        #     'shortcut': u'',
                        #     'trigger': 'EnableBluetooth',
                        # },
                        {
                            'name': self.tr('Search Devices'),

                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'SearchDevices',
                        },
                    ]
                },
                {
                    'name': self.tr('View'),
                    'trigger': 'View',
                    'actions': [
                    ]
                },
                {
                    'name': self.tr('Report'),
                    'trigger': 'Test Rig',
                    'actions': [
                        {
                            'name': self.tr('Report'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'TestRigAll',
                        },
                        {
                            'name': self.tr('Start'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'TestRig',
                        }
                    ]
                },
                {
                    'name': self.tr(' Help '),
                    'trigger': 'Help',
                    'actions': [
                        {
                            'name': self.tr('About ALE'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'About',
                        },
                        {
                            'name': self.tr('Feedback to us'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'Feedbackus',
                        },
                    ]
                }
            ]
        }

        self.creatMenus(self.menusettings)

    def creatMenus(self, menusettings):
        self.setVisible(menusettings['visual'])
        for menu in menusettings['menus']:
            setattr(
                self,
                '%smenu' % menu['trigger'],
                self.addMenu(u'%s' % menu['name'])
            )
            submenu = getattr(self, '%smenu' % menu['trigger'])
            for menuaction in menu['actions']:
                if 'type' in menuaction and menuaction['type'] == "submenu":
                    self.createSubAction(menu['trigger'], menuaction)
                else:
                    self.creatAction(submenu, menuaction)

    def createSubAction(self, pmenu_name, menu):
        childmenu = getattr(self, '%smenu' % pmenu_name)
        submenu = childmenu.addMenu(u'%s' % menu['name'])
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
        # action.triggered.connect(
        #         getattr(self.parent, 'action%s' % menuaction['trigger'])
        #     )
