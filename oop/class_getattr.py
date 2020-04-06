# -*- coding: utf-8 -*-
# 学习class中 __getattr__ 方法的使用


class Chain(object):
    def __init__(self, path=''):
        # print(path)
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    __repr__ = __str__


c = Chain().status.user.timeline.list
print(c)


class Github(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Github('%s/%s' % (self._path, path))

    def __call__(self, path):
        return Github('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    __repr = __str__

'''
以下是链式调用，我们把它分解成能看懂的：
第一步：Chain()  #初始化一个实例
第二步：Chain().users  #查找一个实例的一个属性
第三步：Chain('/users')('michael')  #像调用函数一样调用实例
第四步：Chain('/users/michael').repos  #还是实例的属性
'''
g = Github().users('michael').repos
print(g)
