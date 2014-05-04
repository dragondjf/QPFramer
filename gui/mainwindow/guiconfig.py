#!/usr/bin/python
# -*- coding: utf-8 -*-

import functools

views = {}


def collectView(fuc):

    @functools.wraps(fuc)
    def wrapper(*args, **kwargs):
        self = args[0]
        if hasattr(self, 'viewID'):
            views.update({self.viewID: self})
        fuc(*args, **kwargs)
    return wrapper
