# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/18- 22:30
# 当前用户名： zc
# 文件名：Json序列化
# JSON主要用于数据交互  主流
# XML也是用于数据交互，但是标签的式

# import json
import pickle  # pickle只有python可以用


# json序列化

def say(name):
	print("my name is ", name)


# info = {
# 	"name": "zc",
# 	"age": 23,
# 	"func": say
# }
# f = open("test.txt", 'wb')
# f.write(pickle.dumps(info))  # 把字典转化成字符串
# pickle.dump(info,f)  #等同于上面
# 多次dumps 多次load


# pickle.dumps()默认变成二进制


# json反序列化

f = open("test.txt", 'rb')


def sayhi(name):
	print("hello2,", name)


data = pickle.loads(f.read())  # 把字符串转化成字典
data = pickle.load(f)  # 等同于上面
print(data["func"]("zc"))
print(data["age"])  # 字典使用
