# -*- coding: utf-8 -*-
# 利用os模块编写一个能实现dir -l输出的程序。

import os
from datetime import datetime


for f in os.listdir('.'):
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y/%m/%d %H:%M')
    fsize = os.path.getsize(f) if os.path.isfile(f) else ''
    isDir = '<DIR>' if os.path.isdir(f) else ''
    print(mtime, '\t', isDir, '\t', fsize, '\t', f)


# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
print('\n')


def findFile(str, path='.'):
    for f in os.listdir(path):
        fpath = os.path.join(path, f)  # 获取文件的路径
        if os.path.isfile(fpath) and str in f:
            print(fpath)
        if os.path.isdir(fpath):
            findFile(str, fpath)  # 使用递归调用来查找子目录


findFile('class')
