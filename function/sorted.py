# -*- coding: utf-8 -*-
# 请用sorted()对下面的列表分别按名字排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


L2 = sorted(L, key=by_name)
print(L2)

# 再按成绩从高到低排序


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)

# 不用构建函数可以这么写
L2 = sorted(L, key=lambda L: L[0].lower())
print(L2)
L2 = sorted(L, key=lambda L: L[1], reverse=True)
print(L2)
