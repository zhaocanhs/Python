# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/28- 15:23
# 当前用户名： zc
# 文件名：socket_server

# 服务器端
import socket
import os

sever = socket.socket()
sever.bind(('localhost', 8080))  # 绑定要监听的端口
sever.listen(5)  # 监听 5个人等待发信息
# conn是电话,addr是地址即IP地址
# conn就是客户端连过来而在服务器端为其生成的一个连接实例
conn, addr = sever.accept()  # 等电话打进来
print(conn, addr)
count = 0
while True:
	data = conn.recvfrom(1024)
	print("recv:", data)
	if not data:
		print("data lost....")
		break
	conn.send(data.upper())
	count += 1
	if count > 10:
		break
	res = os.popen(data).read()
	conn.send(res)

sever.close()
