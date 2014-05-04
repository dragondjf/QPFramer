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


class SettingsDialog(BaseDialog):
    def __init__(self, pa, styleoptions, parent=None):
        super(SettingsDialog, self).__init__(styleoptions, parent)
        self.data = {}

        formLayout = QtWidgets.QFormLayout()
        formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        formLayout.setLabelAlignment(QtCore.Qt.AlignRight)
        formLayout.setHorizontalSpacing(40)

        nameLabel = QtWidgets.QLabel("防区名字:")
        paNameLabel = QtWidgets.QLabel(pa['name'])

        didLabel = QtWidgets.QLabel("采集器:")
        paDidLabel = QtWidgets.QLabel(str(pa['did']))

        pidLabel = QtWidgets.QLabel("防区:")
        paPidLabel = QtWidgets.QLabel(str(pa['pid']))

        self.startLabel = QtWidgets.QLabel("启用:")
        self.startLabel.setFixedWidth(100)
        self.startLabel.setAlignment(QtCore.Qt.AlignRight)
        self.startCheckBox = QtWidgets.QCheckBox()
        self.startCheckBox.setChecked(pa['status'])

        print("pa status:", pa['status'])

        formLayout.addRow(nameLabel, paNameLabel)
        formLayout.addRow(didLabel, paDidLabel)
        formLayout.addRow(pidLabel, paPidLabel)
        formLayout.addRow(self.startLabel, self.startCheckBox)

        #确认按钮布局
        self.pbEnter = QtWidgets.QPushButton(u'确定', self)
        self.pbEnter.setFixedHeight(30)
        self.pbCancel = QtWidgets.QPushButton(u'取消', self)
        self.pbCancel.setFixedHeight(30)
        self.pbEnter.clicked.connect(self.enter)
        self.pbCancel.clicked.connect(self.reject)
        enterwidget_mainlayout = QtWidgets.QGridLayout()
        enterwidget_mainlayout.addWidget(self.pbEnter, 0, 0)
        enterwidget_mainlayout.addWidget(self.pbCancel, 0, 1)

        self.layout().addStretch()
        self.layout().addLayout(formLayout)
        self.layout().addStretch()
        self.layout().addLayout(enterwidget_mainlayout)
        self.layout().addSpacing(10)

    def enter(self):
        self.data = {
            "enable": self.startCheckBox.isChecked()
        }
        self.accept()  # 关闭对话框并返回1


def settingsinput(pa, options):
    dialog = SettingsDialog(pa, options)
    if dialog.exec_():
        return True, dialog.data
    else:
        return False, dialog.data


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
    print(settingsinput(styleoptions))
    sys.exit(app.exec_())
