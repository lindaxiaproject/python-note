#coding=utf-8
from socket import *
# 创建TCP类型的套接字
server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定接收信息接口
server_socket.bind(('127.0.0.1',8899))
server_socket.listen(5)
client_socket, client_info = server_socket.accept()
# client_socket 表示这个新的客户端
# client_info 表示这个新的客户端的ip以及port
recv_data = client_socket.recvfrom(1024)
print(f"收到信息:{recv_data[0].decode('gbk')} ,from {client_info}")
client_socket.close()
server_socket.close()