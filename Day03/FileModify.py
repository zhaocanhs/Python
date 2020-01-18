# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/15- 20:20
# 当前用户名： zc
# 文件名：文件修改


# with为了避免打开的文件忘记关闭，可以通过管理上下文
# f = open("test.txt", "r", encoding = "utf-8")
# 等同
with open("test.txt", "r", encoding = "utf-8") as f:
	print(f.readline())
# 同时打开两个及以上的文件
# with open() as objc1,open() as objc2:
# 	 pass
f_new = open("test2.txt", "w", encoding = "utf-8")

for line in f:
	if "czxv" in line:
		line = line.replace("czxv", "赵灿")
	f_new.write(line)
f.close()
f_new.close()
