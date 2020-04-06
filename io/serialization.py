# -*- coding: utf-8 -*-
# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响

import json

obj = dict(name='小明', age=20)
# 如果 ensure_ascii 是 true （即默认值），输出保证将所有输入的非 ASCII 字符转义。
# 如果 ensure_ascii 是 false，这些字符会原样输出。
s = json.dumps(obj, ensure_ascii=True)
print(s)
