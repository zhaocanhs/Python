# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/18- 19:58
# 当前用户名： zc
# 文件名：生成器并行  （单线程下的并行效果）

import time


def consumer(name):
	print("%s 准备吃包子啦!" % name)
	while True:
		baozi = yield  # 从这里出去，又从这进来，生成器的出口

		print("包子[%s]来了,被[%s]吃了!" % (baozi, name))


c = consumer("ChenRonghua")
c.__next__()  # 从yield处进去


# b1= "韭菜馅"
# c.send(b1) #发送值给yield
# c.__ext__()

def producer(name):
	c = consumer('A')
	c2 = consumer('B')
	c.__next__()
	c2.__next__()
	print("老子开始准备做包子啦!")
	for i in range(10):
		time.sleep(1)
		print("做了1个包子,分两半!")
		c.send(i)
		c2.send(i)


producer("alex")
