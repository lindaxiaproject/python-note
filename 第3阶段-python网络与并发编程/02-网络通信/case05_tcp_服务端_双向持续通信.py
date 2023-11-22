# coding=utf-8
from socket import *

'''
    双向通信socket之服务器端
        读取客户端发送的数据，将内容输出到控制台
        将控制台输入的信息发送到客户端

'''
# 创建TCP类型的套接字
server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定接收信息接口
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen()
print("服务端已经启动，等待客户端链接！")
# 接收客户端链接
client_socket, client_info = server_socket.accept()
print("1个客户端建立链接成功！")
while True:
    recv_data = client_socket.recv(1024).decode('gbk')
    # 将消息输出到控制台
    print(f"客户端说：,{recv_data},来自:{client_info}")
    if recv_data == 'end':
        break
    # 获取控制台信息
    msg = input(">")
    client_socket.send(msg.encode("gbk"))

client_socket.close()
server_socket.close()
