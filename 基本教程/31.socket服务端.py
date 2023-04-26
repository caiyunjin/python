'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-26 08:47:23
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-04-26 12:40:50
FilePath: \python\基本教程\31.socket服务端.py
Description: 

'''
# socket用于进程之间的网络通信

import socket

# 服务端
# 创建socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(('localhost', 8999))
# 监听端口
socket_server.listen(1)  # listen 接受连接数量
# 等待客户端连接
# accetp是阻塞方法，等待客户端连接，如没连接就不向下执行 返回的是二元元祖（连接对象，客户端地址信息）
conn, address = socket_server.accept()
print(f'接收到了客户端的连接，客户端的信息是:{address}')

while True:
    # 接收客户端信息，要使用客户端和服务的本次链接对象，而非socket_server对象
    # recv接受的参数是缓冲区大小，一般给1024，返回值是字节，不是字符串，所以需要decode('utf-8')
    data: str = conn.recv(1024).decode('utf-8')
    print(f'客户端发来的消息是:{data}')
    # 发送回复消息
    msg = input('请输入你要和客户端回复的消息：')
    if msg == 'exit':
        break
    conn.send(msg.encode('UTF-8'))
conn.close()
socket_server.close()
