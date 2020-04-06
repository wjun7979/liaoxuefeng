# -*- coding: utf-8 -*-
# 继承和多态


class Animal(object):
    # Animal类是父类或者叫基类
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    # Dog类继承Animal父类
    def run(self):  # Dog类的run()方法覆盖了父类的run()方法
        print('Dog is running...')


class Cat(Animal):
    # Cat类也是继承Animal父类
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    # Tortoise类也是继承Animal父类
    def run(self):
        print('Tortoise is running slowly...')


class Timer(object):
    # Timer类虽然不是继承自Animal类，但它有run()方法，所以它是“鸭子类型”
    def run(self):
        print('start...')


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())
run_twice(Timer())  # 鸭子类型的类也可以作为参数传入
