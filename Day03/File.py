# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/10- 21:27

# 打开文件(open)并读取(read)  设置编码为utf-8
# f = open("test.txt", "r", encoding = "utf-8")  # f为文件句柄 w写模式，r读模式
# a为可读可写
# 写内容
# f.write("zhaocan\n")
# f.write("nihao")

# f.close()         #文件关闭

# 读前5行
# for i in range(5):
# print(f.readline())

# for line in f.readlines():  #readlines()把文件变成列表，每一行为元素
#   	print(line.strip())  # strip()把空格和换行去掉
# enumerate()取下标
# readlines()适合小文件读取
# for index, line in enumerate(f.readlines()):
# 	if index == 9:
# 		print("______________________________分割线————————————————————————")
# 		continue
# 	print(line.strip())

# 一行一行的读取  高级 高效
'''
count = 0
for line in f:
	if count == 9:
		print("______________________________分割线————————————————————————")
		count += 1
		continue
	print(line.strip())
	count += 1
'''
# 字符计数
# f.tell()
# 读取5个字符
# f.read(5)
# 读一行
# print(f.readline())
# 回到起始位置
# f.seek(0)
# 文件的编码
# f.encoding
# # 文件接口
# f.fileno()
# #刷新内存
# f.flush()

# f = open("test.txt", 'r+', encoding = "utf-8")  # 文件读写  打开，读，追加   a+追加写读写
'''
f = open("test.txt", 'w+', encoding = "utf-8")  # 文件写读 #没大用
f.write("--------1-------------\n")
f.write("--------2-------------\n")
f.write("--------3-------------\n")
f.write("--------4-------------\n")
f.write("--------5-------------\n")
print(f.tell())
f.seek(10)
print(f.readline())S
f.write("asdfgfagfgassd")
f.close()
'''

# rb,  二进制文件读
# wb,二进制文件写
# ab,二进制文件追加
f = open("test.txt", 'wb')
f.write("hello zhao\n".encode())  # encode()转换编码
