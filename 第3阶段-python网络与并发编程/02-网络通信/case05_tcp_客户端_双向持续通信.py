#coding=utf-8
from socket import *
'''
双向通信Socket之客户端
    将控制台输入的信息发送给服务端
    读取服务端的数据，将内容输出到控制台
'''

# 创建TCP类型的套接字
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
# 连接服务器端
tcp_client_socket.connect(('127.0.0.1', 8888))
while True:
    msg = input('>')
    # 向服务器发送数据
    tcp_client_socket.send(msg.encode('gbk'))
    if msg == 'end':
        break
    # 接收服务器端数据
    re_data = tcp_client_socket.recv(1024)
    print('服务器端', re_data.decode('gbk'))
tcp_client_socket.close()