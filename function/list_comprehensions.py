# -*- coding: utf-8 -*-
# 练习列表生成式
# 将list中所有的字符串变成小写，注意list中的非字符串类型的元素

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
