# -*- coding: utf-8 -*-
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：

from functools import reduce


def str2num(s):
    # return int(s)  # 这行是错误的源头，int的参数不能是小数字符串
    try:
        return int(s)
    except Exception as e:
        return float(s)


def calc(exp):
    ss = exp.split('+')  # 将算式按"+"拆分成一个list
    ns = map(str2num, ss)  # 将上面list中的字符串全部转换为整型，返回Iterator(迭代器)
    return reduce(lambda x, y: x + y, ns)  # 将上面的Iterator进行累加运算


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
