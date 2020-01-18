# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/16- 0:38
# 当前用户名： zc
# 文件名：function   （装饰器）

import time


# 装饰器
def timer(func):
	def deco(*arg, **kwargs):  # *arg为参数列表，这样无论test1,test2有多少参数都适用
		start_time = time.time()
		func(*arg, **kwargs)
		stop_time = time.time()
		print("the func run time is %s" % (stop_time - start_time))

	return deco


@timer  # 等同于test1 = timer(test1)
def test1():
	time.sleep(3)
	print("in the test1")


@timer
def test2(name):
	time.sleep(3)
	print("in the test2：", name)


# 使用装饰器
# deco(test1)
# deco(test2)

# 使用装饰器
# test1 = timer(test1)  # 或者在test1处上方直接用@+装饰器的名字即可
test1()  # 未改变调用形式
test2("zx")
