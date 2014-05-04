#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import time

class SplashScreen(QtWidgets.QSplashScreen):

    def __init__(self, splash_image):
        super(SplashScreen, self).__init__(splash_image)    # 启动程序的图片
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def fadeTicker(self, keep_t):
        self.setWindowOpacity(0)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() + 0.02   # 设置淡入
            if newOpacity > 1:
                break
            self.setWindowOpacity(newOpacity)
            self.show()
            t -= 1
            time.sleep(0.04)
        self.show()
        time.sleep(keep_t)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() - 0.02   # 设置淡出
            if newOpacity < 0:
                self.close()
                break
            self.setWindowOpacity(newOpacity)
            self.show()
            t += 1
            time.sleep(0.04)
