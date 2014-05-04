#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def set_skin(widget, qssfile):
    if os.path.exists(qssfile):
        fd = open(qssfile, "r")
        style = fd.read()
        fd.close()
        widget.setStyleSheet(style)


def changebg(widget, style=""):
    widget.setStyleSheet(widget.styleSheet() + style)
