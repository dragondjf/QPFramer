#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QUrl, QObject, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
class MyClass(QObject):
    @pyqtSlot(int, result=str)    # 声明为槽，输入参数为int类型，返回值为str类型
    def returnValue(self, value):
        """
        功能: 创建一个槽
        参数: 整数value
        返回值: 字符串
        """
        return str(value+10)
if __name__ == '__main__':
    path = 'demo.qml'   # 加载的QML文件
    app = QGuiApplication([])
    view = QQuickView()
    con = MyClass()
    context = view.rootContext()
    context.setContextProperty("con", con)
    view.engine().quit.connect(app.quit)
    view.setSource(QUrl(path))
    view.show()
    app.exec_()