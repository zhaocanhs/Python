# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/10- 21:39

# 集合
# 1.去重：把列表变成集合，自动去重
# 2.关系测试，测试两组数据之间的交集、并集、差集的=等关系

list_1 = [1, 2, 3, 23, 523, 12, 1, 2, 34, 23]
# 去重
list_1 = set(list_1)

list_2 = set([2, 3, 34, 2, 34, 67, 87, 35, 23])

print(list_1, list_2)

# 取交集
print(list_1.intersection(list_2))
list_1 & list_2

# 取并集
print(list_1.union(list_2))
list_1 | list_2
# 取差集
print(list_1.difference(list_2))
list_1 - list_2
# 取子集
print(list_1.issubset(list_2))

# 对称差集
list_1 ^ list_2

# 添加
list_1.add(909)
list_1.update([21, 1243, 2341])

# 查询
x in list_1  # 判断x是否是在list_1中

# 删除
list_1.pop()  # 随机删除
list_1.remove(1)
list_1.discard(2)

# 取父集
print(list_1.issuperset(list_2))
