# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/27- 3:21
# 当前用户名： zc
# 文件名：异常处理
name = ['zc', '12']
dataa = {}
try:
	# 尝试执行如下代码
	dataa['name']
except KeyError as e:
	# 除非出现KeyError错误
	print("没有这个key", e)
except Exception as e:
	pass
# 未知错误

finally:
	pass

# 不管有没有错都执行
