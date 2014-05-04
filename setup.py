# -*- coding: utf-8 -*-
import sys
import os
import shutil
import zipfile
from cx_Freeze import setup, Executable
import PyQt5

# Dependencies are automatically detected, but it might need
# fine tuning.


def change_package_fromLib(package_name):
    '''
        根据包名从python Lib中获取到包，替换library.zip中名字相同的包
    '''
    library_zippath = os.getcwd() + os.sep + os.sep.join(['dist', 'library.zip'])
    library_path = os.getcwd() + os.sep + os.sep.join(['dist', 'library'])
    with zipfile.ZipFile(library_zippath, 'r') as zip_file:
        zip_file.extractall(path=library_path)
    shutil.rmtree(library_path + os.sep + package_name)
    for item in [package_name]:
        package = __import__(item)
        package_path = os.path.dirname(package.__file__)
        shutil.copytree(package_path, library_path + os.sep + package_name)

    os.remove(os.getcwd() + os.sep + os.sep.join(['dist', 'library.zip']))
    addFolderToZip(library_path, 'dist\library.zip')
    shutil.rmtree(library_path)


def change_package_fromLocal(package_name):
    '''
        根据包名从当前项目中获取到包，替换library.zip中名字相同的包
    '''
    library_zippath = os.getcwd() + os.sep + os.sep.join(['dist', 'library.zip'])
    library_path = os.getcwd() + os.sep + os.sep.join(['dist', 'library'])
    with zipfile.ZipFile(library_zippath, 'r') as zip_file:
        zip_file.extractall(path=library_path)
    shutil.rmtree(library_path + os.sep + package_name)
    for item in [package_name]:
        package_path = os.getcwd() + os.sep + item
        shutil.copytree(package_path, library_path + os.sep + package_name)

    os.remove(os.getcwd() + os.sep + os.sep.join(['dist', 'library.zip']))
    addFolderToZip(library_path, 'dist\library.zip')
    shutil.rmtree(library_path)


def addFolderToZip(folder, zip_filename):
    '''
        将文件夹foldler添加到名字为zip_filename的zip中去
    '''
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        def addhandle(folder, zip_file):
            for f in os.listdir(folder):
                full_path = os.path.join(folder, f)
                if os.path.isfile(full_path):
                    print('Add file: %s' % full_path)
                    zip_file.write(full_path, full_path.split('library\\')[1])
                elif os.path.isdir(full_path):
                    print('add folder: %s' % full_path)
                    addhandle(full_path, zip_file)
        addhandle(folder, zip_file)


def delete_file_folder(src):
    '''delete files and folders'''
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc = os.path.join(src, item)
            delete_file_folder(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass


# def get_py2exe_datafiles(datapath, relativehead):
#     head, tail = os.path.split(datapath)
#     d = {}
#     for root, dirs, files in os.walk(datapath):
#         files = [os.path.join(root, filename) for filename in files]
#         root = root.replace(tail, relativehead)
#         root = root[root.index(relativehead):]
#         d[root] = files
#     return d.items()


def write_file(filename, content):
    '''
        将相应的content写入filename中去
    '''
    fd = open(filename, "w")
    fd.write(content)
    fd.close()


buildOptions = dict(
    packages=[],
    excludes=[],
    # includes=['PyQt5.QtWebKit', "PyQt5.QtPrintSupport"],
    icon="gui\skin\images\QFramer.ico",
)


if sys.platform == 'win32':
    base = 'Win32GUI'
else:
    base = None

executables = [
    Executable(
        'main.py',
        base=base,
        icon="gui\skin\images\QFramer.ico",
        targetName="QFramer.exe",
        appendScriptToExe=False,
        appendScriptToLibrary=True,
    )
]


if __name__ == '__main__':

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

    for item in ['skin']:
        shutil.copytree(os.sep.join([os.getcwd(), 'gui', item]), os.sep.join([build_path, 'gui', item]))

    for item in ['options']:
        os.mkdir(os.sep.join([build_path, item]))

    for item in ['msvcp100.dll']:
        shutil.copyfile(os.sep.join([os.getcwd(), 'dll', item]), os.sep.join([build_path, item]))

    for item in ['libEGL.dll']:
        shutil.copyfile(os.sep.join([path_pyqt5, item]), os.sep.join([build_path, item]))
