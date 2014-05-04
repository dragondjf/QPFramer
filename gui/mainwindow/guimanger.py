#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from gui.functionpages.colorpopupframe import ColorPopupFrame
from .guiconfig import views


class GuiManger(QtCore.QObject):

    """docstring for GuiManger"""

    def __init__(self, parent=None):
        super(GuiManger, self).__init__()
        self.parent = parent
        self.initConnect()

    def initConnect(self):
        views['NavgationBar'].exitButton.clicked.connect(views['MainWindow'].close)
        views['TitleBar'].skinButton.clicked.connect(self.changeBgColor)

    def changeBgColor(self):
        colorpopupframe = ColorPopupFrame(views['MainWindow'])
        colorpopupframe.show()
