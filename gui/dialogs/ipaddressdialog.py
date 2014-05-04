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


class IPaddressDialog(BaseDialog):
    def __init__(self, styleoptions, parent=None):
        super(IPaddressDialog, self).__init__(styleoptions, parent)

        # url内容输入
        self.urlwidget = QtWidgets.QWidget()
        ip_mainlayout = QtWidgets.QGridLayout()
        self.ipLabel = QtWidgets.QLabel(u'输入主机ip:')
        self.ipLineEdit = QtWidgets.QLineEdit(u'192.168.100.100')
        self.ipLineEdit.setInputMask('000.000.000.000')
        self.portLabel = QtWidgets.QLabel(u'输入主机port:')
        self.portLineEdit = QtWidgets.QLineEdit(u'8000')
        ip_mainlayout.addWidget(self.ipLabel, 0, 0)
        ip_mainlayout.addWidget(self.ipLineEdit, 0, 1)
        ip_mainlayout.addWidget(self.portLabel, 1, 0)
        ip_mainlayout.addWidget(self.portLineEdit, 1, 1)

        self.urlwidget.setLayout(ip_mainlayout)

        #确认按钮布局
        self.enterwidget = QtWidgets.QWidget()
        self.pbEnter = QtWidgets.QPushButton(u'确定', self)
        self.pbCancel = QtWidgets.QPushButton(u'取消', self)
        self.pbEnter.clicked.connect(self.enter)
        self.pbCancel.clicked.connect(self.reject)
        enterwidget_mainlayout = QtWidgets.QGridLayout()
        enterwidget_mainlayout.addWidget(self.pbEnter, 0, 0)
        enterwidget_mainlayout.addWidget(self.pbCancel, 0, 1)
        self.enterwidget.setLayout(enterwidget_mainlayout)

        self.layout().addWidget(self.urlwidget)
        self.layout().addWidget(self.enterwidget)
        self.resize(self.width(), self.height())

    def enter(self):
        self.accept()  # 关闭对话框并返回1


def ipaddressinput(options):
    dialog = IPaddressDialog(options)
    if dialog.exec_():
        return True, (dialog.ipLineEdit.text(), int(dialog.portLineEdit.text()))
    else:
        return False, (dialog.ipLineEdit.text(), int(dialog.portLineEdit.text()))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    styleoptions = {
        'title': u'请输入相应的ip地址和端口号：',
        'windowicon': "../skin/images/ov-orange-green.png",
        'minsize': (400, 300),
        'size': (400, 300),
        'logo_title': u'智能光纤云终端管理平台',
        'logo_img_url': "../skin/images/ov-orange-green.png"
    }
    print(ipaddressinput(styleoptions))
    sys.exit(app.exec_())
