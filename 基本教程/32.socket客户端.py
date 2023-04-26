import socket

# 客户端
# 创建cocket对象
socket_client = socket.socket()
# 连接到服务端
socket_client.connect(('localhost', 8999))
while True:
    # 发送消息
    msg = input('请输入要给服务端发送的信息：')
    if msg == '退出':
        break
    socket_client.send(msg.encode('utf-8'))
    # 接受返回消息
    recv_data = socket_client.recv(1024)
    print(f"服务端回复的消息：{recv_data.decode('UTF-8')}")
# 关闭连接
socket_client.close()
