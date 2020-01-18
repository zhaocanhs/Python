# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/17- 0:14
# 当前用户名： zc
# 文件名：破解（myBase Desktop 7.3.3）


import fileinput

import re

import time

import sys

file_path = "myBase.ini"

file_path = r"D:\Users\zc\AppData\Local\wjjsoft\nyfedit7\myBase.ini"

to_change = {

	"App.UserLic.FirstUseOn=": str(int(time.time())),

	"App.UserLic.LaunchNum=": str(0),

	"App.UserLic.SecsUsed=": str(0),

}

for line in fileinput.input([file_path], inplace = 1):

	for key in to_change.keys():

		if re.match(key, line):
			sys.stdout.write(f"{key}{to_change[key]}\n")

			sys.stdout.flush()

			break

	else:

		sys.stdout.write(line)

		sys.stdout.flush()

fileinput.close()

print("done!")
