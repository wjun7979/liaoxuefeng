# -*- coding: utf-8 -*-
# --------------------------------------------------
# 从自然数中筛选出所有的质数
# --------------------------------------------------


def _odd_iter():  # 构造一个从3开始的奇数序列
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):  # 筛选函数
    return lambda x: x % n > 0  # 如果筛选逻辑需要额外的参数，则使用lambda表达式返回匿名函数


def primes():
    yield 2  # 先返回第一个素数2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n  # 返回序列的第一个数
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印100以内的素数
for n in primes():
    if n < 100:
        print(n)
    else:
        break

# ----------------------------------------------------------------------------------
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
# ----------------------------------------------------------------------------------
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')