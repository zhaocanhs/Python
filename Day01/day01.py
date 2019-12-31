#-*- coding:utf-8 -*-
#作者：火小森
print("hello world")

print(7+3)
name = "你好，世界"
print(name)

'''注释多行或者打印多行'''

# 输入
name=input("name:")
Age=input("age:")
job=input("job:")
Salary=input("salary:")
# %s占位符
info='''-----info of   %s-------
Name:%s
Age:%s
Job:%s
Salary:%s
'''% (name,name,Age,job,Salary)
print(info)