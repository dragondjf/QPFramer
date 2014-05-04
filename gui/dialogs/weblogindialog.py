#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import requests
from dataBase import signal_DB
import threading
from Crypto.Hash import MD5
if __name__ == '__main__':
    from basedialog import BaseDialog
else:
    from .basedialog import BaseDialog


class AuthLoginDialog(BaseDialog):

    def __init__(self, styleoptions, parent=None):
        super(AuthLoginDialog, self).__init__(styleoptions, parent)

        self.login_nameLabel = QtWidgets.QLabel(u'用户名')
        self.login_name = QtWidgets.QLineEdit(self)
        self.login_name.setPlaceholderText(u'用户名')

        self.login_passwordLabel = QtWidgets.QLabel(u'密码')
        self.login_password = QtWidgets.QLineEdit(self)
        self.login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password.setPlaceholderText(u'密码')

        self.ipLabel = QtWidgets.QLabel(u'输入主机ip:')
        self.ipLineEdit = QtWidgets.QLineEdit(u'127.0.0.1')
        self.ipLineEdit.setInputMask('000.000.000.000')
        self.portLabel = QtWidgets.QLabel(u'输入主机port:')
        self.portLineEdit = QtWidgets.QLineEdit(u'8888')

        self.pbLogin = QtWidgets.QPushButton(u'登录', self)

        self.pbLogin.setCheckable(True)
        self.pbCancel = QtWidgets.QPushButton(u'取消', self)
        enterwidget_mainlayout = QtWidgets.QGridLayout()
        enterwidget_mainlayout.addWidget(self.pbLogin, 0, 0)
        enterwidget_mainlayout.addWidget(self.pbCancel, 0, 1)

        self.statusLabel = QtWidgets.QLabel("")
        self.statusLabel.setFixedHeight(30)

        mainlayout = QtWidgets.QGridLayout()
        mainlayout.addWidget(self.login_nameLabel, 0, 0)
        mainlayout.addWidget(self.login_name, 0, 1)
        mainlayout.addWidget(self.login_passwordLabel, 1, 0)
        mainlayout.addWidget(self.login_password, 1, 1)
        mainlayout.addWidget(self.ipLabel, 2, 0)
        mainlayout.addWidget(self.ipLineEdit, 2, 1)
        mainlayout.addWidget(self.portLabel, 3, 0)
        mainlayout.addWidget(self.portLineEdit, 3, 1)
        mainlayout.addWidget(self.statusLabel, 4, 1, 1, 2)
        mainlayout.addLayout(enterwidget_mainlayout, 5, 0, 1, 2)

        self.pbLogin.clicked.connect(self.clickEnter)
        self.pbCancel.clicked.connect(self.reject)
        self.pbLogin.setFixedHeight(30)
        self.pbCancel.setFixedHeight(30)

        self.layout().addLayout(mainlayout)
        self.resize(self.width(), self.height())
        self.layout().setContentsMargins(10, 10, 10, 20)

        signal_DB.login_sin.connect(self.authLogin)

    def clickEnter(self):
        name = self.login_name.text()
        password = self.login_password.text()
        ip = self.ipLineEdit.text()
        port = self.portLineEdit.text()
        self.statusLabel.setText("正在登录中...")
        self.pas = None
        self.address = (ip, port)
        self.loginThread = AuthLoginThread(name, password, self.address)
        self.loginThread.start()
        self.pbLogin.setChecked(True)

    def cancleConenct(self):
        self.pbLogin.setChecked(False)
        self.loginThread.flag = False

    @QtCore.pyqtSlot(dict)
    def authLogin(self, info):
        if info['status']:
            self.pas = info['result']
            self.accept()
        else:
            self.pbLogin.setChecked(False)
            self.statusLabel.setText(info['result'])


class AuthLoginThread(threading.Thread, QtCore.QObject):
    """docstring for AuthLoginThread"""
    def __init__(self, user, password, address):
        super(AuthLoginThread, self).__init__()
        self.user = user
        self.password = password
        self.address = address

    def run(self):
        status = None
        result = None
        try:
            userinfo = {"account": self.user, "password": MD5.new(('%s' % self.password).encode('utf-8')).hexdigest()}                
            result = requests.post('http://%s:%s/login' % self.address, data=userinfo)
            loginflag = int(result.json())
            if loginflag == 1:
                signal_DB.login_sin.emit({'status': True, 'result': "登陆成功"})
            elif loginflag == 2:
                signal_DB.login_sin.emit({'status': False, 'result': "请输入正确的用户名"})
            elif loginflag == 3:
                signal_DB.login_sin.emit({'status': False, 'result': "请输入正确的密码"})
        except requests.ConnectionError as e:
            signal_DB.login_sin.emit({'status': False, 'result':"请输入正确的ip地址或端口号"})
        except Exception as e:
            print(e)
            signal_DB.login_sin.emit({'status': False, 'result':"请输入正确的参数"})


def weblogin(loginoptions):
    """返回True或False"""
    dialog = AuthLoginDialog(loginoptions)
    if dialog.exec_():
        return True, dialog.address
    else:
        return False, (u'', u'')


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    styleoptions = {
        'title': u'登录',
        'windowicon': "../skin/images/ov-orange-green.png",
        'minsize': (400, 300),
        'size': (400, 300),
        'logo_title': u'智能光纤云终端管理平台',
        'logo_img_url': "../skin/images/ov-orange-green.png",
    }
    print(login(styleoptions))
    sys.exit(app.exec_())
