# -*- coding:utf-8 -*-
# 作者：火小森

# 字典是无需的，键值对唯一

infor = {
	'stu01': "zhangsan",
	'stu02': "lisi",
	'stu03': "wangwu",
	'stu04': "zhaoliu",
	'stu05': "xiaozhao",

}
# 查找
print(infor['stu01'])
infor.get('stu01')
# 在infor中查找stu01
'stu01' in infor

# 添加
infor['stu06'] = "xiaobai"
print(infor)

# 删除
del infor['stu01']
infor.pop('stu01')
infor.popitem()  # 随机删除

# 修改
infor['stu01'] = "赵灿"

# 所有键值对的值
infor.values()

# 所有键值对的键
infor.keys()

# 原键值存在，修改值，原键值不存在，创建新的键值对
infor.setdefault({"stu01": "xiaoming"})

# 更新
b = {'stu33': "xiaohuo"}
infor.update(b)

# 初始化字典的值
c = dict.fromkeys([1, 2, 3], "test")  #键为1，2，3。值分别为test

# 更高效
for i in infor:
	print(i,infor[i])

for k,v in infor.items():
	print(k,v)
