#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'类和实例'


class Student(object):
    # 实例会自动调用这个方法，一般用来对实例的属性进行初使化
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa Simpson', 99)
lisa.print_score()
print(lisa.name, lisa.get_grade())

bart = Student('Bart Simpson', 59)
bart.print_score()
print(bart.name, bart.get_grade())
