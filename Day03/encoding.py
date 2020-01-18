# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/15- 23:45
# 当前用户名： zc
# 文件名：encoding

import sys

print(sys.getdefaultencoding())  # 当前文件编码格式

'''
s = "你好"  # 默认是Unicode
s_gbk = s.encode("gbk") #把Unicode字符编码变成gbk
print("gbk:", s_gbk)  # gbk
# b'\xc4\xe3\xba\xc3'
print("utf-8:", s.encode())  # utf-8
# b'\xe4\xbd\xa0\xe5\xa5\xbd'

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print("utf-8:", gbk_to_utf8)
# b'\xe4\xbd\xa0\xe5\xa5\xbd'
'''

s = "你好"
print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))  # 最后的decode("gb2312")是将其转化成中文
