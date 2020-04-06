# -*- coding: utf-8 -*-
# 使用迭代查找一个list中最小和最大值，并返回一个tuple


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    minValue = L[0]  # 定义最小值变量，默认值为list的第一个元素
    maxValue = L[0]  # 定义最大值变量，默认值为list的第一个元素
    for value in L:
        if value > maxValue:
            maxValue = value
        if value < minValue:
            minValue = value
    print((minValue, maxValue))
    return (minValue, maxValue)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
