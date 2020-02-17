# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/29- 22:31
# 当前用户名： zc
# 文件名：网络编程

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
conn, addr = sk.accept()  # conn里存储的是一个客户端和server端的连接信息
conn.send(b'hello')
msg = con
