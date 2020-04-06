# -*- coding: utf-8 -*-
# 学习使用metaclass（元类）编写ORM框架


class Field(object):
    # 字段类，负责保存数据库表的字段名和字段类型
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    # 字符型字段
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')  # 调用父类的方法


class IntegerField(Field):
    # 整数型字段
    def __init__(self, name):
        super().__init__(name, 'bigint')


class ModelMetaclass(type):
    # 元类
    def __new__(cls, name, bases, attrs):
        if name == 'Model':  # 排除掉对Model类的修改
            return type.__new__(cls, name, bases, attrs)
        print('Found model:%s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)  # 从类属性中删除Field属性
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    # 基类
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)  # r表示字符串不转义

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []  # 字段列表
        params = []  # SQL预编译列表
        args = []  # 字段值列表
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL:%s' % sql)
        print('ARGS:%s' % str(args))


class User(Model):
    # 操作数据库表的User类
    id = IntegerField('id')  # 定义类的属性到字段的映射
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
