# -*- coding:utf-8 -*-
# 作者：火小森
import copy

'''
person = ['name', ['a', 100]]

# 浅拷贝1
p1 = copy.copy(person)
# 浅拷贝2
p2 = person[:]
# 浅拷贝3
p3 = list(person)
'''

person = ['name', ['saving', 100]]
p1 = person[:]
p2 = person[:]

p1[0] = "zhangsan"
p2[0] = "lisi"

p1[1][1] = "50"  # 浅拷贝的联合操作（100）

print(p1)
print(p2)
