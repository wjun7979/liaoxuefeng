# -*- coding: utf-8 -*-
# 匿名函数


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)

# 用匿名函数对上面的代码进行改造
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
