#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

if __name__ == '__main__':
    from basedialog import BaseDialog
else:
    from .basedialog import BaseDialog


class MessageDialog(BaseDialog):
    def __init__(self, text, styleoptions, parent=None):
        super(MessageDialog, self).__init__(styleoptions, parent)
        # message内容提示
        self.msglabel = QtWidgets.QLabel(text)
        self.msglabel.setAlignment(QtCore.Qt.AlignCenter)
        #确认按钮布局
        self.enterwidget = QtWidgets.QWidget()
        self.pbEnter = QtWidgets.QPushButton(u'确定', self)
        self.pbEnter.clicked.connect(self.enter)
        self.enter_mainlayout = QtWidgets.QGridLayout()
        self.enter_mainlayout.addWidget(self.pbEnter, 0, 0)
        self.enterwidget.setLayout(self.enter_mainlayout)

        self.layout().addWidget(self.msglabel)
        self.layout().addWidget(self.enterwidget)
        self.resize(self.width(), self.height())

    def enter(self):
        self.accept()  # 关闭对话框并返回1


def msg(text, styleoptions):
    """返回True或False"""
    dialog = MessageDialog(text, styleoptions)
    if dialog.exec_():
        return True
    else:
        return False


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    styleoptions = {
        'title': u'消息提示',
        'windowicon': "../skin/images/ov-orange-green.png",
        'minsize': (400, 300),
        'size': (400, 300),
        'logo_title': u'智能光纤云终端管理平台',
        'logo_img_url': "../skin/images/ov-orange-green.png"
    }
    print(msg('sddsdsdsdssddsds', styleoptions))
    sys.exit(app.exec_())
