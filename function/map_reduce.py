# -*- coding: utf-8 -*-
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce


def str2float(s):
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    x1 = s.split('.')[0]  #整数部分
    x2 = s.split('.')[1]  #小数部分
    a1 = reduce(lambda x,y:10*x+y, map(char2num, x1))  #将整数部分转换为int
    a2 = reduce(lambda x,y:0.1*x+y, map(char2num, x2[::-1]))  #将小数部分进行倒序后再转换为int
    # x2[::-1] 相当于起点为最后一个,终点为第一个,然后一次减少一个
    '''上一行代码执行过程如下：
    step 1: fn(x,y) ==> fn(6,5) ==> 0.1*6+5 ==> 0.6+5 ==> 5.6
    step 2: fn(x,y) ==> fn(5.6,4) ==> 0.1*5.6+4 ==> 0.56+4 ==> 4.56
    '''
    return a1 + 0.1 * a2


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
