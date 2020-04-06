#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Michael Liao'

import sys


def test():
    args = sys.argv  # 用list存储了命令行的所有参数
    if len(args) == 1:  # 运行 python module.py 时
        print('Hello, World!')
    elif len(args) == 2:  # 运行 python module.py wJun 时
        print('Hello, %s' % args[1])
    else:  # 运行 python module.py wJun Feng2 时
        print('Too Many arguments!')


# 命令行直接运行时会触发，但做为模块被导入时不会
if __name__ == '__main__':
    test()
