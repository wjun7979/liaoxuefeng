# -*- coding: utf-8 -*-
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，
# 请编写一个函数将其转换为timestamp：

from datetime import datetime, timedelta, timezone
import re


def to_timestamp(dt_str, tz_str):
    # 获取用户输入的时区
    tz = re.match('(?i)^UTC([+-]\d+)\:00', tz_str)
    tz_utc = int(tz.group(1))
    # 将字符串转换为datetime对象
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 强制设置时区
    tz_info = timezone(timedelta(hours=tz_utc))
    utc_dt = dt.replace(tzinfo=tz_info)

    return utc_dt.timestamp()  # 将datetime转换为timestamp


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'utc-09:00')
assert t2 == 1433121030.0, t2

print('ok')
