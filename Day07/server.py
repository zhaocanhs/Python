# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/28- 15:16
# 当前用户名： zc
# 文件名：server

# 服务器端

import socket

server = socket.socket()
# IP地址和端口
server.bind(('localhost', 6969))  # 绑定要监听端口
server.listen(5)  # 监听

print("我要开始等电话了")
while True:
	conn, addr = server.accept()  # 等电话打进来
	# conn就是客户端连过来而在服务器端为其生成的一个连接实例
	print(conn, addr)
	print("电话来了")
	count = 0
	while True:
		# recv收
		data = conn.recv(1024)
		print("recv:", data)
		if not data:
			print("client has lost...")
			break
		conn.send(data.upper())
		count += 1
		if count > 10: break

server.close()
