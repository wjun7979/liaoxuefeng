# -*- coding:utf-8 -*-
# 高阶函数：让函数的参数能够接收别的函数


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))
