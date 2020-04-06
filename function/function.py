# -*- coding: utf-8 -*-
# 解一元二次方程

import math


def quadratic(a, b, c):
    if not isinstance(a+b+c, (int, float)):  #检查数据类型
        raise TypeError('参数类型错误')
    if b**2 - 4*a*c < 0:
        raise ValueError('该方程无解')
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    print('该一元二次方程的解是：', x1, x2)
    return x1, x2


v = input('请输入a,b,c：').split(',')
quadratic(float(v[0]), float(v[1]), float(v[2]))
