# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/23- 23:39
# 当前用户名： zc
# 文件名：Class_test

class Dog:
	n = 123  # 类变量

	def __init__(self, name):
		# 构造函数
		# 在实例化的时候做一些类的初始化工作
		# 析构函数： 在实例释放、销毁的时候自动执行的，通常用于做一些收尾工作， 如关闭一些数据库连接，关闭打开的临时文件

		# 系统会自动执行析构函数，析构函数往往用来做清理善后的工作，比如说在建立对象时用new开辟了一片内存空间，delete会自动调用析构函数后释放内存。
		# 手动释放资源时，可以选择在哪一个环节释放变量资源，而在系统释放资源是在程序调用完成后，再释放资源，一般是在程序执行最后才进行资源释放。

		self.name = name  # 实例变量(静态属性)，作用域就是实例本身

	def say(self):  # 类的方法，功能（动态属性）
		print("%s 叫了" % self.name)


# 私有方法就是在函数名前加_

d1 = Dog("zx")  # 把一个类变成一个具体对象的过程叫实例化（初始化一个类，造一个对象）
d1.say()

# 继承
# class 孩子名字(父类名):
