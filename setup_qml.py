# -*- coding: utf-8 -*-
import sys
import os
import shutil
import zipfile
from cx_Freeze import setup, Executable
import PyQt5
from setup import *

if __name__ == '__main__':

    
    if sys.platform == 'win32':
        base = 'Win32GUI'
    else:
        base = None

    buildOptions = dict(
        packages=[],
        excludes=[],
        includes=['PyQt5.QtNetwork','PyQt5.QtQml', 'PyQt5.QtWebKit','PyQt5.QtWebKit', "PyQt5.QtPrintSupport"],
        icon="gui\skin\images\QFramer.ico",
    )

    executables = [
        Executable(
            'qmlmain.py',
            base=base,
            icon="gui\skin\images\QFramer.ico",
            targetName="QFramer.exe",
            appendScriptToExe=False,
            appendScriptToLibrary=True,
        )
    ]

    for key in ['build', 'dist']:
        path = os.sep.join([os.getcwd(), key])
        delete_file_folder(path)

    path_pyqt5 = PyQt5.__path__[0]
    build_path = os.sep.join([os.getcwd(), 'build', 'exe.win32-3.3'])

    sys.argv.append("build")
    setup(
        name='QFramer',
        version='1.0',
        description='Base on PyQt5',
        options=dict(build_exe=buildOptions),
        executables=executables
    )

    for item in ['application']:
        shutil.copytree(os.sep.join([os.getcwd(), item]), os.sep.join([build_path, item]))

    for item in ['qml']:
        shutil.copytree(os.sep.join([path_pyqt5, item]), os.sep.join([build_path, item]))

    # for item in ['qml']:
    #     copytree(os.sep.join([path_pyqt5, item]), os.sep.join([build_path]))

    for item in ['msvcp100.dll']:
        shutil.copyfile(os.sep.join([os.getcwd(), 'dll', item]), os.sep.join([build_path, item]))

    for item in ['libEGL.dll','Qt5QuickParticles.dll']:
        shutil.copyfile(os.sep.join([path_pyqt5, item]), os.sep.join([build_path, item]))

    for item in [
        'Qt5Multimedia.dll','Qt5MultimediaQuick_p.dll', 'Qt5MultimediaWidgets.dll',
        'Qt5OpenGL.dll', 'Qt5Sensors.dll', 'Qt5WebKitWidgets.dll', 'QtWebProcess.exe']:
        shutil.copyfile(os.sep.join([path_pyqt5, item]), os.sep.join([build_path, item]))
