# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/28- 15:19
# 当前用户名： zc
# 文件名：socket_client
# 客户端
import socket

client = socket.socket()
client.connect(('localhost', 8080))
while True:
	msg = input(">>:").strip()
	if len(msg) == 0:
		continue
	client.send(msg.encode('utf-8'))
	data = client.recv(10240)  # 接受的数据量大小
	print(data.decode())

client.close()
