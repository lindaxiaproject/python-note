#coding=utf-8
from socket import *
# 创建UDP类型的套接字
s = socket(AF_INET, SOCK_DGRAM)
# 绑定接收信息接口
s.bind(('127.0.0.1',8888))
print("等待接收数据.....")
# 1024表示本次接收的最大字节数
recv_data = s.recvfrom(1024)
print(f"收到远程信息:{recv_data[0].decode('gbk')} ,from {recv_data[1]}")
s.close()