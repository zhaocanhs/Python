# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/2/12- 17:42
# 当前用户名： zc
# 文件名：Pymysql

import pymysql

# 连接数据库
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '111111root',
                       database = 'python')
cur = conn.cursor()  # cursor() 游标

user = input("USERNAME:")
pwd = input("PASSWORD:")
sql = 'select * from userinfo where user ="%s" and password ="%s";' % (user, pwd)

cur = conn.cursor(cursor = pymysql.cursors.DictCursor)  # 取出来的数据变成字典，

cur.execute('select * from user;')  # 一条
print(cur.rowcount)  # 获取查出多少行
# ret=cur.fetchone() #取第一行
# print(ret)
ret2 = cur.fetchmany(2)  # 多条#会在fetchone基础上开始找
# print(ret2)
ret3 = cur.fetchall()  # 全部结果
# 增删改
try:
	cur.execute("insert into user values(4,'test04')")
	conn.commit()  # 提交
except:
	conn.rollback()  # 回滚，不执行插入数据
cur.close()
conn.close()
