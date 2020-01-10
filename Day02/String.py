# -*- coding:utf-8 -*-
# 作者：火小森

name = "zhangsan"
# 首字母大写
print(name.capitalize())

# 计数
print(name.count("a"))

# 打印50个字符，不够用-补充
print(name.center(50, '-'))

# 判断时候以an结尾
print(name.endswith("an"))

# 找到字符串中第一个字母索引
print(name.find("zhang"))

# 格式化
name2 = "my name is {name},age is {age}"
print(name2.format(name = 'zhaocan', age = 12))
print(name2.format_map({'name':'zhaohuoshan', 'age':12}))
n
# 纯数字
print('zc124'.isalnum())
# 纯英语
name.isalpha()

# 整数
'12'.isdigit()

# 判断是不是一个合法的标识符
name.isidentifier()

# join的用法
print('+'.join(['1', '2', '3']))

# 替换
print("zhaocan".replace('a', 'A', 1))

# 按指定的方式分成列表
print('zhaocan'.split('a'))
