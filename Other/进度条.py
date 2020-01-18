# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/13- 17:49
# 当前用户名： zc
# 文件名：进度条

import sys, time

for i in range(50):
	sys.stdout.write("#")
	sys.stdout.flush()  # 刷新一下
	time.sleep(0.1)  # 0.1秒执行一次
