# -*- coding:utf-8 -*-
# 作者：火小森
# 日期： 20/1/28- 12:48
# 当前用户名： zc
# 文件名：Socket(网络编程)
import socket

# 创建socket对象
server = socket.socket()
# 绑定IP和端口
server.bind('192.168.0.1', 8000)
# 后边可以等5个人
server.listen(5)
# 等待客户端来连接，如果没人来就傻傻的等待。
ret1 = server.accept()
print(ret1)
