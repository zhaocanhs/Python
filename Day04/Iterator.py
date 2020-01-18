# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/18- 1:22
# 当前用户名： zc
# 文件名：Iterator (迭代器）

# 列表生成式
# a = [i * 2 for i in range(10)]
# print(a)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# 斐波那契数列
def fib(max):  # 10
	n, a, b = 0, 0, 1
	while n < max:  # n<10
		# print(b)
		yield b  # 变为生成器
		a, b = b, a + b
		n = n + 1
	return '---done---'


# print(fib(100))
# <generator object fib at 0x000001F1CCCFC248>

# 使用生成器
f = fib(100)  # 生成器只有__next__()方法
for i in range(10):
	print(f.__next__())

# 捕捉异常
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:  # 如果报的是StopIteration错误，就执行下面代码
		print('Generator return value:', e.value)
		break
