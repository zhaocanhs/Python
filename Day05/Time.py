# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/19- 21:05
# 当前用户名： zc
# 文件名：Time

import time

# 本地时间    time.localtime()
print(time.localtime(16346354584))
print(time.localtime().tm_yday)

# 时间戳转化为元组形式
# gmtime:结果为UTC时区
# local time：结果为UTC+8时区
