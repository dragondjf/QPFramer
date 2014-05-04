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


class ExitDialog(BaseDialog):
    def __init__(self, styleoptions, parent=None):
        super(ExitDialog, self).__init__(styleoptions, parent)

        # 退出设置
        self.exitoptwidget = QtWidgets.QWidget()
        exit_mainlayout = QtWidgets.QGridLayout()

        self.exitradiogroup = QtWidgets.QButtonGroup(self.exitoptwidget)
        self.minRadio = QtWidgets.QRadioButton(u'最小化')
        self.exitRadio = QtWidgets.QRadioButton(u'退出')
        self.exitsaveRadio = QtWidgets.QRadioButton(u'退出并保存配置')
        self.exitradiogroup.addButton(self.minRadio)
        self.exitradiogroup.addButton(self.exitRadio)
        self.exitradiogroup.addButton(self.exitsaveRadio)

        exit_mainlayout.addWidget(self.minRadio, 0, 0)
        exit_mainlayout.addWidget(self.exitRadio, 1, 0)
        exit_mainlayout.addWidget(self.exitsaveRadio, 2, 0)
        self.exitoptwidget.setLayout(exit_mainlayout)
        self.exitsaveRadio.setChecked(True)

        #确认按钮布局
        self.enterwidget = QtWidgets.QWidget()
        self.pbEnter = QtWidgets.QPushButton(u'确定', self)
        self.pbCancel = QtWidgets.QPushButton(u'取消', self)
        self.pbEnter.setFixedHeight(30)
        self.pbCancel.setFixedHeight(30)

        self.pbEnter.clicked.connect(self.exit)
        self.pbCancel.clicked.connect(self.close)

        enterwidget_mainlayout = QtWidgets.QGridLayout()
        enterwidget_mainlayout.addWidget(self.pbEnter, 0, 0)
        enterwidget_mainlayout.addWidget(self.pbCancel, 0, 1)
        self.enterwidget.setLayout(enterwidget_mainlayout)

        self.layout().addStretch()
        self.layout().addWidget(self.exitoptwidget)
        self.layout().addStretch()
        self.layout().addWidget(self.enterwidget)
        self.resize(self.width(), self.height())

        self.exitflag = {}

    def exit(self):
        for radio in ['minRadio', 'exitRadio', 'exitsaveRadio']:
            if getattr(self, radio) is self.exitradiogroup.checkedButton():
                self.exitflag.update({radio: True})
            else:
                self.exitflag.update({radio: False})
        self.accept()


def exit(options):
    """返回True或False"""
    dialog = ExitDialog(options)
    if dialog.exec_():
        return True, dialog.exitflag
    else:
        return False, dialog.exitflag

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
    print(exit(styleoptions))
    sys.exit(app.exec_())
