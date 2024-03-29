# -*- coding: utf-8 -*-
# 请编写函数，在Sqlite中根据分数段查找指定的名字

import os
import sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')  # 数据库文件
if os.path.isfile(db_file):
    os.remove(db_file)  # 如果数据库文件已存在，先删除之

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(r"select name from user where score between ? and ? order by score", (low, high))
        values = cursor.fetchall()
        return list(map(lambda x: x[0], values))
    finally:
        cursor.close()
        conn.close()

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
