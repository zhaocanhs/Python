# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/27- 2:24
# 当前用户名： zc
# 文件名：反射

# 通过字符串映射或修改程序运行时的状态、属性、方法,
# getattr(object,name ,default = None)
# hasattr(object,name  )   判断object中有没有一个name字符串对应的方法或属性
# setattr(x,y,z)
# delattr(x,y)
'''
反射
    hasattr(obj,name_str) , 判断一个对象obj里是否有对应的name_str字符串的方法
    getattr(obj,name_str), 根据字符串去获取obj对象里的对应的方法的内存地址
    setattr(obj,'y',z), is equivalent to ``x.y = v''   通过字符串设置属性
    delattr(x,y)
'''


# 反射代码示例
class Foo(object):

	def __init__(self):
		self.name = 'wupeiqi'

	def func(self):
		return 'func'


obj = Foo()

# #### 检查是否含有成员 ####
hasattr(obj, 'name')
hasattr(obj, 'func')

# #### 获取成员 ####
getattr(obj, 'name')
getattr(obj, 'func')

# #### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)

# #### 删除成员 ####
delattr(obj, 'name')
delattr(obj, 'func')
