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


class numinputDialog(BaseDialog):
    def __init__(self, styleoptions, parent=None):
        super(numinputDialog, self).__init__(styleoptions, parent)

        # url内容输入
        self.numwidget = QtWidgets.QWidget()
        num_mainlayout = QtWidgets.QGridLayout()
        self.numLabel = QtWidgets.QLabel(u'Q的防区个数:')
        self.numspinbox = QtWidgets.QSpinBox(self.numwidget)

        self.ipLabel = QtWidgets.QLabel(u'Q的下位机IP:')
        self.ipIn = QtWidgets.QLineEdit()

        num_mainlayout.addWidget(self.numLabel, 0, 0)
        num_mainlayout.addWidget(self.numspinbox, 0, 1)
        #num_mainlayout.addWidget(self.ipLabel, 1, 0)
        #num_mainlayout.addWidget(self.ipIn, 1, 1)
        self.numwidget.setLayout(num_mainlayout)

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

        self.layout().addWidget(self.numwidget)
        self.layout().addWidget(self.enterwidget)
        self.resize(self.width(), self.height())

    def enter(self):
        self.accept()  # 关闭对话框并返回1


def numinput(value, start, end, step, options):
    dialog = numinputDialog(options)
    dialog.numspinbox.setValue(value)
    dialog.numspinbox.setRange(start, end)
    dialog.numspinbox.setSingleStep(step)
    dialog.numspinbox.setFocusPolicy(QtCore.Qt.NoFocus)
    if dialog.exec_():
        return True, int(dialog.numspinbox.value())#, str(dialog.ipIn.text())
    else:
        return False, int(dialog.numspinbox.value())#, str(dialog.ipIn.text())


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    styleoptions = {
        'title': u'退出设置',
        'windowicon': "../skin/images/ov-orange-green.png",
        'minsize': (400, 300),
        'size': (400, 300),
        'logo_title': u'智能光纤云终端管理平台',
        'logo_img_url': "../skin/images/ov-orange-green.png"
    }
    print(numinput(6, 2, 8, 2, styleoptions))
    sys.exit(app.exec_())
