#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtGui
from . import logo_ico, logo_title, logo_img_url


width = 410
height = 340

dialogsettings = {
    'login_window': {
        'title': u'登陆',
        'windowicon': logo_ico,
        'minsize': (width, height),
        'size': (width, height),
        'logo_title': logo_title,
        'logo_img_url': logo_img_url
    },
    'weblogin_window': {
        'title': u'登陆',
        'windowicon': logo_ico,
        'minsize': (width, height),
        'size': (width, height),
        'logo_title': logo_title,
        'logo_img_url': logo_img_url
    },
    'exitdialog': {
        'title': u'退出',
        'windowicon': logo_ico,
        'minsize': (width, height),
        'size': (width, height),
        'logo_title': logo_title,
        'logo_img_url': logo_img_url
    },
    'msgdialog': {
        'title': u'消息提示',
        'windowicon': logo_ico,
        'minsize': (width, height),
        'size': (width, height),
        'logo_title': logo_title,
        'logo_img_url': logo_img_url
    },
    'confirmdialog': {
        'title': u'消息提示',
        'windowicon': logo_ico,
        'minsize': (width, height),
        'size': (width, height),
        'logo_title': logo_title,
        'logo_img_url': logo_img_url
    },
    'urldialog': {
        'title': u'输入访问的url',
        'windowicon': logo_ico,
        'minsize': (width, height),
        'size': (width, height),
        'logo_title': logo_title,
        'logo_img_url': logo_img_url
    },
    'ipaddressdialog': {
        'title': u'输入访问的url',
        'windowicon': logo_ico,
        'minsize': (width, height),
        'size': (width, height),
        'logo_title': logo_title,
        'logo_img_url': logo_img_url
    },
    'numinputdialog': {
        'title': u'输入整数',
        'windowicon': logo_ico,
        'minsize': (width, height),
        'size': (width, height),
        'logo_title': logo_title,
        'logo_img_url': logo_img_url
    },
    'settingsdialog': {
        'title': u'输入设置参数',
        'windowicon': logo_ico,
        'minsize': (width, height),
        'size': (width, height),
        'logo_title': logo_title,
        'logo_img_url': logo_img_url
    }
}
