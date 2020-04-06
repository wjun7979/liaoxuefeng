# -*- coding: utf-8 -*-
# 对函数fact(n)编写doctest并执行：

from functools import reduce


def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError

    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    # return n * fact(n - 1)  # 可以把这行的函数递归调用改成下一行的reduce高阶函数
    return reduce(lambda x, y: x * y, range(1, n + 1))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
